with open("./targetFolder/file.txt", "rb") as file:
    while True:
        charByte = ' '.join(format(x, 'b') for x in file.read(1))
        if charByte == '':
            break
        print(charByte)
