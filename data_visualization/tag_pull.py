## Aditi Joshi & Jessica Sutantio
## Software Design SPring 2015 Mini Project 4

"""
Searches the social media sites: Twitter, Tumblr, Facebook, and Instagram
for tags that are relevant to the topic of the color of the viral laced dress.
From these tags, we will find the popular opinion of the dress' color and 
enable the user to view which opinion over time.

"""

""" Hashtag Permutations
	'blackandblue'
	'blacknblue'
	'blackblue'
	'blueandblack'
	'bluenblack'
	'blueblack'

	'whiteandgold'
	'whitengold'
	'whitegold'
	'goldandwhite'
	'goldnwhite'
	'goldwhite'

	all of the above + 'dress'

	'thedress'	"""

theDresstags = ['blackandblue','blacknblue','blackblue','blueandblack','bluenblack',
				'blueblack','whiteandgold','whitengold','whitegold','goldandwhite',
				'goldnwhite','goldwhite']

def string2hashtag(strlist):
	# add the hastag symbol to the list of strings
	theDresshashtags = []
	for tag in strlist:
		tag = '#' + tag
		# add 'dress' to each hashtag
		dresstag = tag + 'dress'
		theDresshashtags.append(tag)
		theDresshashtags.append(dresstag)
	theDresshashtags.append('#thedress')

	return theDresshashtags

#########################################################################

"""Twitter streaming"""
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains Aditi's user credentials to access Twitter API 
access_token = '2272000956-r0BA11BAK00nRKnclrr4W5LcjrgpvvlTev9rAXI'
access_token_secret = 'RJ1kFN7VaQAohQydIqa9RcY2gtWDBnGZtKi5PJQ3LOVTj'
consumer_key = "tOcOW6RJY0mUqLYavfiZEDOEs"
consumer_secret = "lFHVJqO6aPZGmiDBSwVJjB4icHd6a5CmHDCxVV8IhgxPZELyDV"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=string2hashtag(theDresstags))