
import cocos
from cocos.layer import Layer
from cocos.sprite import Sprite


class Background(Layer):

    is_event_handler = True

    def __init__(self):
        super().__init__()
        self._image = None

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, val):
        image = self._image
        if image:
            self.remove(image)
        if not val:
            return

        self._image = image = Sprite(val, opacity=100, anchor=(0, 0))
        self.add(image)
        image.position = (cocos.director.director.window.width - image.width, 65)

    def on_resize(self, width, height):
        self._image.position = (cocos.director.director.window.width - self._image.width - 10, 65)
