import RIScraper
from requests import get
from delorean import Delorean
from datetime import datetime
import pytz

####### PICK YOUR SUBREDDIT #####

designatedSubReddit = 'wallpapers'

####### BEGINNING DATE HERE #####

year_b = 2017
month_b = 3
day_b = 7
hour_b = 0
minute_b = 0
second_b = 0

####### ENDING DATE HERE #####

year_e = 2017
month_e = 3
day_e = 7
hour_e = 23
minute_e = 59
second_e = 59

# Y / M / D / H / Mi / S / ??
# (2017, 3, 9, 23, 49, 20, 000000), timezone='GMT')

bd_dt = Delorean(datetime=datetime(year_b, month_b, day_b, hour_b, minute_b, second_b, 000000),  timezone='GMT')
bd_epoch = bd_dt.epoch
print(bd_epoch)

ed_dt = Delorean(datetime=datetime(year_e, month_e, day_e, hour_e, minute_e, second_e, 000000),  timezone='GMT')
ed_epoch = ed_dt.epoch
print(ed_epoch)

# Messages for the downlad_file() function
MSG_START = 'Downloading file: {}.'
MSG_END = '\t{} downloaded in {} seconds.\n'

# Returns a list of urls posted to the subreddit_name
# between start_date and end_date.
# The list is in the form:
# ((url, date_string), (url, date_string), (url, date_string) ...)
def urls_by_period(subreddit_name, start_date, end_date):

    reddit = RIScraper.bot_login()
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
def download_file(url, date_created, verbose=False):

    filename = date_created + str(url).split('/')[-1]

    if verbose:
        print(MSG_START.format(filename))

    with open(filename, "wb") as file:

        dl_time = datetime.now()

        response = get(str(url))
        file.write(response.content)

        delta = (datetime.now() - dl_time).total_seconds()

        if verbose:
            print(MSG_END.format(filename, str(delta)))

        dl_time = datetime.now()

def main():

    urls = urls_by_period(
            designatedSubReddit,
            bd_epoch,
            ed_epoch)

    # You don't need to convert the urls list
    #because it is already a list. Sorry guys!
    # url[0] is the actual url
    # url[1] is the date the image was posted
    for url_list in urls:
        url = url_list[0]
        date_created = url_list[1]
        if url.endswith(('.jpg', '.png')):
            download_file(url, date_created, verbose=True)


if __name__ == '__main__':
    main()
