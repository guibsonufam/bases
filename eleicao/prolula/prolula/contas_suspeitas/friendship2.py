import tweepy
import sys
import os
import time

consumer_key        = "twuQZxuLID8wioORp7nUCxPWu"
consumer_secret     = "ebQoltU1d3RnhaQdpOwHeIQ3oH7GmvfkJYo2NeilrSk3KaKE4b"
access_token        = "123043086-L89ej8XQCePoCGC3vWT3qKwTWtiTGtlUxAJNyz7Y"
access_token_secret = "rje1kNUBr6aGgAToKZUOjjj2nUBUVllvSuqIJ3rFxiVJh"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


arq = open('contas_suspeitas_prolula.txt', 'r')
texto = arq.readlines()

for linha in texto:
	arq2 = open("contas_suspeitas_text_" + linha + ".txt", "w",encoding= 'utf-8')
	stuff = tweepy.Cursor(api.user_timeline, user_id = linha, count = 10, include_rts = True).items()
	#for linha in texto:
	cont=0
	for status in stuff:
		try:
			arq2.write(str(status.created_at) + '\n')
			arq2.write(status.text + '\n')
			#arq2.write('\n')
			#print (status.text)
			cont = cont + 1
			if(cont==10):
				break
		except Exception as e:
			print("wait 15 minutes")
			time.sleep(60*15)

arq.close()