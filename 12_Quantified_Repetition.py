# Quantified Repetition
# { Start quantified repetition of preceding item
# } End quantified repetition of preceding item
# {min, max}
# min and max are positive numbers.
# min must always be included and can be zero.
# max is optional.

# Three Syntaxes
# \d{4,8} matches numbers with four to eight digits
# \d{4} matches numbers with exactly four digits (min is max)
# \d{4,} matches numbers with four or more digits (max is infinite)

# \d{0,} is the same as \d*
# \d{1,} is the same as \d+
# /A{1,2} bonds/ matches "A bonds" and "AA bonds" not "AAA bonds"
import re 
pattern = '\d\. \w{2,5}\s'
word = '''
1. a
2. ab
3. abc
4. abcd
5. abcde
6. abcdef
'''
print(re.findall(pattern,word)) # ['2. ab\n', '3. abc\n', '4. abcd\n', '5. abcde\n']