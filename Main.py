def wordcount(fileSelected):
    selectedFile = open(fileSelected + ".txt", 'r')
    wordCounter = 0
    for line in selectedFile:
        for i in range(len(line)):
            try:
                if line[i] == " " and line[i + 1] != " ":
                    wordCounter += 1
            except IndexError:
                print("Error")
        wordCounter += 1
    print(wordCounter)

print("0 - Encrypt File")
print("1 - Decrypt File")
print("2 - Exit")

action = int(input("\nSelect an action: "))

while action not in [0, 1, 2]:
    print("Invalid input:", action)
    print("0 - Encrypt File")
    print("1 - Decrypt File")
    print("2 - Word Counter")
    print("3 - Exit")
    action = int(input("What action would you like to perform?"))

fileName = input("Enter .txt File Name: ")
if ".txt" in fileName:
    print("Edit changes to", fileName +".txt?")
    print("0 - Change Name")
    print("1 - Keep Name")

selectedFile = open(fileName + ".txt", 'r')
wordCounter = 0
for line in selectedFile:
    words = line.split(" ")
    print(words)
    if words != ['\n']:
        wordCounter += len(words)
    # for i in range(len(line)):
    #     try:
    #         if line[i] == " " and line[i+1] != " ":
    #             wordCounter += 1
    #     except IndexError:
    #         print("Error")
    # if len(line) != 0:
    #     wordCounter += 1
print(wordCounter)