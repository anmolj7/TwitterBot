import os
import feedparser


def get_post_text():
    breakline()
    print('Fetching The latest Article.')
    url = "https://fedoramagazine.org/feed/"
    feed = feedparser.parse(url)
    text = feed['entries'][0].title+': '+feed['entries'][0].link
    breakline()
    print('Fetched! Posting!')
    breakline()
    return text


def clear():
    if os.name == "posix":  # posix stands for linux
        os.system('clear')
    else:
        os.system('cls')


def breakline():
    print('-' * 70)


def get_choice():
    breakline()
    choice = input("Your choice: ")
    breakline()
    return choice


def main():
    clear()
    breakline()
    print('TWITTER BOT - EmperorAj')
    breakline()
    print('A script to post the latest posts from Fedora Magzine\'s blog')
    breakline()
    from TwitterBot import Bot
    bot = Bot()
    bot.tweet(f'{get_post_text()}')


if __name__ == '__main__':
    main()
