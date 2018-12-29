import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
num = phoneNumRegex.search('My number is 509-555-9911.')

print('Phone number: ' + num.group())
