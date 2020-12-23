import re

def numberOfUselessCharacters(word):
    word = ''.join(word.split())
    numberOfBackslashBackslash = len(re.findall(r'\\\\', word))
    numberOfBackslashDoubleQuotes = len(re.findall(r'\\"', word))
    numberOfBackslashX = len(re.findall(r'\\x', word))
    return 2 + numberOfBackslashBackslash + numberOfBackslashDoubleQuotes + 3 * numberOfBackslashX

word = r'"sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en"'
print(numberOfUselessCharacters(word))

f = open("input.txt", 'r')
word1 = r'""'
print(numberOfUselessCharacters(word1))

word2 = r'"abc"'
print(numberOfUselessCharacters(word2))

word3 = r'"aaa\"aaa"'
print(numberOfUselessCharacters(word3))

word4 = r'"\x27"'
print(numberOfUselessCharacters(word4))

f = open("input.txt", 'r')

totalNumberOfUselessCharacters = 0
for line in f:
    print(line)
    print(numberOfUselessCharacters(line))
    totalNumberOfUselessCharacters += numberOfUselessCharacters(line)

print(totalNumberOfUselessCharacters)



