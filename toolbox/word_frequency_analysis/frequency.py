""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	f = open(file_name,'r')
	lines = f.readlines()
	punctuation = string.punctuation
	curr_line = 0
	words = []
	while lines[curr_line].find('START OF THIS PROJECT GUTENBERG EBOOK') == -1:
		curr_line += 1
	lines = lines[curr_line+1:]
	for item in lines:
		word = item.split()
		for item in word:
			for letter in punctuation:
				print letter
				
				item = item.replace(letter,'')
			item = item.strip(string.whitespace)
			item = item.lower()
			words.append(item)
	test = 'twenty!two'
	print string.punctuation
	print test.strip(string.punctuation)
	return words[0:100]

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	pass

print get_word_list('littleWomen.txt')