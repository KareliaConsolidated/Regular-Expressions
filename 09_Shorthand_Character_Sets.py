# Shorthand		# Meaning		#Equivalent
# 	\d			   Digit			[0-9]
#  	\w		   Word Character		[a-zA-Z0-9_]
#   \s  		Whitespace			[\t\r\n]
#   \D  		Not Digit			[^0-9]	
#	\W 			Not Word Character  [^a-zA-Z0-9_]
#   \S    		Not Whitespace		[^\t\r\n]
# CAUTION
# _ is a word character
# - is not a word character

# /\d\d\d\d/ matches "194", but not "text"
# /\w\w\w/ matches "ABC", "123" and "1_A"
import re
pattern = '[\D\S]'
word = '1234 5678 abc'
result = re.findall(pattern, word)
print(result)