# Repetition Metacharacters
# Metacharacter 		Meaning
#		*				Preceding item, zero or more times
#		+				Preceding item, one or more times
#		?				Preceding item, zero or one time

# /.+/ matches any string of characters except a line return
# /Good .+\./ matches "Good morning.", "Good day.", "Good Evening.", and "Good night."
# /\d+/ matches "90210"
# /\s[a-z]+ed\s/ matches lowercase words ending in "ed"
# /apples*/ matches "apple", "apples" and "applesssss"
# /apples+/ matches "apples" and "applesssss", but not "apple"
# /apples?/ matches "apple" and "apples", but not "applesssss"
# /colou?r/ matches "color" and "colour"
import re
pattern_01 = 'apples*'
pattern_02 = 'apples+'
pattern_03 = 'apples?'
word = 'apple apples applesssss'
print(f" apples* : {re.findall(pattern_01, word)}")
print(f" apples+ : {re.findall(pattern_02, word)}")
print(f" apples? : {re.findall(pattern_03, word)}")