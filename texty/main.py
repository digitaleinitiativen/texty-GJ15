
from .screen import MainScreen
from .text_mode import main as text_main

def got_text(text):
    print(text)


def main():
    text_main()


def graph_main():
    s = MainScreen(got_text)
    s.text('Hello World!')
    s.run()

if __name__ == '__main__':
    main()
