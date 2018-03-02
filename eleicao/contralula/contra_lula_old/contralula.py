import codecs
import time
import sys
from importlib import reload
import tweepy
import csv
import simplejson as json

#reload(sys)
#sys.setdefaultencoding("utf-8")

consumer_key="8OKW5ik3n8DqT4npsBMQ5zZQI"
consumer_secret="RxysoCbyEhzLWyyPmgVgFjmiEJw4fvUo2pd0i2fmfQYKpgTpQj"
access_token="191712148-a8fuYrl7R7TDlYGunaOArmD2qF0GvAxGiINV2lbc"
access_token_secret="AVr5CSGBXfoCpTiSmgYAjInqd1a9PYvHm7p9k9aHCYpoS"

# consumer_key = "Ncg99iYY0Z7ZNER2zD2KlbMrP"
# consumer_secret = "gEDARHS9173Mu32YrQaFkPXlfD24Eju5f9XxNxB5W29eODH032"
# access_token = "38209993-B8cma7162TSkJWDOa25qfCS8gUVLjxG6rwttJpgVw"
# access_token_secret = "lzFyPwU0naYp6jQUQGyNEo2zFAqzh0qlSc3jwxDiORGCb"

#consumer_key        = "twuQZxuLID8wioORp7nUCxPWu"
#consumer_secret     = "ebQoltU1d3RnhaQdpOwHeIQ3oH7GmvfkJYo2NeilrSk3KaKE4b"
#access_token        = "123043086-L89ej8XQCePoCGC3vWT3qKwTWtiTGtlUxAJNyz7Y"
#access_token_secret = "rje1kNUBr6aGgAToKZUOjjj2nUBUVllvSuqIJ3rFxiVJh"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

arq = csv.writer(open("contra_lula.csv", "w"), delimiter='\t',quotechar='"')
count = 0
arq2 = open("contra_lula.json", "w", encoding= 'utf-8')
arq3 = open("contra_lula.txt", "w")
statuses = tweepy.Cursor(api.search, q=('#MoluscoNaCadeia' or '#CondenaTRF4'), since='2018-01-24', until='2018-01-26').items()
row=[]
    #----------------------------------------------------------------#
    # STEP 1: Query Twitter
    # STEP 2: Save the returned tweets
    # STEP 3: Get the next max_id
    #----------------------------------------------------------------#
cont = 0
while True:

    try:
         status  = statuses.next()
         json.dump(status._json,arq2,sort_keys = True,indent = 4, ensure_ascii=False) 

         if(hasattr(status,"retweeted_status")):          
            row = str(status.created_at), str(status.retweeted_status.created_at), str(status.user.screen_name), str(status.user.id_str), \
                  str(status.user.followers_count), str(status.user.friends_count), \
                  str(status.retweeted_status.user.screen_name), str(status.retweeted_status.user.id_str), str(status.retweeted_status.user.followers_count), str(status.retweeted_status.user.friends_count), \
                  str(status.retweeted_status.retweet_count), str(status.retweeted_status.favorite_count), str(status.text), str(status.retweeted_status.entities.get('hashtags')), \
                  str(status.retweeted_status.entities.get('media')), str(status.retweeted_status.created_at) 
   
         else:
            row = str(status.created_at), "None", str(status.user.screen_name), str(status.user.id_str), str(status.user.followers_count), \
                  str(status.user.friends_count), \
                  "None", "None", "None", "None", \
                  str(status.retweet_count), str(status.favorite_count), str(status.text), "None", "None"

         arq.writerow(row)
         arq3.write(str(status))
         arq3.write('\n')
         count=count+1
         if cont==0:
            print(str(status.created_at))
            cont=cont+1

    except tweepy.TweepError:
      print("wait 15 minutes..."+str(count))
      time.sleep(60 * 15)
      cont=0
      continue
    except StopIteration:
      print("Acabou a interacao")
      print (count)
      break
