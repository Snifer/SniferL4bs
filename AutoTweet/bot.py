#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, datetime, random

CONSUMER_KEY = "YOUR KEY HERE"
CONSUMER_SECRET="CONSUMER KEY HERE"
ACCESS_KEY="ACCESS KEY HERE"
ACCESS_SECRET="ACCESS SECRET KEY HERE"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename=open('lines.txt','r')#lines.txt file read for tweet
first_line=filename.readlines()
filename.close()

for line in first_line:
     api.update_status(status=line)
     print line
     lines = open('lines.txt').readlines()
     open('lines.txt', 'w').writelines(lines[1:])
     number_random = random.randint(200, 1000)#
     timeTweet = number_random / 60
     print timeTweet
     time.sleep(number_random) 