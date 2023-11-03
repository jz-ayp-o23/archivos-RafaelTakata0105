file = open("beatles.txt", "r", encoding = "utf8")
for linea in file:
    print(linea)
file.close()
