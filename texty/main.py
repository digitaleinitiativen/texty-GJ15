import cocos
from .screen import Screen


def main():
    cocos.director.director.init()
    s = Screen()
    main_scene = cocos.scene.Scene(s)
    cocos.director.director.run(main_scene)


if __name__ == '__main__':
    main()
