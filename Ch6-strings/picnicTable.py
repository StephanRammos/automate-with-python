#picnicTable.py
def printPicnic(itemsDict, leftWidth, rightWidth):
	print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
	for k, v in itemsDict.items():
		#Left-align the key (like 'apples') within a field of width leftWidth (e.g. 12), and pad the rest with dots (.)
		#convert v to a string first bc .rjust() is a string method.
		print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches': 4, 'apples': 12, 'cups': 4, 'cookies': 8000}
printPicnic(picnicItems, 12, 5)
