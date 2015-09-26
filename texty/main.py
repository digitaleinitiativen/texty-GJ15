

import cocos


class HelloWorld(cocos.layer.Layer):
    def __init__(self):
        super( HelloWorld, self ).__init__()



def main():
    cocos.director.director.init()
    h = HelloWorld()
    main_scene = cocos.scene.Scene (h)
    cocos.director.director.run (main_scene)


if __name__ == '__main__':
    main()
