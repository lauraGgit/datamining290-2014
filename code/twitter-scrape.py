    #!/usr/bin/python
 
import json
import sys
import urllib2
import os
import tweepy
import csv, codecs, cStringIO

consumer_key = "rLzFKsgNyV9MWszRxPzFYg"
consumer_secret = "U1hIJ1uSGgzktjvEohXSgcfufP2E4YfEvqJ3XmHv1U"


# The access tokens can be found on your applications's Details
# page located at https://dev.twitter.com/apps (located under "Your access token")
access_token="256479408-A8ZQB9hp8nKGLDvc6jb60ttfwfpj7PytlRskJegW"
access_token_secret="nDijU9NBRB0uwa2vAVqHKgZlKpGm98IhYNPFb2h28hdbz"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


query = ['affordable care act'];

for qy in range(len(query)):

    numResults = 100
    drive = api.search(q=query[qy], count=numResults)
    
    #Callback Handling

        
    for result in drive:
        arr = []
        for val in result:
            arr.append(val)
            print arr

        #if type(result.geo) == dict:
        #   result.lat = result.geo["coordinates"][0]
        #    result.lon = result.geo["coordinates"][1]
        #else:
        #    result.lat = '0'
        #    result.lon = '0'
        #with open('dm.csv', 'a') as csvfile:
        #    tweetwrite = csv.writer(csvfile,delimiter=',', quoting = csv.QUOTE_MINIMAL)
        #    tweetwrite.writerow([result.id,result.created_at,result.lat,result.lon,result.source.encode("utf-8"),result.text.encode("ascii", "ignore"), qy, query[qy]])

