import os
import sys
import cocos
from cocos.actions import *
from background import Background
#from cocos.actions import *
#from cocos import actions, layer, sprite, scene
import pyglet
from pyglet.window import key
from pyglet.window.key import KeyStateHandler
import cocos.euclid as eu
import cocos.collision_model as cm


def width():
    return cocos.director.director.window.width


def height():
    return cocos.director.director.window.height


class Animation(cocos.layer.Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self,exit_callback):

        super(Animation, self).__init__()

        self.keys_pressed = set()
        self.exit = exit_callback

        self.spaceship_move = None
        self.spaceship_move_duration = 2
        self.spaceship_move_step = 200
        self.spaceship = cocos.sprite.Sprite('spaceship.png')
        self.spaceship.position = (width()/2, 100)
        self.spaceship.scale = 1
        self.spaceship.name = "SPACESHIP"
        self.spaceship.cshape = cm.CircleShape(eu.Vector2(self.spaceship.position[0], self.spaceship.position[1]), self.spaceship.width/2)

        self.collision_manager = cm.CollisionManagerBruteForce()
        
        self.bullet_move = None
        self.bullet_move_duration = 3
        self.bullet_move_step = height()

        self.bullets = []
        self.shots = 0

        self.asteroids = []
        
        self.add(self.spaceship, z=0)

        self.init_asteroids()

        self.schedule(self.update)

    def on_key_press(self, key, modifiers):
        """This function is called when a key is pressed.
        
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        See also on_key_release situations when a key press does not fire an
         'on_key_press' event.
        """
        self.keys_pressed.add(key)


    def on_key_release(self, key, modifiers):
        """This function is called when a key is released.
        
        'key' is a constant indicating which key was pressed.
        'modifiers' is a bitwise or of several constants indicating which
           modifiers are active at the time of the press (ctrl, shift, capslock, etc.)
        Constants are the ones from pyglet.window.key
        Sometimes a key release can arrive without a previous 'press' event, so discard
        is used instead of remove.
        This can happen in Windows by example when you 'press ALT, release ALT, press B,
        release B'; the events received are 'pressed ALT, released ALT, released B'.
        This may depend on the pyglet version, here pyglet from repo at may 2014 was used.
        """
        self.keys_pressed.discard(key)

    def init_asteroids(self):
        i = 0
        j = 0
        while i < 10:
            while j < 5:
                self.init_asteroid(i,j)
                j += 1
            j = 0
            i += 1

        
    def init_asteroid(self,x,y):
        asteroid = cocos.sprite.Sprite('asteroids/small/a300{0:02}.png'.format(x))
        asteroid.scale = 1
        asteroid.position = asteroid.width/2 + x * asteroid.width, height() - y * asteroid.height - asteroid.height/2 
        asteroid.cshape = cm.AARectShape(eu.Vector2(asteroid.position[0], asteroid.position[1]), asteroid.width/2,asteroid.height/2)
        asteroid.name = "ASTEROID"
        asteroid.do(Repeat(RotateBy(180,2)))
        
        if y == 4 :
            self.collision_manager.add(asteroid)
            self.asteroids.append(asteroid)
            self.add(asteroid,z=0)

        

    def shot(self):
        bullet = cocos.sprite.Sprite('asteroids/small/a10000.png')
        bullet.scale = 1
        bullet.position = (self.spaceship.position[0],self.spaceship.position[1]+self.spaceship.height)
        bullet.cshape = cm.CircleShape(eu.Vector2(bullet.position[0], bullet.position[1]), bullet.width/2)
        bullet.do(Repeat(MoveBy((0,self.bullet_move_step),self.bullet_move_duration)))
        bullet.name = "BULLET"
        self.collision_manager.add(bullet)
        self.shots += 1
        self.add(bullet, z=1)
        self.bullets.append(bullet)

    def remove_bullets(self):
        for bullet in self.bullets:
            if bullet.position[1] > height():
                self.remove(bullet)
                self.bullets.remove(bullet)
                self.collision_manager.remove_tricky

    def spaceship_position(self):
        if self.spaceship.position[0] <= 0:
            self.spaceship.stop
            self.spaceship.do(Place( (width(),self.spaceship.position[1])))
            if self.spaceship_move:
                self.spaceship.do((self.spaceship_move))
        if self.spaceship.position[0] > width():
            self.spaceship.stop
            self.spaceship.do(Place( (0,self.spaceship.position[1])))
            if self.spaceship_move:
                self.spaceship.do((self.spaceship_move))
        if self.spaceship.position[1] <= 0:
            self.spaceship.stop
            self.spaceship.do(Place( (self.spaceship.position[0],height())))
            if self.spaceship_move:
                self.spaceship.do((self.spaceship_move))
        if self.spaceship.position[1] > height():
            self.spaceship.stop
            self.spaceship.do(Place( (self.spaceship.position[0],0)))
            if self.spaceship_move:
                self.spaceship.do((self.spaceship_move))

    def move_spaceship(self):
        x = 0
        y = 0

        if pyglet.window.key.LEFT in self.keys_pressed :
            x = self.spaceship_move_step * (-1)
        if pyglet.window.key.RIGHT in self.keys_pressed :
            x = self.spaceship_move_step
        if pyglet.window.key.UP in self.keys_pressed :
            y = self.spaceship_move_step
        if pyglet.window.key.DOWN in self.keys_pressed :
            y = self.spaceship_move_step * (-1)


        if x != 0 or y != 0 :
            self.spaceship_move = MoveBy((x,y),self.spaceship_move_duration)
            self.spaceship.do(self.spaceship_move)
        elif self.spaceship_move:
            self.spaceship.do(self.spaceship_move)
   


    def update(self,dt):

        for hit in self.collision_manager.iter_all_collisions():
              if hit[0].name != hit[1].name:
                if hit[0].name == "BULLET" and hit[0] in self.bullets:
                    self.bullets.remove(hit[0])
                    self.remove(hit[0])
                if hit[1].name == "BULLET" and hit[1] in self.bullets:
                    self.bullets.remove(hit[1])
                    self.remove(hit[1])
                if hit[0].name == "ASTEROID" and hit[0] in self.asteroids:
                    self.asteroids.remove(hit[0])
                    self.remove(hit[0])
                if hit[1].name == "ASTEROID" and hit[1] in self.asteroids:
                    self.asteroids.remove(hit[1])
                    self.remove(hit[1])

        self.collision_manager.clear()
        self.remove_bullets()
        self.spaceship_position()
        self.move_spaceship()

        if pyglet.window.key.SPACE in self.keys_pressed :
            self.shot()
            self.keys_pressed.remove(pyglet.window.key.SPACE)
        if pyglet.window.key.Q in self.keys_pressed :
            self.exit(False)

        for obj in self.asteroids:
            self.collision_manager.add(obj) 
        for obj in self.bullets:
            self.collision_manager.add(obj) 
       
        if not self.asteroids:
            self.exit(True)

class SpaceInvader():
    def __init__(self,exit_callback):
        self.animation_layer = Animation(exit_callback)
        self.background_layer = Background()

        self.background_layer.image = 'space.jpg'

    def main_scene(self):
        return cocos.scene.Scene(self.background_layer,self.animation_layer)


def main():
    here = os.path.abspath(os.path.dirname(__file__))
    graphics = os.path.join(here, 'graphics')

    import pyglet.resource
    pyglet.resource.path = [graphics]
    pyglet.resource.reindex()

    cocos.director.director.init()

    game = SpaceInvader(sys.exit)

    cocos.director.director.run(game.main_scene())



if __name__ == '__main__':
    main()
