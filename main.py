import time
from jdk.bin.setup_bot import setup
from bot import MusicBot


def main():
    bot = MusicBot()
    time.sleep(10)
    bot.run()


if __name__ == "__main__":
    setup()
    main()
