#! python3
#strongPasswordCheck.py


import pyperclip, re

lengthRegex = re.compile(r'\S{8,}')
upperRegex = re.compile(r'[A-Z]')
lowerRegex = re.compile(r'[a-z]')
numberRegex = re.compile(r'[0-9]')

print('To stop, enter blank password')
while True:
	password = input('Give me a password:  ')
	if password == '':
		break
	strong = []
	len = lengthRegex.search(password).group()
	up = upperRegex.search(password).group()
	low = lowerRegex.search(password).group()
	try:
		num = numberRegex.search(password).group()
	except AttributeError:
		num = 'None'
	test = [len, up, low, num]
#TODO - make this into a dictionary so you could see that "num = None"
#		-aka, you can see where the error is
	
	print(test)

	if 'None' not in test:
		print('good job, password saved')
		break
	else:
		print('password must be >8 characters, and have a number and both lowercase/uppercase letters')
		continue