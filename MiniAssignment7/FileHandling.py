file = open("a.txt", "w")

try:
    file.write("New-Delhi is the capital city of India.")

    file = open("a.txt", 'r+')
    words = file.read().split()
    maxLength = 0
    maxLengthWord = ""
    for i in range(len(words)):
        if len(words[i]) > maxLength:
            maxLength = len(words[i])
            maxLengthWord = words[i]

    print(maxLengthWord, " : This is the longest word with length : ", maxLength)

finally:
    file.close()