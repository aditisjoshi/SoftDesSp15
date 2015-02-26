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
		the result is a dictionary where the key is the professors name and the value is all the comments as a string
	
	>>> len(find_comments(3))
	3
	"""
	#creating a dictionary
	names_and_comments = {}

	#importing modules from the external file that will predict the gender
	gp = genderPredictor()
	gp.trainAndTest()

	for i in range(1,n + 1):

		#finding the urls and their html (for the number of wanted professors)
		url = 'http://www.ratemyprofessors.com/ShowRatings.jsp?tid=' + str(i)
		url_html = URL(url).download()
		soup = BS(url_html)
		
		#getting name and using external file to predict its gender
		first_name = soup.find('span', 'pfname').string
		last_name = soup.find('span', 'plname').string
		name = first_name + " " + last_name
		gender = gp.classify(first_name)

		#finding the professor department
		title = soup.find('div', 'result-title')

		#getting all of the comments
		comments = soup.find_all('td', 'comments')
		names_and_comments[name] = reduce(lambda x,y: x + " " + y, [comment.p.string.strip() for comment in comments])
	return names_and_comments	


def comment_analysis():
	"""
	function that will analyize the comments using sentiment analysis 
	"""
	names_and_comments = find_comments(3)
	for element in names_and_comments:
		print sentiment(names_and_comments[element])


comment_analysis()


if __name__ == "__main__":
	import doctest
	doctest.testmod()