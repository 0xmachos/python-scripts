#!/usr/bin/env python2
# python-scripts/tweet-followers.py

# tweet-followers.py

## Imports
import sys
import tweepy
import json
import re
from collections import Counter

def main():
    args = sys.argv[1:]

    if len(args) == 0:
    	print "./tweet-followers.py @handle target_name"
    	exit(1)

    username = sys.argv[1]
    target = sys.argv[2]

    auth = tweepy.OAuthHandler(
        'consumer_key', 'consumer_secret')
    auth.set_access_token('access_key',
                          'access_secret_key')

    api=tweepy.API(auth)
    tweepy.Cursor(api.followers, id=username)

    for user_obj in tweepy.Cursor(api.followers).pages():
        # print user._json['name']
        for x in user_obj:
            name = x._json['name'].encode('utf-8')
            screen_name = x._json['screen_name'].encode('utf-8')
            if re.findall(target, name) or re.findall(target, screen_name):
                print ("MATCH!")
                print("{} : @{}").format(name, screen_name)


    exit(0)

if __name__== "__main__":
    main()
