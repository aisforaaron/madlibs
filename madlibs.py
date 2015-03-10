#!/usr/bin/env python
# Madlibs Script
import re  # regular expression methods
import stories
from stories import *

# get all story titles
allTitles = madlibStories.keys()

# ask user to pick a story title
titles = ''
for title in allTitles:
	titles += '-'+title+'\n'
storyTitle = raw_input("Pick a story by entering the title\n" + titles + ": ")

# get story text w/tokens (imported from stories.py)
storyText = madlibStories[storyTitle]

# split story text into lines by line break delimeter (splitlines method)
storyLines = storyText.splitlines()

# replace tokens w/unique tokens 
storyLinesTokens = []
counter=1
# loop through lines in story
for line in storyLines:
	# each updated line is saved into list as an item
	lineFinal = [] 
	# if the line is a line break "\n" line is null
	# so add empty slot to list
	if not line:
		storyLinesTokens.append('')
	else:
		# loop through all words in line, split by spaces
		for word in line.split(' '):
			# see if word is a token. a string like {...}
			w = re.match(r'({)(.*?)(})(.*)', word, re.M|re.I)
			# if there is a match, it's a token so replace with unique token name
			if w:
				wordFinal = '{' + str(counter) + w.group(2) + '}' + w.group(4) # w.group(4) is for punctuation/spaces
				counter+=1
			else: 
				wordFinal = word
			# rebuild line w/tokens
			lineFinal.append(wordFinal)
		# rebuild line w/line breaks
		j = ' '.join(lineFinal)
		storyLinesTokens.append(j)

# convert new story w/unique tokens back to string
storyText = '\n'.join(storyLinesTokens)

# use findall, regex method to pull out all tokens, add to list
tokens = re.findall(r'({.*?})', storyText, re.M|re.I)

# prompt user for answers, add to list
answers = [] # empty dict var
# loop through tokens, prompt user for entry
for token in tokens: 
	# use regex to just get the token w/o {#...}
	name = re.match(r'({\d*)(.*?)(})', token, re.M|re.I)
	answers.append(raw_input("Enter a " + name.group(2) + ": "))	# store answers in dict var

# Output to terminal
print '------------ ' + storyTitle +' ---------------' 
# loop through and replace tokens with user answers
counter = 0
for token in tokens:	
	storyText = re.sub(token, answers[counter], storyText)
	counter+=1
# print final story w/answers
print storyText