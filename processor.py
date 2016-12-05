# -*- coding: utf-8 -*-


import re
import csv
from nltk.stem.porter import *
from url_classifier import getURLType

################test data###################



docs = []
allContent = []
allCodes = []

# open the coded tweets csv file
with open('change-500.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        # arrange file content in the tuple, push to documents array
        allContent.append(row[2])
        allCodes.append(row[6])

docs = list(zip(allContent, allCodes))


################test data###################

testData = allContent[:50]


def countHashtag(tweet):
    hashTagCounter = 0
    for word in tweet.split():
        if word.startswith("#"):
            hashTagCounter += 1
    return hashTagCounter

def countAtUser(tweet):
    atUserCounter = 0
    for word in tweet.split():
        if word.startswith("@"):
            atUserCounter += 1
    return atUserCounter

def countEmoji(tweet):
    emojis = re.findall(u'[\U0001f600-\U0001f650]', tweet.decode("utf-16"))

    return emojis

def ifStartWithHashtag(tweet):
    return tweet[0] == "#"


def ifEndWithHashtag(tweet):
    return tweet.split()[-1][0] == "#"


def replaceAtUser(tweet):
    tweet = re.sub(r'[@]\S*', '@user', tweet)

    return tweet

def removeHashtag(tweet):
    tweet = re.sub(r'[#]', '', tweet)

    return tweet

def cleanUrl(tweet):
    tweet = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', 'URL', tweet)

    return tweet

def replaceUrl(tweet):
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', tweet)
    for url in urls:
        tweet = tweet.replace(url, getURLType(url))
    return tweet

def processData(allTweets):

    featureSet = []
    cleanTweets = []

    for i, tweet in enumerate(allTweets):

        features = ''

        # if ifStartWithHashtag(tweet):
        #     features += " fstarthashtag"
        # if ifEndWithHashtag(tweet):
        #     features += " fendhashtag"
        #
        # counter = countHashtag(tweet)
        # if counter == 0:
        #     features += " f0hashtag"
        #
        # elif counter > 0 and counter <= 3:
        #     features += " f03hashtag"
        #
        # elif counter > 3 and counter <= 5:
        #     features += " f35hashtag"
        #
        # elif counter > 5 and counter <= 7:
        #     features += " f57hashtag"
        #
        # elif counter > 7:
        #     features += " f8hashtag"

        # featureSet.append(features)
        #
        # # tweet = replaceUrl(tweet)
        # #
        # tweet = replaceAtUser(tweet)
        # #
        tweet = removeHashtag(tweet)
        # #
        # tweet = tweet.lower()
        # #
        # stemmer = PorterStemmer()
        #
        # tweet = tweet.decode("utf8")
        #
        # tweetStems = [stemmer.stem(word) for word in tweet.split()]
        #
        # tweet = " ".join(tweetStems)

        # tweet += features



        tweet = cleanUrl(tweet)

        print countEmoji(tweet)

        cleanTweets.append(tweet)

        print "finished"
        print i

    return cleanTweets

print testData[38]