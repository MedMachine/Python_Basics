#odd 2k+1
while True:
    a = raw_input("Inserte primer numero: ")
    b = raw_input("Inserte segundo numero: ")
    if a.isdigit() and b.isdigit():
        if int(a) < int(b):
            i = int(a)
            ans = 0
            while i <= int(b):
                if i % 2 == 0:
                    i += 1
                else:
                    ans += i
                    i += 1
            print (ans)

        else:
            print("El primer numero NO debe ser mayor al segundo")
    else:
        print ("Invalido: Solo numeros.")
