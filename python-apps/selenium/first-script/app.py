from selenium import webdriver


class FirstBot(webdriver.Chrome):

    def __init__(self):
        super().__init__()

    def say_hi(self):
        print("Hello World")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Class FirstBot...")


def main():
    with FirstBot() as bot:
        # bot = FirstBot()
        bot.say_hi()


if __name__ == '__main__':
    main()
