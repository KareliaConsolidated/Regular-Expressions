# ^ Negate a Character set
# Not any one of Several Characters (like !)
# To do that, add ^ as the first character inside the character set
# /[^aeiou]/ matches any one consonant (non-vowel)
# /see[^mn]/ matches "seek" and "sees" but not "seem" or "seen"
import re 
pattern = 'see[^mn]'
word = re.findall(pattern, 'seek sees seem seen')
print([word[i] for i in range(len(word))]) # ['seek', 'sees']

### Caution ###
# /see[^mn]/ does not match "see"
# /see[^mn]/ does match "see." and "see "

word_test = 'I am going to test the space count !'
pattern_test = '[^A-Za-z!]'
space_test = re.findall(pattern_test, word_test)
print(len([space_test[i] for i in range(len(space_test))])) # 8
