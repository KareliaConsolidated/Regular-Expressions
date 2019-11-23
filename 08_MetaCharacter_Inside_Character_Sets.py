# Metacharacters Inside Character Sets
# Most metacharacters inside character sets are already escaped
# Do not need to escape them again
# /h[a.t]/ matches "hat" and "h.t", but not "hot"
# EXCEPTIONS: ]-^\
import re 
pattern = 'h[a.]t'
word = 'hit hat h.t'
result = re.findall(pattern, word)
print(result) # ['hat', 'h.t']

pattern_test = 'var[(\[][0-9][\])]'
word_test = 'var(3) var[4]'
result = re.findall(pattern_test, word_test)
print(result) # ['var(3)', 'var[4]']

pattern_test = 'file[0\-\\_]1'
word_test = 'file01 file-1 file_1'
result = re.findall(pattern_test, word_test)
print(result) # ['file01', 'file-1', 'file_1']