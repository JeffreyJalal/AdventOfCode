def isNiceStringP1(word):
    vowels = {'a', 'e', 'u', 'i', 'o'}
    naugtyStrings = {"ab", "cd", "pq", "xy"}
    numberOfVowels = 0
    previousLetter = ""
    hasDoubleLetter = False
    for letter in word:
        if letter in vowels:
            numberOfVowels += 1
        if (previousLetter + letter) in naugtyStrings:
            return False
        if letter == previousLetter:
            hasDoubleLetter = True
        previousLetter = letter
    return (numberOfVowels >= 3) & hasDoubleLetter

print(isNiceStringP1("haegwjzuvuyypxyu"))

numberOfNiceWords = 0
f = open("input.txt", "r")
for word in f:
    #print(word)
    if isNiceStringP1(word):
        numberOfNiceWords += 1

print(numberOfNiceWords)

def isNiceStringP2(word):
    secondPreviousLetter = word[0]
    previousLetter = word[1]
    hasTwoPairsOfSame = False
    hasRepeatSecondAfter = False
    for i in range(2, len(word)):
        if word[i] == secondPreviousLetter:
            hasRepeatSecondAfter = True
        if (secondPreviousLetter + previousLetter) in word[i:]:
            hasTwoPairsOfSame = True
        if hasTwoPairsOfSame & hasRepeatSecondAfter:
            return True
        secondPreviousLetter = previousLetter
        previousLetter = word[i]
    return False

print(isNiceStringP2("ieodomkazucvgmuy"))

f.seek(0, 0)
numberOfNiceWordsP2 = 0
for word in f:
    #print(word)
    if isNiceStringP2(word):
        numberOfNiceWordsP2 += 1

print(numberOfNiceWordsP2)


f.close()