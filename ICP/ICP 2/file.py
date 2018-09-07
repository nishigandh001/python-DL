fname = input("Enter the name of the file:")
infile = open(fname, 'r')
words = 0
characters = 0
for line in infile:
    wordslist = line.split()
    words = words + len(wordslist)
    characters = characters + len(line)
print(words)
print(characters)