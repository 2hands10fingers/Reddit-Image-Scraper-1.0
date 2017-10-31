import os
import config
import redditaccess
import requests
from delorean import Delorean
from datetime import datetime
import time


#########################
### FUNCTION JUNCTION ###
#########################

def clear_screen():
    # Check for OS. 'nt' = windows.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def time_clear_header1():
    time.sleep(0.9)
    clear_screen()
    print(
        "\t  .___________________________________________. \n \t / \t \t \t \t \t" + "       \\" + "" +
        "\n\t|    Welcome to the Reddit Image Scraper 1.0\t| \n \t| \t \tby pyStudyGroup \t \t" + "" + "|" +
        "\n\t +~____________________________________________~+ \n")


def time_clear_headerSTART(month_b, day_b, year_b):
    time.sleep(0.9)
    clear_screen()
    print(
        "\t  .___________________________________________. \n \t / \t \t \t \t \t" + "       \\" + "" +
        "\n \t|    Welcome to the Reddit Image Scraper 1.0\t| \n \t| \t   DATE RANGE: " + str(
            month_b) + "-" + str(day_b) + "-" + str(
            year_b) + " -- " "\t \t" + "" + "|" + "\n\t +~____________________________________________~+ \n")


def time_clear_headerEND(month_b, day_b, year_b, month_e, day_e, year_e):
    time.sleep(0.9)
    clear_screen()
    print(
        "\t  .____________________________________________. \n \t / \t \t \t \t \t" + "       \\" + "" +
        "\n \t|    Welcome to the Reddit Image Scraper 1.0\t| \n \t| \t DATE RANGE: " + str(
            month_b) + "-" + str(day_b) + "-" + str(year_b) + " -- " + str(month_e) + "-" + str(day_e) + "-" + str(
            year_e) + "\t" + "" + "|" + "\n\t +~____________________________________________~+ \n")


def sleeper(num):
    time.sleep(num)


########################
###   VALIDATORS     ###
########################

def validate_date(valid_range, message):
    selected_date = int(input(message))

    while not valid(selected_date, valid_range):
        print("\n\tWoops! Try entering a valid number. " +
              str(selected_date) + " was not a valid number.")
        sleeper(2)
        time_clear_header1()

    return selected_date


########################
### HELPER FUNCTIONS ###
########################

# --------------------------------------------------

def set_date_range(month):
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    if month in days_31:

        valid_range = range(1, 32)

    elif month in days_30:

        valid_range = range(1, 31)

    else:

        valid_range = range(1, 29)  # February. I'll figure out leap years later.

    return valid_range


def valid(selected_date, valid_range):
    return selected_date in valid_range


# --------------------------------------------------

# Returns a list of urls posted to the subreddit_name
# between start_date and end_date.
# The list is in the form:
# ((url, date_string), (url, date_string), (url, date_string) ...)

def urls_by_period(subreddit_name, start_date, end_date):
    reddit = redditaccess.bot_login()
    subreddit = reddit.subreddit(subreddit_name)
    submissions = subreddit.submissions(start=start_date, end=end_date)
    ret_list = list()  # ret_list is the list I will return

    # For each url I add (url, datetime)
    # to ret_list. I first added this
    # for testing purposes.
    # but I think it can be used to prepend
    # file names with creation dates
    # so the downloaded files could be
    # easier organized later.

    for submission in submissions:
        file_list = list()
        date_created = datetime.utcfromtimestamp(submission.created_utc).strftime('%Y%m%d_%H%M%S_')

        file_list.append(submission.url)
        file_list.append(date_created)
        ret_list.append(file_list)

    return ret_list


# --------------------------------------------------

# Download the file for a given url.
# The file is saved in the same directory
# this script is in.
# Returns the download starting time
# If the request fails, it returns -1

def download_file(url, date_created, filename, subreddit):

    folder = os.path.join(config.file_path, subreddit)

    if not os.path.exists(folder):
        os.makedirs(folder)

    path = os.path.join(folder, filename)

    with open(path, 'wb') as f:
        start = datetime.now()
        response = requests.get(url)

        if not response.status_code == 200:
            return -1

        f.write(response.content)
    return start


# --------------------------------------------------

def main():
    ########################
    ###     CONSTANTS    ###
    ########################

    # Messages for the downlad_file() function
    MSG_START = 'Downloading file: {}.'
    MSG_END = '\t{} downloaded in {} seconds.\n'

    # Values
    year_range = range(2005, int(datetime.now().year) + 1)
    month_range = range(1, 13)

    # Messages
    year_start_msg = '\n\tEnter the year you would like to START your range: \n\t'
    year_end_msg = '\n\tEnter the year you would like to END your range: \n\t'
    month_msg = '\n\tNow, how about a month: '
    day_msg = '\n\tLastly, enter the day: '

    ########################
    ### START DATE LOGIC ###
    ########################

    sleeper(0.2)
    time_clear_header1()

    year_b = validate_date(year_range, year_start_msg)

    print("\n\tExcellent! " + str(year_b) + " is a great year.")
    time_clear_header1()

    month_b = validate_date(month_range, month_msg)

    print("\n\tWe'll accept that")
    time_clear_header1()

    date_range = set_date_range(month_b)
    day_b = validate_date(date_range, day_msg)

    print("\n\tLooks good to us.")
    print("\n\n\tYou have selected a start date of: " + str(month_b) + "-"
          + str(day_b) + "-" + str(year_b) + "\n\n\tIs this correct? We hope so!")
    sleeper(2.0)

    ########################
    ##### END DATE LOGIC ###
    ########################

    time_clear_headerSTART(month_b=month_b, day_b=day_b, year_b=year_b)

    year_e = validate_date(year_range, year_end_msg)

    print("\n\tExcellent! " + str(year_e) + " is a great year. Just like " + str(year_b) + "!")
    time_clear_headerSTART(month_b=month_b, day_b=day_b, year_b=year_b)

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
    designatedSubReddit = input('\n\t At last, what subreddit would you like to scrape? \n\n\t www.reddit.com\\r\\')

    print("\n\t \t   Downloading images from /r/" + str(designatedSubReddit) +
          "... \n\n\t    ___________________________________________\n\n \t\t\t\t*** \n")
    sleeper(2.0)

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

    # url[0] is the actual url
    # url[1] is the date the image was posted

    total_downloaded = 0

    for url_list in urls:

        url = url_list[0]
        date_created = url_list[1]

        if url.endswith(('.jpg', '.png')):

            # Prepend the post creation date to the file name.
            filename = date_created + str(url).split('/')[-1]

            print(MSG_START.format(filename))

            start = download_file(url,
                                  date_created, filename, designatedSubReddit)

            if start != -1:
                print(MSG_END.format(filename, str((datetime.now() - start).total_seconds())))

            total_downloaded += 1

    # Closting statements
    print("---------------------------------------------")
    print("\n You downloaded a total of {} images.\n".format(total_downloaded))
    print("\n Thanks for using Reddit Image Scraper 1.0 \n")


if __name__ == '__main__':
    main()
