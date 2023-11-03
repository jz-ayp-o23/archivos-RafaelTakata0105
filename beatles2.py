file = open("beatles.txt", "r", encoding = "utf8")
for linea in file:
    for caracter in linea:
        print(repr(caracter), end =" ")
    print()
file.close()