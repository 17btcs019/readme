import os
import time
import tweepy
consumer_key= 	'WaXQ9rDcG6nxIv02X31G2fECj'
consumer_secret= 'WtctnQaDb3i64oGJLwlwEvHfKZwCogGaWKbtBsCJpLFS1lPmsu'
access_token= 	'819222898749472769-LYVWIzVaSSIP7t7O9r3oxZwMnWQC6lV'
access_token_secret= 'SVcMDXIxFnT3mFqddAfIVkaelwLIcwCDMTBy3L5kvppc2'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)
b=1
a=0
while a<=2:
    img="/home/cs2017a118/Desktop/img"+str(b)+".jpg"
    cmd="fswebcam -r 1024x720 -S 3 --jpeg 100 "+img
    os.system(cmd)
    print("pic taken")
    api.update_with_media(img, status="lol")
    print("wait")
    time.sleep(3)
    a+=1
    b+=1
    print("done")
