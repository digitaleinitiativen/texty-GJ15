from .screen import MainScreen


def got_text(text):
    print(text)


def main():
    s = MainScreen(got_text)
    s.text('Hello World!')
    s.run()


if __name__ == '__main__':
    main()
