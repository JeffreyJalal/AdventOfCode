import re

def numberOfUselessCharacters(word):
    word = ''.join(word.split())
    word = word[1:-1]
    print(word)
    numberOfBackslashBackslash = len(re.findall(r'\\\\', word))
    numberOfBackslashDoubleQuotes = len(re.findall(r'\\"', word))
    numberOfBackslashX = len(re.findall(r'\\x', word))
    return 2 + numberOfBackslashBackslash + numberOfBackslashDoubleQuotes + 3 * numberOfBackslashX

word = r'"sjdivfriyaaqa\xd2v\"k\"mpcu\"yyu\"en"'
print(numberOfUselessCharacters(word))
print(word)
print(eval(word))

word1 = r'""'
print(numberOfUselessCharacters(word1))

word2 = r'"abc"'
print(numberOfUselessCharacters(word2))

word3 = r'"aaa\"aaa"'
print(numberOfUselessCharacters(word3))

word4 = r'"\x27"'
print(numberOfUselessCharacters(word4))

word5 = r'"syvugow"'
print(numberOfUselessCharacters(word5))

print("Begin")
f = open("input.txt", 'r')

totalNumberOfUselessCharacters = 0
totalNumberOfUselessCharactersS2 = 0
for line in f:
    print(line)
    solution1 = numberOfUselessCharacters(line)
    print(solution1)
    totalNumberOfUselessCharacters += solution1
    solution2 = len(''.join(line.strip())) - len(eval(line))
    print(solution2)
    totalNumberOfUselessCharactersS2 += solution2
    if(solution1 != solution2):
        print("Error on input : ")
        print(line)
        break



print(totalNumberOfUselessCharacters)
print(totalNumberOfUselessCharactersS2)

print(sum(len(''.join(s.strip())) - len(eval(s)) for s in open('input.txt')) )
print(sum(2+s.count('\\')+s.count('"') for s in open('input.txt')))



