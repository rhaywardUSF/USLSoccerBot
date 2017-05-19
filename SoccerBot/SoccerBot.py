# SoccerBot 
# This program automates user flair assignment. A bot user is set up and reads incoming mailbox messages. 
# The bot user receives a flair request, and assigns said flair to the user.
# If the subreddit has the matching flair image and flair code, the user will see the team crest appear next to their name.
# Ultimately, this bot will assign flair, update sidebar scores, and update news banners at the top of the subreddit
# Written by Randy Hayward
# RandyHayward.com

import praw
import sys
import os
import time
import logging
import sqlite3
sys.path.append(os.path.dirname(__file__) + "/Helpers")
import AuthHelper
from PrintHelper import tPrint
sys.path.append(os.path.dirname(__file__) + "/Functionality")
sys.path.append(os.path.dirname(__file__) + "/DB")
import CheckAndAssignFlair



loggerMain = logging.getLogger("SoccerBot_Main")
loggerMain.info("Program Start")
r = None
currentSubreddit = None
conn = None
c = None
location = 'data.sqlite3'
r = AuthHelper.login("Config/Auth.ini")

while True:
    tPrint("Enter Loop")
    subredditsIModerate = r.get_my_moderation()
    CheckAndAssignFlair.run(r)
    time.sleep(5)

