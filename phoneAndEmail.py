#! python3
# phoneAndEmail.py 
'''
---- Phone and email Program ----
Parses through text that user copied to clipboard, and looks
for phone numbers and emails, then pastes the formatted info
back onto the clipboard.
'''

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?				# area code (optional - so "?")
	(\s|-|\.)?						# separator
	\d{3}							# first 3 digits
	(\s|-|\.)						# separator
	\d{4}							# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		# extension
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+				# 1 - email username
	@								#     @ symbol
	[a-zA-Z0-9.-]+					# 2 - domain name..ex:gmail, aol
	(\.[a-zA-Z]{2,4})				# 3 - dot-something
	)''', re.I | re.VERBOSE)
	
'''
note 1: username part - one or more characters (+ sign) that can be any of the following:
		lowercase/upercase letters, numbers, dot, underscore, percent, plus, hyphen
		[a-zA-Z0-9._%+-]
note 2: domain name similar to username - but slightly less permissive character class
note 3: dot-com part (technically known as top-level domain, which can really be dot-anyhting
		between two and four characters
		
sidenote: format for email addresses has a lot of weird rules
		This regex won't match every possible valid email address, but will match most
		typical addresses you'll encounter.
'''
	
# TODO: Find matches in clipboard text
#		Handle errors if no match is found.
text = str(pyperclip.paste())
matches = []

for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1],groups[3], groups[5]])	# formats: xxx-xxx-xxxx
	if groups[6] != '':
		phoneNum += ' x' + groups[6]						# add extension if found
	matches.append(groups[0])

for groups in emailRegex.findall(text):
	matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print(matches)
	print('Copied to clipboard: ')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found.')


