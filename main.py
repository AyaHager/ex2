# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
def revword(word: str) -> str:
    word = word.lower()
    return (word[::-1])

def countword():
    file = open("text.txt", "r")
    txt = file.read()
    file.close()
    word = txt.split()[0]
    word = word.lower()
    words = txt.split(" ")
    length = len(words)
    counter = 1
    newText = word + "\n"
    lenOfFirstWord = len(newText)
    words[0] = words[0][lenOfFirstWord:]
    for i in range(0, length):
        tempWord = words[i]
        if tempWord.__contains__("\n"):
            words2 = tempWord.split("\n")
            for j in range(len(words2)):
                revWord2 = revword(words2[j])
                if(revWord2 == word):
                    counter += 1
                newText += revWord2 + "\n"
            newText = newText[:-1]
            newText = newText + " "
        else:
            reverseWord = revword(tempWord)
            if reverseWord == word:
                counter += 1
            newText += reverseWord + " "
    newText = newText[:-1]
    fileW = open("text2.txt","w")
    fileW.write(newText)
    return counter


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(countword())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
