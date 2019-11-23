# What are Regular Expressions ? 
# Regular Expressions are tool for searching and matching parts of a text by describing patterns that should be used, to identify those parts. A Regular Expressions is a set of symbols that describe the text pattern.
# Formal Language interpreted by a regular expression processor.
# Regular Expressions are not a programming language, they are used for matching, searching and replacing text.
# Used by Programming Languages
# "Regex" for Short

#### Usage Examples ####
# Test if a credit card number has the correct number of digits
# Test if an email address is in valid format
# Search a document for either "color" or "colour"
# Replace all occurences of "Bob", "Bobby" or "B" with "Robert"
# Count how many times "training" is preceded by "computer", "video" or "online".

#### Regular Expression Matches ####
# Matches
# A regular expression matches text if it correctly describes the text.
# Text matches a regular expression if it is correctly described by the expression.
# Online Resources 
# https://regexr.com
# https://regex101.com
# https://regexpal.com

# Notation Conventions 
# /abc/ # Forward Slashes represent delimiters, that defines pattern inside those delimiters

##### Modes #####
# Standard: /re/
# Global: /re/g # Match throughout the document
# Case insensitive:  /re/i
# Multiline:  /re/m # Match Text Across Multiline

# Grep
# grep
# g/re/p # Global Regular Expression Print

# Literal Characters
# /car/ matches "car"
# /car/ matches the first three letters of "carnival"
# Similar to Seaching in a Word Processor
# Simplest Match There Is
# Case-Sensitive(By-Deafult)

import re

pattern = 'cat'

reg = re.findall(pattern,'The cow, camel and cat communicated!')

print(len(reg)) # 2