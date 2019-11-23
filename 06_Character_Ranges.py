# Character Ranges
# We use metacharacter(-) which represents "Range of Characters"
# Includes all character between two characters
# Only a metacharacter inside a character set; a literal dash otherwise.
# [0-9]
# [A-Za-z]

### CAUTION ###
# [50-99] is not all numbers from 50 to 99, it targets one number at one time.
import re 
pattern = '[0-9]'
word = re.findall(pattern, 'Call 911')
print([word[i] for i in range(len(word))]) # ['9', '1', '1']