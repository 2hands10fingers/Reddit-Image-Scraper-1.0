import praw
import config


def bot_login():
    r = praw.Reddit(username=config.username,
                    password=config.password,
                    client_secret=config.client_secret,
                    client_id=config.client_id,
                    user_agent="RedditImageScraper by /u/2hands10fingers, /u/Joe_Anonimist, /u/iakovosbelonias")
    return r


if __name__ == '__main__':
    r = bot_login()

    print(r)
