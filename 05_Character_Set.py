# Character Set Metacharacters
# [ Begin a Character Set
# ] End a Character Set
# Any one of serveral Characters
# But only one character
# Order of characters in the set does not matter
# /[aeiou]/ matches any one vowel
# /gr[ea]y/ matches "grey"
import re
pattern = 'gr[ea]y'
print(re.findall(pattern, 'grey gray')) # ['grey', 'gray']