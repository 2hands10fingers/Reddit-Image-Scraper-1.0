""" Download images from Reddit during the submitted time periods. """
import os
import time
import argparse
from datetime import date
from datetime import datetime

from requests import get
from delorean import Delorean

import redditaccess

#########################
# ## FUNCTION JUNCTION ###
#########################


def clear_screen():
    # Check for OS. 'nt' = windows.
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def graphic(text):
    left_padding = (47 - len(text)) // 2
    right_padding = (47 - len(text)) // 2
    # fix it when the numerator is odd
    if left_padding + len(text) + right_padding < 47:
        right_padding += 1
    time.sleep(0.9)
    clear_screen()
    first_line = "{}.{}.\n".format(" " * 10, "_" * 43)
    second_line = "{}/{}\\\n".format(" " * 9, " " * 45)
    middle_lines = "{}|{}{}{}|\n"
    third_line = middle_lines.format(" " * 8, " " * 4,
                                     "Welcome to the Reddit Image Scraper 1.0", " " * 4)
    fourth_line = middle_lines.format(" " * 8, " " * left_padding, text, " " * right_padding)
    fifth_line = "{}+~{}~+\n".format(" " * 9, "_" * 43)
    print(first_line + second_line + third_line + fourth_line + fifth_line)


# Returns a list of urls posted to the subreddit_name
# between start_date and end_date.
# The list is in the form:
# ((url, date_string), (url, date_string), (url, date_string) ...)
def urls_by_period(subreddit_name, start_date, end_date):

    reddit = redditaccess.bot_login()
    subreddit = reddit.subreddit(subreddit_name)

    submissions = subreddit.submissions(
        start=start_date, end=end_date)

    # ret_list is the list I will return
    ret_list = list()

    # for each url I add (url, datetime)
    # to ret_list. I first added this
    # for testing purposes.
    # but I think it can be used to prepend
    # file names with creation dates
    # so the downloaded files could be
    # easier organized later.
    for submission in submissions:
        file_list = list()
        file_list.append(submission.url)
        date_created = datetime.fromtimestamp(
            submission.created_utc).strftime('%Y%m%d_%H%M%S_')
        file_list.append(date_created)
        ret_list.append(file_list)

    return ret_list


# Download the file for a given url.
# Prepend the post creation date to the file name.
# The file is saved in the same directory
# this script is in.
# If verbose is True the script prints:
# The name of the file being downloaded
# The file download time.
def download_file(output_dir, MSG_START, MSG_END, url, date_created, verbose=False):

    filename = date_created + str(url).split('/')[-1]
    file_path = os.path.join(output_dir, filename)

    if verbose:
        print(MSG_START.format(filename))

# TODO: move the download out of the with open. It should be run first, and if successful the file is written.

    with open(file_path, "wb") as fh:  # file has a special meaning and should not be used as a variable

        dl_time = datetime.now()

        response = get(str(url))
        fh.write(response.content)

        delta = (datetime.now() - dl_time).total_seconds()

        if verbose:
            print(MSG_END.format(filename, str(delta)))

        dl_time = datetime.now()


def main(args):

    ########################
    # ## START DATE LOGIC ###
    ########################

    time.sleep(0.2)
    graphic("by pyStudyGroup")

    year_b = int(input('\n\tEnter the year you would like to START your range: \n\t'))

    while year_b not in range(2005, int(datetime.now().year + 1)):
        print("\n\tWoops! Try entering a valid number. " + str(year_b) + " was not a valid number.")
        time.sleep(2)
        graphic("by pyStudyGroup")
        year_b = int(input('\n\tEnter the year you would like to START your range: \n\t'))

    print("\n\tExcellent! " + str(year_b) + " is a great year.")
    graphic("by pyStudyGroup")

    month_b = int(input('\n\tNow, how about a month: '))

    while month_b not in range(1, 13):
        print("\n\n\tWoops! Try entering a valid number. " +
              str(month_b) + " was not a valid number.")
        time.sleep(2)
        graphic("by pyStudyGroup")
        month_b = int(input('\n\tNow, how about a month: '))

    print("\n\tWe'll accept that")
    graphic("by pyStudyGroup")

    # I'll refactor this part in a function once we get it working.
    days_31 = [1, 3, 5, 7, 8, 10, 12]
    days_30 = [4, 6, 9, 11]

    if month_b in days_31:
        date_range = range(1, 32)
    elif month_b in days_30:
        date_range = range(1, 31)
    else:
        # February. I'll figure out leap years later.
        date_range = range(1, 29)

    day_b = int(input('\n\tLastly, enter the day: '))
    while day_b not in date_range:
        print("\n\tWoops! Try entering a valid number. " + str(day_b) + " was not a valid number.")
        time.sleep(2)
        graphic("by pyStudyGroup")
        day_b = int(input('\n\tLastly, enter the day: '))

    print("\n\tLooks good to us.")
    print("\n\n\tYou have selected a start date of: " + str(month_b) + "-" +
          str(day_b) + "-" + str(year_b) + "\n\n\tIs this correct? We hope so!")
    time.sleep(2.0)

    begin_date = date(year_b, month_b, day_b)
    begin_text = "DATE START: {}".format(begin_date.strftime("%m-%d-%Y"))
    graphic(begin_text)

    ########################
    # #### END DATE LOGIC ###
    ########################

    year_e = int(input('\n\tEnter the year you would like to END your range: \n\t'))

    while year_e not in range(2005, int(datetime.now().year + 1)):
        print("\n\tWoops! \nWoops! Try entering a valid number. " + str(year_e) + " was not a valid number.")
        time.sleep(2)
        graphic(begin_text)
        year_e = int(input('\n\tEnter the year you would like to END your range: \n\t'))

    print("\n\tExcellent! " + str(year_e) + " is a great year. Just like " + str(year_b) + "!")
    graphic(begin_text)

    month_e = int(input('\n\tNow, how about a month: '))

    while month_e not in range(1, 13):
        print("\n\n\tWoops! Try entering a valid number. " + str(month_e) + " was not a valid number.")
        time.sleep(2)
        graphic(begin_text)
        month_e = int(input('\n\tNow, how about a month: '))

    print("\n\tWe'll accept that")
    graphic(begin_text)

    # copy/paste from above. Needs to be in a function.
    if month_e in days_31:
        date_range = range(1, 31)
    elif month_e in days_30:
        date_range = range(1, 30)
    else:
        # February. I'll figure out leap years later.
        date_range = range(1, 28)

    day_e = int(input('\n\tLastly, enter the day: '))

    while day_e not in date_range:
        print("\n\tWoops! Try entering a valid number. " + str(day_e) + " was not a valid number.")
        time.sleep(2)
        graphic(begin_text)
        day_e = int(input('\n\tLastly, enter the day: '))

    print("\n\tLooks good to us.")

    end_date = date(year_e, month_e, day_e)
    end_text = "DATE RANGE: {} - {}".format(begin_date.strftime("%m-%d-%Y"), end_date.strftime("%m-%d-%Y"))
    graphic(end_text)

    designatedSubReddit = input('\n\t At last, what subreddit would you like to scrape? \n\n\t www.reddit.com\\r\\')

    print("\n\t \t   Downloading images from /r/" + str(designatedSubReddit) + "... \n\n\t    ___________________________________________\n\n \t\t\t\t*** \n")
    time.sleep(2.0)
    ########################
    # #### INPUT PROCESSING #
    ########################

    # Y / M / D / H / Mi / S / ??
    # (2017, 3, 9, 23, 49, 20, 000000), timezone='GMT')

    bd_dt = Delorean(datetime=datetime(year_b, month_b, day_b, 0, 0, 0, 000000), timezone='GMT')
    bd_epoch = bd_dt.epoch
    print(bd_epoch)

    ed_dt = Delorean(datetime=datetime(year_e, month_e, day_e, 23, 59, 0, 000000), timezone='GMT')
    ed_epoch = ed_dt.epoch
    print(ed_epoch)

    # Messages for the downlad_file() function
    MSG_START = 'Downloading file: {}.'
    MSG_END = '\t{} downloaded in {} seconds.\n'

    urls = urls_by_period(
        designatedSubReddit,
        bd_epoch,
        ed_epoch)

    # You don't need to convert the urls list
    # because it is already a list. Sorry guys!
    # url[0] is the actual url
    # url[1] is the date the image was posted
    for url_list in urls:
        url = url_list[0]
        date_created = url_list[1]
        if url.endswith(('.jpg', '.png')):
            download_file(args.output_dir, MSG_START, MSG_END, url, date_created, verbose=True)
    print("\n Thanks for using Reddit Image Scraper 1.0 \n")


def parse_args(args):
    parser = argparse.ArgumentParser(
        description='Download images from a subreddit during certain dates')
    parser.add_argument('output_dir', help='Full path to directory where images should be saved.')
    args = parser.parse_args(args)
    if not os.path.isdir(args.output_dir):
        print("The directory provided does not exist, create it first and then rerun the program.")
        raise SystemExit
    return args


if __name__ == '__main__':
    import sys
    main(parse_args(sys.argv[1:]))
