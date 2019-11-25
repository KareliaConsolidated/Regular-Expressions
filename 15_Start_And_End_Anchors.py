# Start and End Anchors
# ^ Start of String/Line
# $ End of String/Line
# \A Start of String, Never End of Line
# \Z End of String, Never End of Line

# Start and End Anchors, reference a position, not an actual character
# Zero-width
import re 
pattern = '^\w+@\w+\.[a-z]{3}$'
word = 'someone@nowhere.com'
print(re.findall(pattern, word))

# Line Breaks and Multimode
# print(re.search("^regex$", "string", re.MULTILINE))