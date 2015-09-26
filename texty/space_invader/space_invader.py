import cocos
from texty.layers.background import Background
from cocos.actions import *
import pyglet
from pyglet.window import key
from pyglet.window.key import KeyStateHandler

def width():
    return cocos.director.director.window.width


def height():
    return cocos.director.director.window.height


class Animation(cocos.layer.Layer):

    is_event_handler = True     #: enable pyglet's events

    def __init__(self):

        super(Animation, self).__init__()

        self.spaceship_move = None
        self.spaceship_move_speed = 0.1
        self.spaceship_move_step = 10
        self.spaceship = cocos.sprite.Sprite('graphics/spaceship.png')
        self.spaceship.position = (320, 240)
        self.spaceship.scale = 1
        
        self.bullet_move = None
        self.bullet_move_speed = 0.1
        self.bullet_move_step = 20

        self.bullets = []

        self.asteroids = []
        
        self.add(self.spaceship, z=1)
        self.keys_pressed = set()

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
            self.asteroids.append([])
            while j < 5:
                self.asteroids[i].append(self.init_asteroid(i,j))
                j += 1
            j = 0
            i += 1

        
    def init_asteroid(self,x,y):
        if y == 0:
            asteroid = cocos.sprite.Sprite('graphics/asteroids/small/a300{0:02}.png'.format(x))
        elif y == 1:
            asteroid = cocos.sprite.Sprite('graphics/asteroids/small/a400{0:02}.png'.format(x))
        elif y == 2:
            asteroid = cocos.sprite.Sprite('graphics/asteroids/small/b100{0:02}.png'.format(x))
        else:
            asteroid = cocos.sprite.Sprite('graphics/asteroids/small/b400{0:02}.png'.format(x))
        asteroid.scale = 1
        asteroid.position = asteroid.width/2 + x * asteroid.width, height() - y * asteroid.height - asteroid.height/2 
        self.add(asteroid,z=0)
        asteroid.do(Repeat(RotateBy(180,2)))
        return asteroid

        

    def shot(self):
        bullet = cocos.sprite.Sprite('graphics/asteroids/small/a10000.png')
        bullet.scale = 1
        bullet.position = (self.spaceship.position[0],self.spaceship.position[1]+self.spaceship.height)
        bullet.do(Repeat(MoveBy((0,self.bullet_move_step),self.bullet_move_speed)))
        self.add(bullet, z=1)
        self.bullets.append(bullet)

    def remove_bullets(self):
        for bullet in self.bullets:
            if bullet.position[1] > height():
                self.remove(bullet)
                self.bullets.remove(bullet)

    def spaceship_position(self):
        if self.spaceship.position[0] < 0:
            self.spaceship.stop
            self.spaceship.do(Place( (width(),self.spaceship.position[1])))
            if self.spaceship_move:
                self.spaceship.do((self.spaceship_move))
        if self.spaceship.position[0] > width():
            self.spaceship.stop
            self.spaceship.do(Place( (0,self.spaceship.position[1])))
            if self.spaceship_move:
                self.spaceship.do((self.spaceship_move))
        if self.spaceship.position[1] < 0:
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
            self.spaceship_move = MoveBy((x,y),self.spaceship_move_speed)
            self.spaceship.do(self.spaceship_move)
        elif self.spaceship_move:
            self.spaceship.do(self.spaceship_move)
   


    def update(self,dt):
        self.remove_bullets()
        self.spaceship_position()
        self.move_spaceship()
        if pyglet.window.key.SPACE in self.keys_pressed :
            self.shot()
            self.keys_pressed.remove(pyglet.window.key.SPACE)
       

def main():
    # director init takes the same arguments as pyglet.window
    cocos.director.director.init()

    # We create a new layer, an instance of SpaceInvader
    animation_layer = Animation()
    #background_layer = 
   # shots_layer = Shots()

    # tell the layer to perform a Rotate action in 10 seconds.
    #test_layer.do(RotateBy(360, duration=10))

    # A scene that contains the layer test_layer
    main_scene = cocos.scene.Scene(animation_layer)


    # And now, start the application, starting with main_scene
    cocos.director.director.run(main_scene)

    # or you could have written, without so many comments:
    #      director.run( cocos.scene.Scene( SpaceInvader() ) )




if __name__ == '__main__':
    main()