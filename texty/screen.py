import pyglet
import cocos

DEFAULT_INPUT = 'Eingabe: '


class MainScreen():

    def __init__(self, callback):
        cocos.director.director.init()
        self.screen = Screen()
        self.main_scene = cocos.scene.Scene(KeyDisplay(callback), self.screen)

    def run(self):
        cocos.director.director.run(self.main_scene)

    def text(self, text):
        self.screen.text(text)


class Screen(cocos.layer.Layer):

    def __init__(self):
        super(Screen, self).__init__()
        self.label = cocos.text.Label('',
            font_name='Times New Roman',
            font_size=18,
            anchor_x='center', anchor_y='center', multiline=True, width=320)
        self.label.position = 160, 460
        self.add(self.label)

    def text(self, text):
        self.label.element.text = text


class KeyDisplay(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self, callback):
        super(KeyDisplay, self).__init__()
        self.callback = callback

        self.text_label = cocos.text.Label("", x=5, y=5)
        self.text = DEFAULT_INPUT

        self.update_text()
        self.add(self.text_label)

    def on_text(self, char):
        self.text += char
        self.update_text()

    def on_key_release(self, key, modifiers):
        if key == pyglet.window.key.RETURN:
            self.submit()

    def update_text(self):
        self.text_label.element.text = self.text

    def submit(self):
        self.callback(self.text)
        self.text = DEFAULT_INPUT
        self.update_text()
