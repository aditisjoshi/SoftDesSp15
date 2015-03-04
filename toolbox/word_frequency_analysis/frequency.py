""" Analyzes the word frequencies in a book downloaded from
	Project Gutenberg """

import string

def get_word_list(file_name):
	""" Reads the specified project Gutenberg book.  Header comments,
		punctuation, and whitespace are stripped away.  The function
		returns a list of the words used in the book as a list.
		All words are converted to lower case.
	"""
	start_string = 'START OF THIS PROJECT GUTENBERG EBOOK'

	# opening book and reading 
	with open(file_name,'r') as f:
		whole_text = f.read()

	# finding the start
	start = whole_text.find(start_string)
	whole_text = whole_text[start+len(start_string):]
	whole_text = whole_text.translate(None, string.punctuation).lower().strip()

	# splitting into words and returning 
	return whole_text.split()

def get_top_n_words(word_list, n):
	""" Takes a list of words as input and returns a list of the n most frequently
		occurring words ordered from most to least frequently occurring.

		word_list: a list of words (assumed to all be in lower case with no
					punctuation
		n: the number of words to return
		returns: a list of n most frequently occurring words ordered from most
				 frequently to least frequently occurring
	"""
	word_count = {}

	for word in word_list:
		current = word_count.get(word,0)
		word_count[word] = current + 1

	word_frequency = sorted(word_count.items(), key=lambda x: -x[1])

	return [word for word,frequency in word_frequency[:n]]

word_list = get_word_list('littleWomen.txt')
print get_top_n_words(word_list,100)