# ( Start grouped expression
# ) End grouped expression
# Group Portions of the expression
# Apply repetition operators to a group
# Create a group of alternation expressions
# Captures group for use in matching and replacing

#/(abc)+/ matches "abc" and "abcabcabc"
# /(in)?dependent/ matches "independent" and "dependent"
import re
word = '555-666-7890'
pattern = '(\d{3})-(\d{3})-(\d{4})'
print(f"{re.findall(pattern, word)}")

pattern_01 = 'w(ei|ie)rd'
word_01 = 'weird or wierd'
print(re.findall(pattern_01, word_01))