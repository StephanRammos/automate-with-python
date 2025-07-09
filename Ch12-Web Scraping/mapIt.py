#mapIt.py
#mapIt.bat in C:\Users\user\Scripts\
import webbrowser
#webbrowser.open('https://www.google.com/maps/place/870+Valencia+St,+San+Francisco,+CA+94110/')

import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
	#Get address form command line. Recall first element of sys.argv list is the filename
	address = ' '.join(sys.argv[1:])
	#if CL args D.N.E. then use clipboard via pyperclip module
else:
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
