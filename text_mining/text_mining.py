"""
text-mining
Aditi Joshi
Software Design Spring 2015
goal of the project: to find comments from ratemyprofessors.com and parse through them to find words used most often between genders
"""


from pattern.web import *
from pattern.en import * 
from bs4 import BeautifulSoup as BS
import random
from genderPredictor import genderPredictor


def find_comments(n):
	""" 
		Returns the comments for a given professor in a dictionary where the key is the Professor's name
		n is the number of professors that you have to loop through
		the result is two dictionary where the key is the professors name and the value is all the comments as a string
		there is one dictionary for all male professors and another one as all female professors
	"""
	#creating a dictionary for both genders
	women_dict = {}
	men_dict = {}

	#importing modules from the external file that will predict the gender
	gp = genderPredictor()
	gp.trainAndTest()

	for i in range(1,n + 1):

		#finding the urls and their html (for the number of wanted professors)
		url = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + str(i)
		url_html = URL(url).download()
		soup = BS(url_html)
		
		#checking to make sure that the url is valid
		try:
			#getting name and using external file to predict its gender
			first_name = soup.find('span', 'pfname').string
			last_name = soup.find('span', 'plname').string
			name = first_name + " " + last_name
			gender = gp.classify(first_name)

			#getting all of the comments
			comments = soup.find_all('td', 'comments')

			#write the comments to the appropriate dictionary (if it is a woman, women_dict, if it is a man, man_dict)
			if gender == 'M':
				men_dict[name] = reduce(lambda x,y: x + " " + y, [comment.p.string.strip() for comment in comments])
			elif gender == 'F':
				women_dict[name] = reduce(lambda x,y: x + " " + y, [comment.p.string.strip() for comment in comments])	

		#if the url is not valid, then pass and go to the i value of the loop
		except:
			pass

	return men_dict, women_dict	

def sentiment_analysis(dictionary):
	"""
	this function will do sentiment analysis for each of the comments for the professors in the dictionary
	"""

	sentiment_dict = {}

	#for each of those dictionary values, go through the comments and do sentiment analysis for each set of comments
	for element in dictionary:
		sentiment_dict[element] = sentiment(dictionary[element])
	return sentiment_dict


def text_analysis(dictionary, words):
	"""
	this function is going to parse through a given dictionary for both sentiment analysis as well as a list of words given to the function
	
	>>> text_analysis({'animal': 'catz'},['catz'])
	{'catz': 1}
	>>> text_analysis({'animal': 'catz', 'fabulous': 'catz'},['catz'])
	{'catz': 2}
	>>> text_analysis({'animal': 'catz catz'},['catz'])
	{'catz': 2}
	"""

	word_count = {}

	#then, use the key words in the list that was passed in to count the frequency of the words that were passed in
	for word in words:
		for element in dictionary.values():
			values = element.split()
			for item in values:
				if word in item:
					current = word_count.get(word,0)
					word_count[word] = current + 1
 	
	return word_count


def comment_analysis(n, words):
	"""
	function that will analyize the comments using sentiment analysis 
	it takes in the number of professors that you want to check for and a list of words that you want to count the comments for
	"""

	# first call the function that will give you a dictionary of name and comments 
	men_dict, women_dict = find_comments(n)

	#calls sentiment_analysis to find the sentiment in each of the comments associated with the professors
	men_sentiment = sentiment_analysis(men_dict)
	women_sentiment = sentiment_analysis(women_dict)

	#calls the text analysis to find the number of the words
	men_word_count = text_analysis(men_dict, words)
	women_word_count = text_analysis(women_dict, words)

	return men_sentiment, women_sentiment, men_word_count, women_word_count


#print comment_analysis(500,['mean','boring','evil','difficult','hard','nice','friendly','smart','fun','funny','rude','ugly'])


if __name__ == "__main__":
	import doctest
	doctest.testmod()