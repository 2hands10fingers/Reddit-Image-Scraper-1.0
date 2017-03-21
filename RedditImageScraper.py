import redditaccess
from requests import get
from delorean import Delorean
from datetime import datetime
import os, sys
import time
import asyncio
import aiohttp
import aiofiles
import argparse


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
MSG_END = '\t{} downloaded in {} seconds. Completed at {}.\n'


# Get submissions
def get_submissions(subreddit_name, start_date, end_date, verbose):

    reddit = redditaccess.bot_login()
    subreddit = reddit.subreddit(subreddit_name)

    dl_time = datetime.now()

    print("Retrieving submissions from {}. Started at {}".format(subreddit_name, time.strftime("%H:%M:%S")))
    submissions = subreddit.submissions(
            start=start_date, end=end_date)

    delta = (datetime.now() - dl_time).total_seconds()

    if verbose:
        print("Retrieval of submissions took {} seconds.  Completed at {}".format(
                                                        str(delta), time.strftime("%H:%M:%S")))

    # Returns a generator of submissions.
    return submissions

# Download image.  Function actually downloads every url and saves it onto disk.
# Does not discriminate on what to download.  Saves file with the "date_created"
# parameter and the url.
async def fetch_image(url, date_created, verbose):
    filename = date_created + str(url).split('/')[-1]

    # Shows what is being downloaded.
    if verbose:
        print(MSG_START.format(filename))

    # Opens url and a file using aiohttp and aiofiles.
    # Reads the content 1024 chunks at a time so that content is downloaded
    # and written to disk asynchronously. Normal file writing is I/O blocking.
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(url) as response:
            async with aiofiles.open(filename, mode ='wb') as file:
                dl_time = datetime.now()
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    await file.write(chunk)

    # Prints out how long each file took to download.
    # Timing times each co-routine with its own local variables, so there is no
    # mixing up of printing from other co-routines.
    delta = (datetime.now() - dl_time).total_seconds()
    if verbose:
        print(MSG_END.format(filename, str(delta), time.strftime("%H:%M:%S")))

    return


# Return list of image urls and dates from given submission.
def get_urls_and_dates(submissions):

    # List that we'll return at the end.
    urls_and_dates = []

    # Loop through the submissions here. TODO: Figure out a way to loop through the submissions faster.
    for submission in submissions:

        # Want to call this as least as possible since it is an API call I believe?
        url = submission.url

        # Only add jpgs, png, and jpegs to list.
        if url.endswith((".jpg", ".png", ".jpeg")):
            date_created = datetime.fromtimestamp(
                submission.created_utc).strftime('%Y%m%d_%H%M%S_')
            urls_and_dates.append([url, date_created])

    return urls_and_dates


# Can easily expand amount of args using the verbosity as a baseline example.
def get_args(args):
    parser = argparse.ArgumentParser(description="Finds all submissions between "
                                                 "given dates and downloads urls"
                                                 "that end in .jpg, jpeg, and png.")

    parser.add_argument('-v', '--verbose', action='store_true', help='Print verbose output.', default=False)

    # TODO: Probably add in a -h argument eventually.
    return parser.parse_args(args)

# Main function.  Get the submissions from the subreddit between the
# specified dates, and then run the parse function on each one.
async def main(args):

    # Get our args stored in parser.
    parser = get_args(args)

    # Our first arg! For now, just verbosity. Can easily expand.
    verbose = parser.verbose

    # Initializes the Reddit object and gets the subssions between given dates from it.
    submissions = get_submissions(designatedSubReddit, bd_epoch, ed_epoch, verbose)

    # Get our list of urls to go and download.
    img_urls = get_urls_and_dates(submissions)

    # Start throwing in the tasks for our loop to download.
    tasks = [
            asyncio.ensure_future(fetch_image(url, date_created, verbose))
            for url, date_created in img_urls
        ]

    # This will make the loop wait for all of the tasks above to finish before finishing main()
    await asyncio.wait(tasks)

if __name__ == "__main__":

    # Start the loop!!!
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(sys.argv[1:]))
