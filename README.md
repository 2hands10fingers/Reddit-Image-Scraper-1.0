# Reddit Image Scraper 1.0 brought to you by <a href="http://www.pystudygroup.com/">pyStudyGroup</a>
<i>Credits: <a href="https://github.com/2hands10fingers">/u/2hands10fingers</a>, <a href="https://github.com/Anonimista">/u/Joe_Anonimist</a>, <a href="https://github.com/Belonias">/u/iakovosbelonias</a>, <a href="https://github.com/tjcim">iakov</a></i>

Scrapes Reddit images from any public subreddit by a user-specified date range and saves them to your computer.

# Introduction

Many tools scrape Reddit but don't give you the power to grab data on your terms. This changes things.

# How it Works

Use Python 3 to scrape any .jpg or .png images in the available subreddit (you can always add or remove file extensions within the code). Simply run the program in terminal using <code>$ python3 RedditImageScraper.py</code> under the correct directory where RedditImageScraper.py is downloaded, enter your start and ending dates, then you will select any public subreddit of your choice, and *PRESTO*! you will begin downloading images.

# Installation

<strong>1. Download</strong>

You can download this repository directly from GitHub and place the files where you want to run the program from. Remember, where the program is located, that is where your pictures will download to.

<strong>2. Delorean</strong>

Reddit Image Scraper 1.0 uses epochs to work all around the world at any time. You must also install the <strong>Delorean</strong> module. See available instructions <a href="http://delorean.readthedocs.io/en/latest/install.html">here</a>.

<strong>3. Obtaining Reddit Access</strong>

Oauth2 is required. Reddit doesn't like anonymous people taking their stuff, so you will need to copy the config.py.sample to config.py then open up the config.py file to add your own <i>username</i>, <i>password</i>, <i>client_id</i>, and <i>client_secret</i> to the file. Please follow Reddit's Oauth2 simple to follow guidelines to grab the <code>client_id</code> and <code>client_secret</code> <a href="https://github.com/reddit/reddit/wiki/OAuth2">here</a>.


# Notes

Download speeds may vary depending on the length of your selected date range, the Reddit server's current performance, or your current internet speed. You will only be able to select the years 2005 (when Reddit was launched) through the current year. If you want download all of the images for the current day, simply enter the date twice (e.g., 3-14-2017 -- 3-14-2017).

Thank you and enjoy,

2hands10fingers

<img src="https://upload.wikimedia.org/wikipedia/en/thumb/8/82/Reddit_logo_and_wordmark.svg/1280px-Reddit_logo_and_wordmark.svg.png"></img>
