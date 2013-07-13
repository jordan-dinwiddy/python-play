#!/usr/bin/python

args = [3, 6];

# Here the * is unpacking the arguments list into positional 
# arguments to be parsed into the function
print range(*args);


# In the same fashion, dictionaries can be used to deliver keyword
# arguments to a function. 

def say_something(word_1='word1', word_2='word2'):
	print "word_1: " + word_1
	print "word_2: " + word_2


say_something()
say_something(word_2='Yo dude');

keyword_args = {"word_1": "hey man", "word_2": "how you doing?"};
say_something(**keyword_args);
