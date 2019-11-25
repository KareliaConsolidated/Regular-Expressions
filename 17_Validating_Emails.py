import re
pattern = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
word = 'ex_am_ple@example.com'
print(re.findall(pattern, word)) # ['ex_am_ple@example.com']