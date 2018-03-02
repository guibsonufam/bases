import tweepy
import csv
import time
import os
import json
import sys

# -*- encoding: utf-8 -*-
consumer_key="8OKW5ik3n8DqT4npsBMQ5zZQI"
consumer_secret="RxysoCbyEhzLWyyPmgVgFjmiEJw4fvUo2pd0i2fmfQYKpgTpQj"
acess_token="191712148-a8fuYrl7R7TDlYGunaOArmD2qF0GvAxGiINV2lbc"
acess_token_secret="AVr5CSGBXfoCpTiSmgYAjInqd1a9PYvHm7p9k9aHCYpoS"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_token_secret)

api=tweepy.API(auth)

#user = api.get_user("thomassantanas");

#rel = api.lookup_friendships(screen_names="QUEBRADINHAJN")

#for x in rel:
#if(isinstance(rel, tweepy.models.Relationship)):
#    print (rel)

b = api.show_friendship(source_id='2606779704', target_id='751429122073690112')

print (b)
print(b[0].following, b[1].following)
#print (api.show_friendship(source_screen_name='thomassantanas', target_screen_name='ManuSoar')[1].following)
