#messing with twitter

import tweepy
import time
import sys
import re
import os
#tweets = str(sys.argv[1]) + ".txt"

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'De0FSHQ3aMShBeePwHqjESwVn'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'fQboQLJX58Sx3h9QLiw6mPPl7ORwUKA6tAlqnHj3oU6YkCeIRh'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '917211703196123142-8E760BtYeEyw4lrl4uxm7pncGK9JA7y'#keep the quotes, replace this with your access token
ACCESS_SECRET = 'BTxNi53jpZeW68M2v8aKTB7qhzedltvVT3MUQdJgVSSM6'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

start = time.time()
END_TIME = 500

#remove new lines
#remove [' <-- at the beginning and --> '] at the end
tweetfile = open("masterpeace_tweets.txt", 'r')
tweets = tweetfile.readlines()

if not os.path.isfile("tweet_replied.txt"):
	tweet_replied = []
else:
	with open("tweet_replied.txt", "r") as f:
		tweet_replied = f.read()
		tweet_replied = tweet_replied.split("\n")
		tweet_replied = list(filter(None, tweet_replied))

def cleantweet(dirty_tweet):
    lentweet = len(dirty_tweet)
    if "['" in dirty_tweet[0:2]:
        almost_clean = dirty_tweet[2:]
    else:
        almost_clean = dirty_tweet
        pass


    if "']" in almost_clean[lentweet-1:]:
        clean_tweet = almost_clean[:lentweet-2]
    else:
        clean_tweet = almost_clean
        pass

    return clean_tweet

sendbeatsbot = api.get_user('metaphorminute')
#print(sendbeatsbot.followers())

#make initial request for most recent tweets (200 is the maximum allowed count)
#new_tweets = api.user_timeline(screen_name = screen_name,count=200)

done = False
while not done:
    new_tweet = api.user_timeline(screen_name = 'SendBeatsBot',count=1)[0]
    #new_tweets = api.user_timeline(screen_name = 'hopepotamus23',count=1)
    #print((new_tweet.retweeted_status.id)) #THIS IS THE ID OF THE RETWEETED STATUS
    #print((new_tweet.retweeted_status.author.screen_name))

    if str(new_tweet.id) in tweet_replied:
        print("no new tweets")
        print("no new tweets \n")
        time.sleep(5)


    else:
        print("*****new tweet*****")
        print("tweet id: " + str(new_tweet.retweeted_status.id))
        print("tweet author: " + str(new_tweet.retweeted_status.author.screen_name))
        print("tweet text: " + str(new_tweet.text))

        tweet_replied.append(str(new_tweet.id))
        api.update_status(status = "@" + new_tweet.retweeted_status.author.screen_name + " hey here's some of my beats!" + "https://soundcloud.com/masterpeacerecords/tracks", in_reply_to_status_id = str(new_tweet.retweeted_status.id))
        print("replied!")
        print("continuing loop \n")

        with open("tweet_replied.txt", "a") as f:
            f.write(str(new_tweet.id) + "\n")

    if time.time() > start + END_TIME: #try to understand this!
        print("**************PROGRAM DONE*************")
        done = True
        break
