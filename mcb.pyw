#! python3
#mcb.pyw - Multclipboard (mcb)

# Usage: py.exe mcb.pyw save <keyword> 	- Saves clipboard to keyword 
#		py.exe mcb.pyw <keyword> 		- Loads keyword to clipboard
#		py.exe mcb.pyw delete <keyword>	- Deletes keyword from shelf
#		py.exe mcb.pyw clear			- Deletes all keywords
#		py.exe mc.pyw list 				- Loads all keywords to clipboard

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')		# shelf file named with the prefix 'mcb'

# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# List keywords
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	# Delete a single keyword
	elif sys.argv[1].lower() == 'delete':
		if sys.argv[2] in mcbShelf:
			del mcbShelf[sys.argv[2]]
	# Delete (clear) all keywords
	elif sys.argv[1].lower() == 'clear':
		mcbShelf.clear()
	# Copy keyword/content to shelf file (dictionary)
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

# TODO: List keywords and load content.

mcbShelf.close()