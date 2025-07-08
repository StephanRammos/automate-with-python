#English to Pig Latin
print("English to Pig Latin:")
message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = [] #A list of the words in Pig Latin.
for word in message.split(): 
	#Seperate the non-letters at the start of this word:
	prefixNonLetters = ''
	#while ... and the first element of word is not a letter. Concatenate the 0-th element of word
	#to prefixNonLetter. Overwrite word to exclude 0th element.
	while len(word) > 0 and not word[0].isalpha():
		prefixNonLetters += word[0]
		word = word[1:]
	if len(word) == 0:
		pigLatin.append(prefixNonLetters)
		continue

	#Seperate the non letters at the end of this word:
	suffixNonLetters = ''
	while not word[-1].isalpha(): #when last character of word is not a letter
		suffixNonLetters += word[-1] + suffixNonLetters
		word = word[:-1]

	



