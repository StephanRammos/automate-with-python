#bulletPointAdder.py
import pyperclip
#store the lists of films by country into variable text
text = pyperclip.paste()
print(text)
#seperate lines and add stars
lines = text.split('\n')
print(lines)

for i in range(len(lines)):  #loop through all indexes in the "lines" list"
	lines[i] = '* ' + lines[i].rstrip() #add star to each string in "lines" list
print(lines)

# Join and copy back to clipboard
pyperclip.copy('\n'.join(lines))