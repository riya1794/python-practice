#word funcions

def break_words(sentence):
	words = sentence.spilt(' ')
	return words

def sort_words(words):
	sorted_words = sorted(words)
	return sorted_words

def first_word(words):
	first = words.pop(0)
	return first

def last_word(words):
	last = words.pop(-1)
	return last
