#mclip.py  multi-clipboard automatic messages

TEXT = {'agree':"""Yes, I agree. That sounds fine to me.""",
	'busy':"""Sorry, can we do this later this week or next week?""",
	'upsell': """Would you consider making this a monthly donation?"""}

import sys , pyperclip
if len(sys.argv) < 2:
	print('Usage: python mclip.py [keyphrase] - copy phrase text')
	sys.exit()

keyphrase = sys.argv[1]  # first command line arg is the keyphrase

if keyphrase in TEXT:
	# copy to the clipboard the value corresponding to the user entered key
	pyperclip.copy(TEXT[keyphrase])
	print('Text for ' + keyphrase + ' copied to clipboard.')

else:
	print('There is no text for ' + keyphrase)

#Enter the following into editor and save file as mclip.bat


#my path to file is C:\Users\user\Desktop\automate-the-boring-stuff-with-python\Ch6-strings 
# i save the mclip.bat in the same ch6 folder. I think i read it has to be saved in a different folder?