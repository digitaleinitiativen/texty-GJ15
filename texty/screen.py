import pyglet
import cocos
from texty.layers.background import Background

DEFAULT_INPUT = 'Was willst du tun? '
FONT_SIZE = 15
HIS_WIDTH = 240
HIS_FONT_SIZE = 11

FONT = 'Arial'
HISTORY_FONT = 'Courier New'
TITLE_FONT = 'Courier New'

TITLE_SIZE = 40
TITLE_FONT_SIZE = 35
TITLE_COLOR = (0, 255, 0, 255)
TITLE = "Munckin Cat Milky Way Odyssey"


def width():
    return cocos.director.director.window.width


def height():
    return cocos.director.director.window.height


class MainScreen():

    def __init__(self, callback):
        cocos.director.director.init(resizable=True, autoscale=False, width=1024, height=800)
        self.history = History()
        self.screen = Screen(self.history)
        self.background = Background()
        self.main_scene = cocos.scene.Scene(
            self.background,
            self.screen,
            self.history,
            KeyDisplay(callback, self.history)
        )

    def run(self):
        cocos.director.director.run(self.main_scene)

    def text(self, text):
        self.screen.text(text)


class Screen(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self, history):
        super(Screen, self).__init__()
        self.history = history
        self.label = None
        self.already_in_history = set()
        self.title = cocos.text.Label(
            TITLE,
            font_name=TITLE_FONT,
            font_size=TITLE_FONT_SIZE,
            width=width(),
            color=TITLE_COLOR)
        self.add(self.title)
        self.redraw_label()

    def text(self, text):
        if not text in self.already_in_history:
            self.history.add_text(text)
            self.already_in_history.add(text)
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
            font_name=FONT,
            font_size=FONT_SIZE,
            anchor_x='left', anchor_y='top', multiline=True, width=width() - 10 - HIS_WIDTH)
        self.label.position = HIS_WIDTH + 10, height() - 10 - TITLE_SIZE
        self.title.position = (width() - self.title.element.content_width) / 2, height() - TITLE_SIZE - 10
        self.add(self.label)
        self.draw()


class History(cocos.layer.ScrollableLayer):

    is_event_handler = True

    def __init__(self):
        super(History, self).__init__()
        self.label = None
        self.redraw_label()

    def add_text(self, text):
        self.label.element.text += text + '\n\n\n'
        self.autoscroll()

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
                                      font_name=HISTORY_FONT,
                                      font_size=HIS_FONT_SIZE,
                                      anchor_x='left',
                                      anchor_y='top',
                                      multiline=True,
                                      width=HIS_WIDTH,
                                      x=10, y=height() - 10 + TITLE_SIZE)
        self.add(self.label)
        self.autoscroll()

    def on_mouse_scroll(self, x, y, delta_x, delta_y):
        if (self.label.element.content_height > height() and (self.label.position[1] > 0 or delta_y > 0)):
            self.label.position = (self.label.position[0],
                                   self.label.position[1] + delta_y)

    def autoscroll(self):
        if self.label.element.content_height > height() - 10:
            self.label.position = (0, self.label.element.content_height - height() - 10 - TITLE_SIZE)


class KeyDisplay(cocos.layer.Layer):

    is_event_handler = True

    def __init__(self, callback, history):
        super(KeyDisplay, self).__init__()
        self.callback = callback
        self.history = history

        self.text_label = cocos.text.Label("", x=HIS_WIDTH + 10, y=5 + TITLE_SIZE, font_size=FONT_SIZE)
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
        self.history.add_text(self.text[len(DEFAULT_INPUT):])
        self.text = DEFAULT_INPUT
        self.update_text()
