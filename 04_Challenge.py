# Challenge: Characters
# Apply global regular expressions to the text "Self-Reliance"
# How many times does the word "self" appear ?
# Count: himself, herself, itself, myself, yourself, thyself
# Using three literal characters and three wildcard characters, match: please, palace, parade
# What matches /t..ch/ besides "teach"?
import re
with open('Emerson.txt') as file:
	Emerson = file.read()
	pattern_01 = 'Self-Reliance'
	print(len(re.findall(pattern_01, Emerson))) # 1
	pattern_02 = "self"
	print(len(re.findall(pattern_02, Emerson))) # 2
	pattern_03 = 'p..a.e'
	list_of_words = 'please palace parade'
	print(re.findall(pattern_03, list_of_words)) # ['please', 'palace', 'parade']	
	pattern_04 = 't..ch'
	result = re.findall(pattern_04, Emerson)
	print([result[i] for i in range(len(result)) if result[i] != 'teach'])