import cocos


class MainScreen():

    def __init__(self, callback):
        cocos.director.director.init()
        self.screen = Screen(callback)
        self.main_scene = cocos.scene.Scene(self.screen)

    def run(self):
        cocos.director.director.run(self.main_scene)

    def text(self, text):
        self.screen.text(text)


class Screen(cocos.layer.Layer):

    def __init__(self, callback):
        super(Screen, self).__init__()
        self.callback = callback
        self.label = cocos.text.Label('Hello World!',
            font_name='Times New Roman',
            font_size=18,
            anchor_x='center', anchor_y='center', multiline=True, width=320)
        self.label.position = 160, 460
        self.add(self.label)

    def text(self, text):
        pass
