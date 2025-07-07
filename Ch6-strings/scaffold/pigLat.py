#program to overwrite strings with non-letter characters to only letter parts.
#scaffold for pigLat.py
words = ["hellios", ".ouranos", "10Thalassa"]

for i in range(len(words)):
    word = words[i]
    while len(word) > 0 and not word[0].isalpha():
        word = word[1:]
    words[i] = word #overwrite the list element
    print(word + '\n')
print(words)