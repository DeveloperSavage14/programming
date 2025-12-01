with open('Greeting.txt', "a+") as file:
    print(file.read())
    file.write(input("")+"\n")
    print(file.read())
