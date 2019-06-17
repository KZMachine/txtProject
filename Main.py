# Karim Zaher
import Encrypt # Class from "Encrypt.py" file
import FileNamer

crypto = Encrypt.Crypto()
filenamer = FileNamer.SetFileName()

# Initialize variables


def wordcount(fileSelected):
    # Initialize variables
    wordCounter = 0
    alphabet = []

    for letter in range(97, 123): # Create an alphabet array
        alphabet.append(chr(letter))

    # Choose which file to edit
    with open(fileSelected + ".txt", 'r') as selectedFile:
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
print("1 - Encrypt Text")
print("2 - Decrypt Text")
print("3 - Exit")

action = int(input("\nSelect an action: "))

while action not in [0, 1, 2, 3]:  # If input is invalid
    print("Invalid input:", action)
    print("0 - Word Counter")
    print("1 - Encrypt Text")
    print("2 - Decrypt Text")
    print("3 - Exit")
    action = int(input("What action would you like to perform?"))

if action == 3:
    quit()

filenamer.fileNamer()

fileName = filenamer.getFileName()
extension = filenamer.getExtension()

if action == 0:
    print(wordcount(fileName))
elif action == 1:
    crypto.encrypt_file(fileName, extension)
elif action == 2:
    crypto.decrypt_file(fileName, extension)
