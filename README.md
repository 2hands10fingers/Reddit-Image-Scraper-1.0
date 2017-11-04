# Reddit Image Scraper 1.0 brought to you by <a href="http://www.pystudygroup.com/">pyStudyGroup</a>
<i>Credits: <a href="https://github.com/2hands10fingers">/u/2hands10fingers</a>, <a href="https://github.com/Anonimista">/u/Joe_Anonimist</a>, <a href="https://github.com/Belonias">/u/iakovosbelonias</a>, <a href="https://github.com/tjcim">tjcim</a></i>

Scrapes Reddit images from any public subreddit by a user-specified date range and saves them to your computer.

<img src="https://i.imgur.com/e2mgH7D.png"></img>
____

# Introduction

Many tools scrape Reddit but don't give you the power to grab data on your terms. This changes things.

# How it Works

Use Python 3 to scrape any .jpg or .png images in the available subreddit (you can always add or remove file extensions within the code). Simply run the program in terminal using <code>$ python3 RedditImageScraper.py</code> under the correct directory where RedditImageScraper.py is downloaded, enter your start and ending dates, then you will select any public subreddit of your choice, and *PRESTO*! you will begin downloading images.

# Installation

<strong>1. Download</strong>

You can download this repository directly from GitHub and place the files where you want to run the program from. Remember, where the program is located, that is where your pictures will download to. You can change `file_path` in config.py to direct all downloads to that directory.

<strong>2. Install Dependencies</strong>

We make sure things are easy to install and test by using the requirements.txt file. In your terminal, type <code> $ pip install -r requirements.txt</code> and you should have everything you need to get going. 

<strong>3. Obtaining Reddit Access</strong>

Oauth2 is required. Reddit doesn't like anonymous people taking their stuff, so you will need to copy the config.py.sample to config.py then open up the config.py file to add your own <i>username</i>, <i>password</i>, <i>client_id</i>, and <i>client_secret</i> to the file. Please follow Reddit's Oauth2 simple to follow guidelines to grab the <code>client_id</code> and <code>client_secret</code> <a href="https://github.com/reddit/reddit/wiki/OAuth2">here</a>.


# Testing

RIS now comes with testing abilities and error logging. We recommend doing this within python3's virtual environement.

### Setupping up the virtual testing environment:
<code>

$ python3 -m venv env

$ source env/bin/activate

$ pip install -r requirements.txt

$ pytest

</code>

# Notes

Download speeds may vary depending on the length of your selected date range, the Reddit server's current performance, or your current internet speed. You will only be able to select the years 2005 (when Reddit was launched) through the current year. If you want to download all of the images for the current day, simply enter the date twice (e.g., 3-14-2017 -- 3-14-2017).

Thank you and enjoy,

2hands10fingers

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Reddit_logo_and_wordmark.svg/1280px-Reddit_logo_and_wordmark.svg.png"></img>
