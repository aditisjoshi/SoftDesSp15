import requests # pip install requests
import facebook # pip install facebook-sdk
import json


base_url = 'https://graph.facebook.com/me'
ACCESS_TOKEN = 'CAACEdEose0cBABZCCbeL7T8vqRskLxLtsd8sYQYFbW2maSjuu2AcZCGflcMNuINMLCmvztqBNfv0lezInZB35ljia6no8ERK9S2dTmvabt0irvpcaYyPelwvMacE1GKR5IYiGutFiYD3AXCu5DZA5gylFKqbQHgpVF2ZCjPeE0iFZC7JOcPLoT16sjwztdZBPYGMZByDPaefZBFHjeFmo4j8ZB'

# Get 10 likes for 10 friends
fields = 'id,name,friends.limit(10).fields(likes.limit(10))'

url = '%s?fields=%s&access_token=%s' % \
    (base_url, fields, ACCESS_TOKEN)

# Create a connection to the Graph API with your access token

g = facebook.GraphAPI(ACCESS_TOKEN)


def pp(o): 
    """
    A helper function to pretty-print Python objects as JSON
    """
    print json.dumps(o, indent=1)

# Find Pepsi and Coke in search results

# pp(g.request('search', {'q' : '#blackandblue', 'type' : 'page', 'limit' : 2}))

# # Use the ids to query for likes

thedress_pageid = '736182803145921'
pp(g.get_object(thedress_pageid))

print '##########################################################################'
pp(g.get_connections(thedress_pageid, 'story_tags'))
# pepsi_id = '56381779049' # Could also use 'PepsiUS'
# coke_id = '40796308305'  # Could also use 'CocaCola'

# # A quick way to format integers with commas every 3 digits
# def int_format(n): return "{:,}".format(n)


# if __name__ == "__main__":
#     print "Pepsi likes:", int_format(g.get_object(pepsi_id)['likes'])
#     print "Coke likes:", int_format(g.get_object(coke_id)['likes'])
