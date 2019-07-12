while True:
    fname = raw_input("Nombre del archivo: ") #Variable que equivale al documento
    numlin = 0 #Contador de lineas
    with open(fname,'r') as doc:
        for line in doc:
            if numlin%2 == 0:
                numlin += 1
            else:
                print line.rstrip()
                numlin += 1
                
