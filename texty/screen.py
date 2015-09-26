import pyglet
import cocos

DEFAULT_INPUT = 'Eingabe: '
FONT_SIZE = 15
HIS_WIDTH = 240
HIS_FONT_SIZE = 13


def width():
    return cocos.director.director.window.width


def height():
    return cocos.director.director.window.height


class MainScreen():

    def __init__(self, callback):
        cocos.director.director.init(resizable=True, autoscale=False, width=1024, height=800)
        self.screen = Screen()
        self.history = History()
        self.main_scene = cocos.scene.Scene(self.screen, self.history, KeyDisplay(callback))

    def run(self):
        cocos.director.director.run(self.main_scene)

    def text(self, text):
        self.screen.text(text)


class Screen(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self):
        super(Screen, self).__init__()
        self.label = None
        self.redraw_label()

    def text(self, text):
        self.label.element.text = text

    def on_resize(self, width, height):
        self.redraw_label()

    def redraw_label(self):
        text = None
        if self.label:
            text = self.label.element.text
            self.remove(self.label)
        else:
            text = ''
        self.label = cocos.text.Label(text,
            font_name='Times New Roman',
            font_size=FONT_SIZE,
            anchor_x='left', anchor_y='top', multiline=True, width=width() - 10)
        self.label.position = HIS_WIDTH + 10, height() - 10
        self.add(self.label)
        self.draw()


class History(cocos.layer.ScrollableLayer):

    def __init__(self):
        super(History, self).__init__()
        self.label = cocos.text.Label('',
                                      font_name='Times New Roman',
                                      font_size=HIS_FONT_SIZE,
                                      anchor_x='left',
                                      anchor_y='top',
                                      multiline=True,
                                      width=HIS_WIDTH,
                                      x=0, y=5)
        self.add(self.label)


class KeyDisplay(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self, callback):
        super(KeyDisplay, self).__init__()
        self.callback = callback

        self.text_label = cocos.text.Label("", x=HIS_WIDTH + 10, y=5, font_size=FONT_SIZE)
        self.text = DEFAULT_INPUT

        self.update_text()
        self.add(self.text_label)

    def on_text(self, char):
        self.text += char
        self.update_text()

    def on_key_press(self, key, modifiers):
        if key == pyglet.window.key.BACKSPACE and self.text != DEFAULT_INPUT:
            self.text = self.text[:-1]
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
