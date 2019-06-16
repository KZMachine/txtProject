# Karim Zaher


def wordcount(fileSelected):
    # Choose which file to edit
    selectedFile = open(fileSelected + ".txt", 'r')
    # Initialize variables
    wordCounter = 0
    alphabet = []

    for letter in range(97, 123):
        alphabet.append(chr(letter))

    for line in selectedFile:
        words = line.split(" ")  # Turns a line into an array
        if words != ['\n']:  # Checks to see whether line is empty or not
            for word in words:
                for i in alphabet:
                    if i in word.lower():
                        wordCounter += 1
                        break
    return wordCounter


print("0 - Word Counter")
print("1 - Encrypt Text[currently unavailable]")
print("2 - Decrypt Text[currently unavailable]")
print("3 - Exit")

action = int(input("\nSelect an action: "))

while action not in [0, 1, 2, 3]:  # If input is invalid
    print("Invalid input:", action)
    print("0 - Word Counter")
    print("1 - Encrypt Text[currently unavailable]")
    print("2 - Decrypt Text[currently unavailable]")
    print("3 - Exit")
    action = int(input("What action would you like to perform?"))

if action == 3:
    quit()

fileName = input("Enter .txt File Name: ")
if ".txt" == fileName[len(fileName) - 4:len(fileName)]:  # Removes .txt extension if user adds it
    fileName = fileName[0:len(fileName) - 4]
    print(fileName)

if action == 0:
    print(wordcount(fileName))