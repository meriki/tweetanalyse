import json
import operator
from pymongo import MongoClient
client=MongoClient()
db=client.tweetdata
collection=db.t

total=collection.count()
cursor=collection.find()

count=0
places=[]
hashtags_count={}
type_media=0
type_text=0
type_both=0
am=1

for document in cursor:
	try:
		if document['text'].startswith('RT'):
			count=count+1
			text="i"
	except Exception:
		text="none"

	try:
		place.append(document['place']['bounding_box']['coordinates'])
	except Exception:
		c=1

	hashtags=[h["text"].lower() for h in document["entities"]["hashtags"]]
	for hashtag in hashtags:
		if hashtag in hashtags_count.keys():
			hashtags_count[hashtag]=hashtags_count[hashtag]+1
		else:
			hashtags_count[hashtag]=1

	try:
		media=document['entities']['media']
	except Exception:
		try:
			media=tweet['retweeted_status']['entities']['media']
		except Exception:
			media="none"
			# try:
			# 	media=tweet['retweeted_status']['retweeted_status']['entities']['media']
			# except Exception:
				# media="none"

	if(text=="none"):
		type_media=type_media+1
	elif (media == "none"):
		type_text=type_text+1
	else:
		type_both=type_both+1

#1
retweets=count
original = total-retweets
print "count_retweets",count

#2
sorted_hashtags=sorted(hashtags_count.items(),key=operator.itemgetter(1),reverse=True)
n=1
top10={}
def myfunction(text):
    try:
        text = unicode(text, 'utf-8')
    except TypeError:
        return text


# print sorted_hashtags
for x in sorted_hashtags:
	if n<=10:
		top10[x[0]]=hashtags_count[x[0]]
		n=n+1
	else:
		break

for v in sorted(top10.items(),key=operator.itemgetter(1),reverse=True):
	print v[0],top10[v[0]]
#3
hillary=['hillary','clinton','hillary2016','dumptrump','trumplies','queenofhearts','women','trumppence','trumphypocrite','crookeddonald','hillarybecause','clinton2016','trumprapist','hillary','hilaryclinton','gohillary','wegohiandvote','imstillwithher','clintonfoundation','hillarycare','nevertrump','hillaryclinton','iamwithher','strongertogether']
sumhillary=0
for h in hillary:
	sumhillary=hashtags_count[h]+sumhillary 

trump=['hillaryforprison','trump','maga','trumptrain','donaldtrump2016','blacksfortrump','womenfortrump','stophillary','hillary4prison','gotrump','teamtrump','trumplandslide','trumpsarkar','votetrump2016','votetrumppence16','donald','lockherup','donaldtrump','corrupthillary','neverhillary','trumpwin','trump2016']
sumtrump=0
for t in trump:
	sumtrump=hashtags_count[t]+sumtrump
print sumhillary,sumtrump
if(sumhillary>sumtrump):
	print "Hillary is more popular"
else:
	print "Trump is more popular"
#4
print type_both
print type_text
print type_media