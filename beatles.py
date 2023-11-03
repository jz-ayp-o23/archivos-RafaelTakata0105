file = open("beatles.txt", "r", encoding = "utf8")
for line in file:
    print(line.strip())
file.close()
