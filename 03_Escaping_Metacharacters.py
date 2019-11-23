# \ Escape the next character
# Allow use of metacharacters as literal characters.
# Match a Period with \. (Now its a Literal Period)
# /9\.00/ matches "9.00", but not "9500" or "9-00"
# Match a backslash by escaping a backslash (\\)
# Escaping is only done for metacharacters.
# Literal characters should never be escaped; may give them meaning.
# Quotation marks are not be metacharacters; do not need to be escaped.
import re

pattern = '9.00' 

reg = re.findall(pattern,'9.00 9500 9-00')

print(reg) # ['9.00', '9500', '9-00']
print(len(reg)) # 3

pattern_escape = '9\.00' 

reg_esc = re.findall(pattern_escape,'9.00 9500 9-00')

print(reg_esc) # ['9.00']
print(len(reg_esc)) # 1

pattern_escape_part = 'h.._export\.txt' 

reg_esc_part = re.findall(pattern_escape_part,'his_export.txt her_export.txt')

print(reg_esc_part) # ['his_export.txt', 'her_export.txt']
print(len(reg_esc_part)) # 2

# Other Special Characters
# Spaces
# Tabs (\t)
# Line Returns (\r, \n, \r\n) # \r - Line Return, \n - New Line