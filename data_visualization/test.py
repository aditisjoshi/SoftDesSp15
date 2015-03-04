#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy

#Variables that contains the user credentials to access Twitter API 
access_token = '2272000956-r0BA11BAK00nRKnclrr4W5LcjrgpvvlTev9rAXI'
access_token_secret = 'RJ1kFN7VaQAohQydIqa9RcY2gtWDBnGZtKi5PJQ3LOVTj'
consumer_key = "tOcOW6RJY0mUqLYavfiZEDOEs"
consumer_secret = "lFHVJqO6aPZGmiDBSwVJjB4icHd6a5CmHDCxVV8IhgxPZELyDV"
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

search_text = "#thedress"
search_number = 100
search_result = api.search(search_text, until='2015-03-04')
for i in search_result:
    print i.text

# #This is a basic listener that just prints received tweets to stdout.
# class StdOutListener(StreamListener):

#     def on_data(self, data):
#         print data
#         return True

#     def on_error(self, status):
#         print status


# if __name__ == '__main__':

#     #This handles Twitter authetification and the connection to Twitter Streaming API
#     l = StdOutListener()
#     auth = OAuthHandler(consumer_key, consumer_secret)
#     auth.set_access_token(access_token, access_token_secret)
#     stream = Stream(auth, l)

#     #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
#     stream.filter(track=['#thedress', '#whiteandgold', '#blueandblack'])