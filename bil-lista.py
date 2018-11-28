meny = 0
message = ""
delete = 0

while meny !=4: 
    try:
        meny = int(input("tryck på 1 för att skriva ut listan \n tryck på 2 för att skriva i listan \n tryck på 3 för att rensa \n tryck 4 för att avsluta"))
    except:
        print("skriv en siffra")
    if meny == 1: 
        f = open('lista.txt', 'r')
        for line in f: 
            print(line)
        print("")
        f.close()
