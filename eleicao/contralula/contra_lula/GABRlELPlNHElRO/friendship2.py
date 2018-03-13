import tweepy
import csv
import time
import os
import json
import sys
import sys

# -*- encoding: utf-8 -*-
consumer_key="8OKW5ik3n8DqT4npsBMQ5zZQI"
consumer_secret="RxysoCbyEhzLWyyPmgVgFjmiEJw4fvUo2pd0i2fmfQYKpgTpQj"
acess_token="191712148-a8fuYrl7R7TDlYGunaOArmD2qF0GvAxGiINV2lbc"
acess_token_secret="AVr5CSGBXfoCpTiSmgYAjInqd1a9PYvHm7p9k9aHCYpoS"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(acess_token,acess_token_secret)
userID_target = '871133532810125312'
api=tweepy.API(auth, wait_on_rate_limit=True)

row_segue=[]
row_naoSegue=[]

arq2 = open("seguem.txt", "w",encoding= 'utf-8')
arq3 = open("nao_seguem.txt", "w",encoding= 'utf-8')
arq4 = open("error_exception","w",encoding= 'utf-8')
arq = open('ids.txt', 'r')
texto = arq.readlines()

for linha in texto :
    try:    
        print(linha)    
        a = (api.show_friendship(source_id=linha, target_id=userID_target))[0].following
        row_segue = (api.show_friendship(source_id=linha, target_id=userID_target))

        if a==True:
            row_segue = str(row_segue[0].id_str), str(row_segue[1].id_str)
            #print(row)        
            arq2.write(str(row_segue)+'\n')
            
       
        elif a==False:
            #print("nao segue")
            row_naoSegue = str(row_segue[0].id_str), str(row_segue[1].id_str)
            arq3.write(str(row_naoSegue)+'\n')

    
    except tweepy.TweepError as e:
        if e.api_code == 163:
            print("achou erro 163")         
            arq4.write(linha + e.reason +'\n')        
        else:        
            print("wait 15 minutes...")
            arq4.write(linha + e.reason +'\n')
            #+str(count)        
            time.sleep(60 * 15)
            #cont=0
        continue
    except StopIteration:
        print("Acabou a interacao")
        #print (count)
        break

arq.close()

#print(a[0].following, a[1].following)
