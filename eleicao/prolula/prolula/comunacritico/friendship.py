import tweepy
import csv
import time
import os
import simplejson
import sys

# -*- encoding: utf-8 -*-
consumer_key="8OKW5ik3n8DqT4npsBMQ5zZQI"
consumer_secret="RxysoCbyEhzLWyyPmgVgFjmiEJw4fvUo2pd0i2fmfQYKpgTpQj"
acess_token="191712148-a8fuYrl7R7TDlYGunaOArmD2qF0GvAxGiINV2lbc"
acess_token_secret="AVr5CSGBXfoCpTiSmgYAjInqd1a9PYvHm7p9k9aHCYpoS"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_token_secret)

api=tweepy.API(auth)

#arq = open("json.txt", "w")
#arq3 = open("nao_seguem.txt", "w")
#arq = open('ids.txt', 'r')
#texto = arq.readlines()
#source='3432'
#try:
b = api.show_friendship(source_id='1722802370', target_id='796180188946112512')
    
print (str(b))
#ids = []
#for page in tweepy.Cursor(api.friends, user_id="191712148").pages():
#    ids.extend(page)
#    time.sleep(1)
    #print(page.id_str)
    #print(page.screen_name)
#    print (page)
#    arq.write(str(page)+'\n')
#users_list = api.lookup_friendships(user_ids=['191712148'])
#users_list = api.lookup_users(user_ids=['191712148'])
#print (users_list)
#for user in users_list:
#   print (user.screen_name)
