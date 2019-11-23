# Metacharacters

# Characters with special meaning
# Transform literal characters into powerful expressions.
# Only a few to learn
# \.*+-{}[]^$|?():!=
# Can have more than one meaning

# The WildCard Metacharacter
# . (DOT) Any Character except newline or Line Break
import re

pattern1 = 'c.t'
pattern2 = '.a.a.a'

reg1 = re.findall(pattern1,'The cot, camel and cat communicated!')
reg2 = re.findall(pattern2,'Banana, Papaya')

print(reg1) # ['cot', 'cat', 'cat']
print(len(reg1)) # 3

print(reg2) # ['Banana', 'Papaya']
print(len(reg2)) # 2

# h.t matches "hat", "hot" and "hit", but not "heat"
# Broadcast match possible
# Most Common MetaCharacter
# Most Common Mistake:
	# /9.00/ matches "9.00", "9500", and "9-00"

# Tip: A good regular expression should match the text you want to target and only that text, nothing more!