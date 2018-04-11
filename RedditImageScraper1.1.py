from os import name, system, path, makedirs
import config
import redditaccess
from delorean import Delorean
from datetime import datetime
from time import sleep
from json import loads
from re import findall, sub
from bs4 import BeautifulSoup as bs
from requests import get

######################### # # # # # #
### REDDIT IMAGE SCRAPER 1.1 # # # # #
######################### # # # # # # 

def clear_screen():
    # Check for OS. 'nt' = windows.
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def time_clear_header1():
    sleep(0.9)
    clear_screen()
    banner =  f"""
          .___________________________________________.
         /                                             \\
        |    Welcome to the Reddit Image Scraper 1.0    |
        |               by pyStudyGroup                 |
         +~____________________________________________~+  """

    print(banner)


def time_clear_headerSTART(month_b, day_b, year_b):
    sleep(0.9)
    clear_screen()

    banner = f"""
          .___________________________________________.
         /                                             \\
        |    Welcome to the Reddit Image Scraper 1.0    | 
        |      DATE RANGE: {month_b}-{day_b}-{year_b} --                  |
         +~____________________________________________~+ """
  
    print(banner)


def time_clear_headerEND(month_b, day_b, year_b, month_e, day_e, year_e):
    sleep(0.9)
    clear_screen()
    banner = f"""
          .___________________________________________. 
         /                                             \\
        |    Welcome to the Reddit Image Scraper 1.0    | 
        |    DATE RANGE: {month_b}-{day_b}-{year_b} -- {month_e}-{day_e}-{year_e}   \t|
         +~____________________________________________~+ """
    
    print(banner)

def validate_date(valid_range, message):
    selected_date = int(input(message))

    while not valid(selected_date, valid_range):
        
        print(f"\n\tWoops! Try entering a valid number. {selected_date} was not a valid number.")
        sleep(2)
        time_clear_header1()

    return selected_date

def set_date_range(month):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    if month in days_31:
        valid_range = range(1, 32)

    elif month in days_30:
        valid_range = range(1, 31)

    else:
        valid_range = range(1, 29) # February. I'll figure out leap years later.

    return valid_range

def valid(selected_date, valid_range):

    return selected_date in valid_range

def urls_by_period(subreddit_name, start_date, end_date):
    """ # ((url, date_string), (url, date_string), (url, date_string) ...) """
    reddit = redditaccess.bot_login()
    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.submissions(start=start_date, end=end_date)
    ret_list = list()

    for submission in submissions:
        file_list = list()
        date_created = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y%m%d_%H%M%S_')

        file_list.append(submission.url)
        file_list.append(date_created)
        file_list.append(submission.title)
        ret_list.append(file_list)

    return ret_list

def download_file(url, date_created, filename, subreddit):
    folder = path.join(config.file_path, subreddit)

    if not path.exists(folder):
        makedirs(folder)

    the_path = path.join(folder, filename)

    with open(the_path, 'wb') as f:
        start = datetime.now()
        response = get(url)

        if not response.status_code == 200:
            return -1 # If the request fails, it returns -1

        f.write(response.content)
    return start

def main():
    year_range = range(2005, int(datetime.now().year)+1)
    month_range = range(1, 13)
    year_start_msg = '\n\tEnter the year you would like to START your range: \n\t'
    year_end_msg = '\n\tEnter the year you would like to END your range: \n\t'
    month_msg = '\n\tNow, how about a month: '
    day_msg = '\n\tLastly, enter the day: '

    ########################
    ### START DATE LOGIC ###
    ########################

    sleep(0.2)
    time_clear_header1()
    year_b = validate_date(year_range, year_start_msg)

    print(f'\n\tExcellent!{year_b} is a great year.')
    time_clear_header1()

    month_b = validate_date(month_range, month_msg)

    print("\n\tWe'll accept that")
    time_clear_header1()

    date_range = set_date_range(month_b)
    day_b = validate_date(date_range, day_msg)

    print("\n\tLooks good to us.")
    print(f'\n\n\tYou have selected a start date of: {month_b}-{day_b}-{year_b}')
    print("\n\n\tIs this correct? We hope so!")
    sleep(2.0)

    ########################
    ##### END DATE LOGIC ###
    ########################

    time_clear_headerSTART(month_b=month_b, 
                           day_b=day_b, 
                           year_b=year_b)
    year_e = validate_date(year_range, year_end_msg)

    print(f'\n\tExcellent! {year_e} is a great year. Just like {year_b}!')

    time_clear_headerSTART(month_b=month_b, 
                           day_b=day_b, 
                           year_b=year_b)
    month_e = validate_date(month_range, month_msg)

    print("\n\tWe'll accept that")
    
    time_clear_header1()
    time_clear_headerSTART(month_b=month_b,
                           day_b=day_b,
                           year_b=year_b)

    date_range = set_date_range(month_e)
    day_e = validate_date(date_range, day_msg)

    print("\n\tLooks good to us.")
    time_clear_headerEND(month_b=month_b, day_b=day_b,
                         year_b=year_b, month_e=month_e,
                         day_e=day_e, year_e=year_e)
    
    input_prompt = '\n\t At last, what subreddit would you like to scrape? \n\n\t www.reddit.com\\r\\'
    designatedSubReddit = input(input_prompt)

    print(f'\n\t \t   Downloading images from /r/{designatedSubReddit}...')
    print("\n\n\t    ___________________________________________\n\n \t\t\t\t*** \n")
    sleep(2.0)

    ########################
    ##### INPUT PROCESSING #
    ########################

    # Y / M / D / H / Mi / S / ??
    # (2017, 3, 9, 23, 49, 20, 000000), timezone='GMT')

    bd_dt = Delorean(datetime=datetime(year_b, month_b,
                                       day_b, 0, 0, 0, 000000),
                                       timezone='GMT')
    bd_epoch = bd_dt.epoch
    ed_dt = Delorean(datetime=datetime(year_e, month_e, day_e,
                                       23, 59, 0, 000000),
                                       timezone='GMT')
    ed_epoch = ed_dt.epoch
    urls = urls_by_period(designatedSubReddit,
                          bd_epoch,
                          ed_epoch)

    total_downloaded = 0

    ########################
    ##### DOWNLOADING ######
    ########################

    for url_list in urls:
        try:
            url = url_list[0] # -- the actual url
            date_created = url_list[1] # -- the date the image was posted
            post_title_untamed = url_list[2] # -- post title without parsing
            post_title = sub(r'([^\s\w]|_)+', '', post_title_untamed) # -- post title with parsing

            def file_namer(splitter):
                file_name = f'{date_created} {post_title} {splitter}'
                
                return file_name

            def soup_parse(parse_string):
                soup = bs(get(url).text, parse_string)

                return soup

            def counter_namer(filename):
                if start != -1:
                    seconds = (datetime.now() - start).total_seconds()

                print(f'\t{filename} downloaded in {seconds} seconds.\n')

            # == DIRECT DOWNLOAD
            if url.endswith(config.extensions):
                filename = file_namer(url.split("/")[-1])
                start = download_file(url, date_created, filename, designatedSubReddit)
                
                print(f"\nDownloading from\n {post_title_untamed} \n")
                print(f'Downloading file: {filename}.')

                counter_namer(filename)
                total_downloaded += 1

            # ----- ADDED FEATURES

            # == REDDITBOORU
            elif url.startswith(('https://redditbooru.com/gallery/')):
                soup = soup_parse('lxml')
                gallery_links = soup.find_all('script')

                print(f"\nDownloading redditbooru gallery items from: {post_title_untamed}\n")

                for i in gallery_links:
                    cdn_url = findall('\"cdnUrl\":(\".*?\")', i.text)

                    if len(cdn_url) > 0:
                            redditbooru_list = [i.replace('"', '').replace("\\", '') for i in cdnURL]
                            
                            counter_namer()
                            total_downloaded += 1

                    for i in redditbooru_list:
                        filename = file_namer(i.split("/")[-1])
                        start = download_file(i, date_created, filename, designatedSubReddit)

                        counter_namer(filename)
                        total_downloaded += 1

            # == IMGUR GALLERIES
            elif url.startswith('https://imgur.com/a/'):
                slug = url.rsplit('/', 1)[-1]
                imgur_source = get(f'https://imgur.com/ajaxalbums/getimages/{slug}').text
                parse_for_images = findall("\"images\":\[.*\]", imgur_source)

                if not parse_for_images:
                    print("-"*60)
                    print("\nLooks like this image was removed! Let's move on...\n")
                    print("-"*60)
                    continue
                
                else:
                    convert_to_json = loads(parse_for_images[0][9:])
                    imgur_list = [f'https://i.imgur.com/{i["hash"]}{i["ext"]}' for i in convert_to_json]
                    
                    print(f"\nDownloading imgur gallery items from: {post_title_untamed}\n")

                    for i in imgur_list:
                        filename = file_namer(i.split("/")[-1])
                        start = download_file(i, date_created, filename, designatedSubReddit)

                        counter_namer(filename)
                        total_downloaded += 1
                
            # == PIXV
            elif url.startswith('https://pixv.net'):
                soup_parse('html.parser')
                pixv_image_containers = soup.find_all("div", {"class", "img-container"})
                pixv_imgaes = [i.a.img.get("src") for i in pixv_image_containers]
                print(f"\nDownloading pixv item(s) from: {post_title_untamed}\n")
                
                for i in imgur_list:
                    filename = file_namer(i.split("/")[-1])
                    start = download_file(i, date_created, filename, designatedSubReddit)

                    counter_namer(filename)
                    total_downloaded += 1
            
            # == INSTAGRAM
            elif url.startswith('https://www.instagram.com/p/'):
                source = get(url).text
                img_link = findall('display_url":(\".*?\")', source)[0][1:][:-1]
                
                print(f"\nDownloading an Instagram image from: {post_title_untamed}\n")
                filename = file_namer(img_link.split("/")[-1])
                start = download_file(i, date_created, filename, designatedSubReddit)

                counter_namer()
                total_downloaded += 1

            # == TUMBLR
            elif url.split('/')[2].split('.')[1] == 'tumblr':                    
                soup = soup_parse('lxml')
                gallery_links = soup.find_all("iframe", {"class" : "photoset"})

                for i in gallery_links:
                    request_link = i.get("src")
                    link = url.split('/')[2]
                    full_request_link = f'http://{link}{request_link}'                    
                    new_soup = bs(get(full_request_link).text, 'lxml')
                    tumblr_img_links = [i.get('src') for i in new_soup.find_all('img')]

                    for i in tumblr_img_links:
                        print(f"\nDownloading tumblr image(s) from: {post_title_untamed}\n")
                        filename = file_namer(i.split("/")[-1])
                        start = download_file(i, date_created, filename, designatedSubReddit)

                        counter_namer(filename)
                        total_downloaded += 1
            
            # == TWITTER
            elif url.startswith('https://twitter.com'):
                soup = soup_parse('lxml')
                twitter_img_tags = soup.find_all('img')

                for i in twitter_img_tags:
                    
                    try:
                        if img_source.startswith('https://pbs.twimg.com/media/'):
                            img_source = i.get('src')
                            print(f"\nDownloading a Twitter image from: {post_title_untamed}\n")
                            filename = file_namer(i[0].split("/")[-1])
                            start = download_file(i, date_created, filename, designatedSubReddit)

                            counter_namer(filename)
                            total_downloaded += 1

                    except AttributeError:
                        continue

        except OSError:

            print("-"*60)
            print("\nThat image causes an error! Let's move on...\n")
            print("-"*60)
            continue

    #Closing statements
    print("-"*60)
    print(f"\n You downloaded a total of {total_downloaded} images.\n")
    print("\n Thanks for using Reddit Image Scraper 1.0 -SPECIAL EDITION- \n")


if __name__ == '__main__':
        
        main()
