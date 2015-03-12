# from pattern.web import *
# from pattern.en import * 

# fb = Facebook(license='CAAEuAis8fUgBADADmXLSVYzufNYqia0gSZASFdbAwiStXVkj51ZCy9UtxN08ZB5GBh1RtWLfRgT3dVbb7wiWZAh87iRXffjVomfnkZAmzpyO6tXZBUhBKb2OUz74foDj3vXdiShVodpZAQxT5nfWYXhsuL2eHMeMWtWN7YaMKnAAnhZAFsXreQVXLpzXpv1vBGYZD')

# for post in fb.search('#blackandblue', type=SEARCH, since='2015-02-26', until='2015-03-04'):
# 	texts = repr(post.text)
# 	dates = repr(post.date)
# print len(fb.search('#blackandblue', type=SEARCH, since='2015-02-26', until='2015-03-04'))

# for post in fb.search('#whiteandgold', type=SEARCH):
# 	texts = repr(post.text)
# 	dates = repr(post.date)
# print len(fb.search('#whiteandgold', type=SEARCH))


import requests # pip install requests
import json

base_url = 'https://graph.facebook.com/me'
ACCESS_TOKEN = 'CAACEdEose0cBANTrgIbvgdL7FZBzC38nW0XwIbdaEDqAnRIZBYJlBHAqUu1OY1ZBKfhZAlJXL0LlcKepRMoh38trZCXi6R8Fe0cNLYjWPQmjuKJ9wGlGFskISLitg3ZCJrd2BHUGSJdc0NVfFxgLwv9VoceMAo3bZCRvjF2fhKsjffLyMUmUQyV7JhQHJKaeWsa4SAdUpEPbx7jZBRRIV8IX'


# Get 10 likes for 10 friends
fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN)

# This API is HTTP-based and could be requested in the browser,
# with a command line utlity like curl, or using just about
# any programming language by making a request to the URL.
# Click the hyperlink that appears in your notebook output
# when you execute this code cell to see for yourself...
print url

# Interpret the response as JSON and convert back
# to Python data structures
content = requests.get(url).json()

# Pretty-print the JSON and display it
print json.dumps(content, indent=1)



import facebook # pip install facebook-sdk

# A helper function to pretty-print Python objects as JSON

def pp(o): 
    print json.dumps(o, indent=1)

# Create a connection to the Graph API with your access token

g = facebook.GraphAPI(ACCESS_TOKEN)

# Execute a few sample queries

print '---------------'
print 'Me'
print '---------------'
pp(g.get_object('me'))
print
print '---------------'
print 'My Friends'
print '---------------'
pp(g.get_connections('me', 'friends'))
print
print '---------------'
print 'Social Web'
print '---------------'
pp(g.request("search", {'q' : 'social web', 'type' : 'page'}))
