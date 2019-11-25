# \b	Word Boundary(Start/End of Word)
# \B	Not a Word Boundary
# Reference a position, not an actual character
# Before the first word character in the string
# After the last word character in the string
# Between a word character and a non word character

# '/\b\w+\b/' finds four matches in "This is a test."
# '/\b\w+\b/' matches all of "all_123" but only part of "top-notch"
# '/\bNew\bYork\b/' does not match "New York"
# '/\bNew\b \bYork\b/' matches "New York"
# '/\B\w+\B/' finds two matches in "This is a test." ("hi" and "es")
import re 
pattern = r'\w+e\b'
word = "Shall I compare thee to a summer's day? Thou art more lovely and more temperate: Rough winds do shake the darling buds of May, And summer's lease hath all too short a date"
print(re.findall(pattern, word)) # ['compare', 'thee', 'more', 'more', 'temperate', 'shake', 'the', 'lease', 'date']
