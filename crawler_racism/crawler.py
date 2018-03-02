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

arq = csv.writer(open("teste.csv","w", encoding='utf-8'))
#arqc = csv.writer(arq, delimiter="\t", quotechar='"')
arq2 = open("teste.json", "w", encoding='utf-8')
#query = (('http') and ('Black Friday OR BlackFriday OR #blackfriday OR #BLACKFRIDAY OR #blackweek OR black week OR black week'))
row=[]

statuses = tweepy.Cursor(api.search,q=('RT' and 'copa do mundo'), since='2017-11-30', until='2017-11-31',lang='pt', count=100).items()


while True:
	try:
		status = statuses.next()
		row=str(status.user.screen_name), str(status.created_at),str(status.text)
		arq.writerow(row)
        
		arq2.write(str(status))
		arq2.write("\n")


	except tweepy.TweepError:
		print("15 min...")
		time.sleep(60*15)
		continue

	except StopIteration:
		print("cabô")
		break

