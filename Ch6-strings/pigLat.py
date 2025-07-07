#English to Pig Latin
print("English to Pig Latin:")
message = input()

VOWELS = ('a','e','i','o','u','y')

pigLatin = [] #A list of the words in Pig Latin.
for word in message.split(): 
	#Seperate the non-letters at the start of this word:
	prefixNonLetters = ''
	while len(word) > 0 and not word[0].isalpha():
		prefixNonLetters += word[0]
		word = word[1:]
	if len(word) == 0:
		pigLatin.append(prefixNonLetters)
		continue

