class SetFileName:
    global extension
    global fileName

    @staticmethod
    def getExtension():
        return extension

    @staticmethod
    def getFileName():
        return fileName

    @staticmethod
    def fileNamer():
        global fileName
        global extension
        fileName = input("Enter .txt/.enc File Name: ")

        if ".txt" == fileName[len(fileName) - 4:len(fileName)]:  # Removes .txt extension if user adds it
            fileName = fileName[0:len(fileName) - 4]
            extension = '.txt'
        elif ".enc" == fileName[len(fileName) - 4:len(fileName)]:  # Removes .txt extension if user adds it
            fileName = fileName[0:len(fileName) - 4]
            extension = '.enc'
        else:
            print("'.txt' - .txt File")
            print("'.enc' - .enc File")
            extension = input("Extension Type: ")
            while extension not in ['.txt', '.enc']:  # If input is invalid
                print("Invalid input:", extension)
                print("'.txt' - .txt File")
                print("'.enc' - .enc File")
                extension = input("Extension Type: ")

        try:
            test = open(fileName + extension)
            test.close()
        except FileNotFoundError:
            print("File not found. Make sure that the File is in the same folder as this program.")
            fileNamer()
