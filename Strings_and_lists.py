# -*- coding: cp1252 -*-     #Esto permite utilizar caracteres extraños a python
def fun():
    var = raw_input("Inserte el texto: ")
    fr = raw_input("Inicio de la seccion 1: ")
    sc = raw_input("Fin de la seccion 1: ")
    td = raw_input("Inicio de la seccion 2: ")
    ft = raw_input("Fin de la seccion 2: ")
    if fr.isdigit() and sc.isdigit() and td.isdigit() and td.isdigit() and ft.isdigit():
        if float(fr) < float(sc) and float(sc) < float(td) and float(td) < float(ft):
            res1 = var[int(fr):int(sc) + 1]
            res2 = var[int(td):int(ft) + 1]
            print res1 + " " + res2
        else:
            print "Los numeros deben ir en orden ascendente de menor a mayor."
    else:
         print "¡Por favor inserte solo numeros!"

while True:
    fun()
   


               
