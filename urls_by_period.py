
import RIScraper

def urls_by_period(subreddit_name, start_date, end_date):
    
    reddit = RIScraper.bot_login()
    subreddit = reddit.subreddit('wallpapers')

    submissions = subreddit.submissions(
            start=start_date, end=end_date)
    
    ret_value = list()
    for submission in submissions:
        ret_value.append(submission.url)
        
    return ret_value


def main():
    
    # https://www.epochconverter.com/
    urls = urls_by_period(
            'wallpapers', 
            1488961062, 
            1489047462)
            
    for url in urls:
        print(url)


if __name__ == '__main__':
    main()
