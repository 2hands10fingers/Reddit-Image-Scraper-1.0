import RIScraper
from requests import get
import time

def urls_by_period(subreddit_name, start_date, end_date):

    reddit = RIScraper.bot_login()
    subreddit = reddit.subreddit(subreddit_name)

    submissions = subreddit.submissions(
            start=start_date, end=end_date)

    ret_value = list()
    for submission in submissions:
        ret_value.append(submission.url)

    return ret_value

def dlfile(url):
    fileName = str(url).split('/')[-1]
    #fileName = str(url).rsplit('/', maxsplit=-1)
    with open(fileName, "wb") as file:
        response = get(str(url))
        file.write(response.content)

def main():

    # https://www.epochconverter.com/
    urls = urls_by_period(
            'wallpapers',
            1488961062,
            1489047462)

    for url in urls:
        list_of_urls = []
        list_of_urls.append(url)
        if url.endswith(('.jpg', '.png')):
        #'.jpg' or '.png' in str(url):
            dlfile(url)
            #time.sleep(1.0)

if __name__ == '__main__':
    main()
