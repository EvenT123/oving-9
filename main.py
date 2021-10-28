
with open("sporsmaalsfil.txt", "r" , encoding="UTF8") as file:
    for line in file:
        SpmEnd = line.find(":")
        print(line[:SpmEnd])