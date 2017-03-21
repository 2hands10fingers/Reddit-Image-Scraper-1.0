import redditaccess
from requests import get
from delorean import Delorean
from datetime import datetime
import os
import time
import asyncio
import aiohttp
import aiofiles


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
    print("\t  .___________________________________________. \n \t / \t \t \t \t \t" + "       \\" + "" + "\n\t|    Welcome to the Reddit Image Scraper 1.0\t| \n \t| \t \tby pyStudyGroup \t \t" + "" + "|" + "\n\t +~____________________________________________~+ \n")

def time_clear_headerSTART():
    time.sleep(0.9)
    clear_screen()
    print("\t  .___________________________________________. \n \t / \t \t \t \t \t" + "       \\" + "" + "\n \t|    Welcome to the Reddit Image Scraper 1.0\t| \n \t| \t   DATE RANGE: "+ str(month_b) + "-" + str(day_b) + "-" + str(year_b)+ " -- " "\t \t" + "" + "|" + "\n\t +~____________________________________________~+ \n")

def time_clear_headerEND():
    time.sleep(0.9)
    clear_screen()
    print("\t  .___________________________________________. \n \t / \t \t \t \t \t" + "       \\" + "" + "\n \t|    Welcome to the Reddit Image Scraper 1.0\t| \n \t| \t DATE RANGE: "+ str(month_b) + "-" + str(day_b) + "-" + str(year_b)+ " -- " + str(month_e) + "-" + str(day_e) + "-" + str(year_e) + "\t" + "" + "|" + "\n\t +~____________________________________________~+ \n")

########################
### START DATE LOGIC ###
########################

time.sleep(0.2)
time_clear_header1()

year_b = int(input('\n\tEnter the year you would like to START your range: \n\t'))

while not year_b in range(2005, int(datetime.now().year +1)):
    print("\n\tWoops! Try entering a valid number. " + str(year_b) + " was not a valid number.")
    time.sleep(2)
    time_clear_header1()
    year_b = int(input('\n\tEnter the year you would like to START your range: \n\t'))

print ("\n\tExcellent! " + str(year_b) + " is a great year.")
time_clear_header1()

month_b = int(input('\n\tNow, how about a month: '))

while not month_b in range(1, 13):
    print("\n\n\tWoops! Try entering a valid number. " + str(month_b) + " was not a valid number.")
    time.sleep(2)
    time_clear_header1()
    month_b = int(input('\n\tNow, how about a month: '))

print ("\n\tWe'll accept that")
time_clear_header1()

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
while not day_b in date_range:
    print("\n\tWoops! Try entering a valid number. " + str(day_b) + " was not a valid number.")
    time.sleep(2)
    time_clear_header1()
    day_b = int(input('\n\tLastly, enter the day: '))

print ("\n\tLooks good to us.")
print("\n\n\tYou have selected a start date of: " + str(month_b) + "-" + str(day_b) + "-" + str(year_b)+ "\n\n\tIs this correct? We hope so!")
time.sleep(2.0)

########################
##### END DATE LOGIC ###
########################

time_clear_headerSTART()

year_e = int(input('\n\tEnter the year you would like to END your range: \n\t'))

while not year_e in range(2005, int(datetime.now().year +1)):
    print("\n\tWoops! \nWoops! Try entering a valid number. " + str(year_e) + " was not a valid number.")
    time.sleep(2)
    time_clear_header1()
    year_e = int(input('\n\tEnter the year you would like to END your range: \n\t'))

print ("\n\tExcellent! " + str(year_e) + " is a great year. Just like " + str(year_b) +"!")
time_clear_headerSTART()

month_e = int(input('\n\tNow, how about a month: '))

while not month_e in range(1, 13):
    print("\n\n\tWoops! Try entering a valid number. " + str(month_e) + " was not a valid number.")
    time.sleep(2)
    time_clear_header1()
    month_e = int(input('\n\tNow, how about a month: '))

print ("\n\tWe'll accept that")
time_clear_header1()
time_clear_headerSTART()
# copy/paste from above. Needs to be in a function.
if month_e in days_31:
    date_range = range(1, 31)
elif month_e in days_30:
    date_range = range(1, 30)
else:
    # February. I'll figure out leap years later.
    date_range = range(1, 28)

day_e = int(input('\n\tLastly, enter the day: '))

while not day_e in date_range:
    print("\n\tWoops! Try entering a valid number. " + str(day_e) + " was not a valid number.")
    time.sleep(2)
    time_clear_header1()
    day_e = int(input('\n\tLastly, enter the day: '))

print ("\n\tLooks good to us.")
time_clear_headerEND()

designatedSubReddit = input('\n\t At last, what subreddit would you like to scrape? \n\n\t www.reddit.com\\r\\')

print("\n\t \t   Downloading images from /r/" + str(designatedSubReddit) + "... \n\n\t    ___________________________________________\n\n \t\t\t\t*** \n")
time.sleep(2.0)
########################
##### INPUT PROCESSING #
########################

# Y / M / D / H / Mi / S / ??
# (2017, 3, 9, 23, 49, 20, 000000), timezone='GMT')

bd_dt = Delorean(datetime=datetime(year_b, month_b, day_b, 0, 0, 0, 000000),  timezone='GMT')
bd_epoch = bd_dt.epoch
print(bd_epoch)

ed_dt = Delorean(datetime=datetime(year_e, month_e, day_e, 23, 59, 0, 000000),  timezone='GMT')
ed_epoch = ed_dt.epoch
print(ed_epoch)

# Messages for the downlad_file() function
MSG_START = 'Downloading file: {}.'
MSG_END = '\t{} downloaded in {} seconds. Completed at {}.".\n'

# Get submissions
def get_submissions(subreddit_name, start_date, end_date):

    reddit = redditaccess.bot_login()
    subreddit = reddit.subreddit(subreddit_name)

    dl_time = datetime.now()

    print("Retrieving submissions")
    submissions = subreddit.submissions(
            start=start_date, end=end_date)

    delta = (datetime.now() - dl_time).total_seconds()

    print("Retrieval of submissions took {} seconds.  Completed at {}".format(
                                                        str(delta), time.strftime("%H:%M:%S")))

    # Returns a generator of submissions.
    return submissions

# Download image file.
# Currently only supports direct links to jpg/png
async def fetch_image(url, date_created, verbose=True):
    filename = date_created + str(url).split('/')[-1]

    if verbose:
        print(MSG_START.format(filename))

    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            async with aiofiles.open(filename, mode ='wb') as file:
                dl_time = datetime.now()
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    await file.write(chunk)

    delta = (datetime.now() - dl_time).total_seconds()
    if verbose:
        print(MSG_END.format(filename, str(delta), time.strftime("%H:%M:%S")))

    return


# Return date and url from submission.
def get_date_and_url(submission):
    url = submission.url
    date_created = datetime.fromtimestamp(
            submission.created_utc).strftime('%Y%m%d_%H%M%S_')
    return [url, date_created]


# Main function.  Get the submissions from the subreddit between the
# specified dates, and then run the parse function on each one.
async def main():

    submissions = get_submissions(designatedSubReddit, bd_epoch, ed_epoch)

    img_urls = [get_date_and_url(submission)
                for submission in submissions
                if submission.url.endswith((".jpg", ".png", ".jpeg"))
                ]

    tasks = [
        asyncio.ensure_future(fetch_image(url, date_created))
        for url, date_created in img_urls
    ]

    await asyncio.wait(tasks)

# Start loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


"""
# Returns a list of urls posted to the subreddit_name
# between start_date and end_date.
# The list is in the form:
# ((url, date_string), (url, date_string), (url, date_string) ...)
def urls_by_period(subreddit_name, start_date, end_date):

    reddit = redditaccess.bot_login()
    subreddit = reddit.subreddit(subreddit_name)

    dl_time = datetime.now()

    print("Retrieving submissions")
    submissions = subreddit.submissions(
            start=start_date, end=end_date)

    delta = (datetime.now() - dl_time).total_seconds()

    print("Retrieval of submissions took {} seconds".format(str(delta)))

    # ret_list is the list I will return
    ret_list = list()

    # for each url I add (url, datetime)
    # to ret_list. I first added this
    # for testing purposes.
    # but I think it can be used to prepend
    # file names with creation dates
    # so the downloaded files could be
    # easier organized later.
    start_sub_time = datetime.now()

    for submission in submissions:
        date_created = datetime.fromtimestamp(
              submission.created_utc).strftime('%Y%m%d_%H%M%S_')
        print(submission.url)
        ret_list.append(submission.url)

    total_sub_time = (datetime.now() - start_sub_time).total_seconds()
    print("Total submission storage of {} submissions took {} seconds".format(len(ret_list), total_sub_time))



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
"""