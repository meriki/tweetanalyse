#put the data in a mongodb collection
#create another collection that has your country, number of times hillary ot trump are being written
#list of hashtags
#if the tweet is original or retweeted
#count the favorite counts on original tweets
#type of tweet
import pymongo
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from pymongo import MongoClient
client=MongoClient()
db=client.tweetdata
collection=db.tweets

access_token = '792138944187990016-UbthdabAkD2UuPE7ODZb5go7nLpQopN'
access_token_secret = 'gxnXEGT7EvypxH6BiDNL5MlaVIexWjUheOweo12CcXPYu'
user_key = 'EAtdi0QN3UuGlMSQtQe5Vc29m'
user_secret = 'pY5m2fmekSQ6z5EuSqW4ZzQBusNAXNtUKndcoxADyUliVxCzWn'

class StdOutListener(StreamListener):
	def on_data(self,data):
		tweet=json.loads(data)
		created_at=tweet['created_at']
		id_str=tweet['id_str']

		try:
			text=tweet['text']
		except Exception:
			text="none"

		if(text != "none"):
			if (tweet['text'].startswith('RT')):
				retweeted=True
			else:
				retweeted=False
		
		try:
			place=tweet['place']['country']
		except Exception:
				try:
					place=tweet['user']['location']
				except Exception:
					place="none"

		hashtags=[x['text'] for x in tweet['entities']['hashtags']]

		try:
			media=tweet['entities']['media']
		except Exception:
			try:
				media=tweet['retweeted_status']['entities']['media']
			except Exception:
				media="none"

		if(text=="none"):
			type_tweet="media"
		elif (media == "none"):
			type_tweet="text"
		else:
			type_tweet="text+image"

		fav_count=tweet['favorite_count']

		# obj={'id_str':id_str,'text':text,'place':place,'hashtags':hashtags,'favourite_count':fav_count,'type':type_tweet,'retweeted':retweeted}

		#here
		#create a hashtags dict with key as hashtag and value as number of times it appears
		#create a arraylist of places mentioned to plot
		#count original and retweets
		#create a dict of fav counts with key as no of fav counts and value as number of people having that many fav counts
		#a dic of text,image and text+image as keys and values as number of them

		obj={"id_str":id_str,"text":text,"place":place,"favourite_count":fav_count,"hashtags":hashtags,"retweeted":retweeted,"type":type_tweet}
		collection.insert(obj)
		print obj
		return True
	def on_error(self,status):
		print status 

if __name__=='__main__':
	listener=StdOutListener()
	auth=OAuthHandler(user_key,user_secret)
	auth.set_access_token(access_token,access_token_secret)
	stream = Stream(auth,listener)
	stream.filter(track=['#USelections, #hillary, #trump'])