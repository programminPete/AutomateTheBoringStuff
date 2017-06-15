#! python3
#madlib.py - 

# Usage: 
# Create a Mad Libs program that reads in text files and 
# lets the user add their own text anywhere the word ADJECTIVE, 
# NOUN, ADVERB, or VERB appears in the text file.

# import re  # did without regex first

def madlibs():

# Open a text file and save to variable 'content'
	filename = input('Give me a text file: ')
	file = open(filename, 'r')
	text = file.read()

	adj = 'ADJECTIVE'
	noun = 'NOUN'
	verb = 'VERB'
	adverb = 'ADVERB'
	print(len(words))
	madlibs_words = []
	madlibs_keys = []
	# split the text into words - then go through and prompt user on replacement.
	words = text.split()
	for word in words:
		if adj in word:
			user_lib = input('Enter an adjective: ')
		elif noun in word:
			user_lib = input('Enter an noun: ')
		elif verb in word:
			user_lib = input('Enter a verb: ')
		elif adverb in word:
			user_lib = input('Enter an adverb: ')
		else:
			madlibs_words.append(word)
			continue
		# If old word had a period after, add into the replacement word.
		if word.endswith('.'):
			user_lib = user_lib+'.'
		#append the added word into the madlib_words list of words
		madlibs_words.append(user_lib)

#	print(madlibs_words)
#	print(madlibs_keys)
	#join the list into the 
	text_out = " ".join(madlibs_words)

	print(text)
	print(text_out)
	
madlibs()
