# Match both "lives" and "lived"
# Match "virtue" but not "virtues"
# Match the numbers and periods on all numbered paragraphs
# Find the 16-character word that starts with "c"
import re
with open('Emerson.txt') as file:
	Emerson = file.read()
	pattern01 = 'live[sd]'
	result_01 = re.findall(pattern01, Emerson)
	print(result_01)  # ['lives', 'lives', 'lives', 'lives', 'lived', 'lived', 'lives']

	pattern02 = 'virtue[^s]'
	result_02 = re.findall(pattern02, Emerson)
	print(result_02) # ['virtue ', 'virtue ', 'virtue ', 'virtue ', 'virtue.', 'virtue ', 'virtue?', 'virtue,', 'virtue.', 'virtue ', 'virtue ', 'virtue,', 'virtue,', 'virtue.']

	pattern03 = '\d\.'
	result_03 = re.findall(pattern03, Emerson)
	print(result_03) # ['1.', '2.', '3.', '4.']

	pattern04 = 'c\w{15}'
	result_04 = re.findall(pattern04, Emerson)
	print(result_04) # ['circumnavigation']

