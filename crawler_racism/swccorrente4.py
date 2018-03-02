import codecs
import time
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")
import tweepy
import csv


#consumer_key="8OKW5ik3n8DqT4npsBMQ5zZQI"
#consumer_secret="RxysoCbyEhzLWyyPmgVgFjmiEJw4fvUo2pd0i2fmfQYKpgTpQj"
#access_token="191712148-a8fuYrl7R7TDlYGunaOArmD2qF0GvAxGiINV2lbc"
#access_token_secret="AVr5CSGBXfoCpTiSmgYAjInqd1a9PYvHm7p9k9aHCYpoS"

consumer_key        = "twuQZxuLID8wioORp7nUCxPWu"
consumer_secret     = "ebQoltU1d3RnhaQdpOwHeIQ3oH7GmvfkJYo2NeilrSk3KaKE4b"
access_token        = "123043086-L89ej8XQCePoCGC3vWT3qKwTWtiTGtlUxAJNyz7Y"
access_token_secret = "rje1kNUBr6aGgAToKZUOjjj2nUBUVllvSuqIJ3rFxiVJh"
# consumer_key = "Ncg99iYY0Z7ZNER2zD2KlbMrP"
# consumer_secret = "gEDARHS9173Mu32YrQaFkPXlfD24Eju5f9XxNxB5W29eODH032"
# access_token = "38209993-B8cma7162TSkJWDOa25qfCS8gUVLjxG6rwttJpgVw"
# access_token_secret = "lzFyPwU0naYp6jQUQGyNEo2zFAqzh0qlSc3jwxDiORGCb"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
# arq = open("tweets_Amazonas.txt", "w")
# impeachment OR Dilma OR Eduardo Cunha OR Pedaladas fiscais
# statuses = tweepy.Cursor(api.search, q='impeachment OR Dilma OR (Eduardo AND Cunha) OR (Pedaladas AND fiscais) OR PT OR Lula OR #NaoTeraGolpe OR #ForaDilma OR (Lula AND honesto)', since='2016-01-20', until='2016-01-22').items()
# statuses = tweepy.Cursor(api.search, q='Dilma OR Eduardo Cunha OR PT OR Lula', since='2016-01-20', until='2016-01-22').items()
# statuses = tweepy.Cursor(api.search, q='(Lula AND Inocente) OR Lula', since='2016-01-20', until='2016-01-24').items()

arq = csv.writer(open("RTs_blackfriday.csv", "w"), delimiter='\t',quotechar='"')
count = 0
arq2 = open("RTs_blackfriday.txt", "w")
statuses = tweepy.Cursor(api.search, q=('RT' and 'Black Friday OR BlackFriday OR #blackfriday'), since='2017-11-30', until='2017-11-31').items()
row=[]
    #----------------------------------------------------------------#
    # STEP 1: Query Twitter
    # STEP 2: Save the returned tweets
    # STEP 3: Get the next max_id
    #----------------------------------------------------------------#
cont =0
while True:

    try:
         status  = statuses.next()

         if(hasattr(status,"retweeted_status")):
            row = str(status.user.screen_name), str(status.user.id_str), str(status.created_at), str(status.retweet_count), str(status.user.followers_count), \
                  str(status.user.friends_count),str(status.retweeted_status.user.screen_name),str(status.retweeted_status.user.id_str), \
                  str(status.in_reply_to_user_id), str(status.text)
         else:
            row = str(status.user.screen_name), str(status.user.id_str), str(status.created_at), str(status.retweet_count), str(status.user.followers_count), \
                  str(status.user.friends_count), "None","None", str(status.in_reply_to_user_id), str(status.text)

         arq.writerow(row)

         arq2.write(str(status))
         arq2.write('\n')
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
