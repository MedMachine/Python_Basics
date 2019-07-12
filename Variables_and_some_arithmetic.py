from math import *
while True:
    leg1 = raw_input("Inserte el lado 1: ")
    leg2 = raw_input("Inserte el lado 2: ")
    if leg1.isdigit() and leg2.isdigit():
        res = float(leg1)**2 + float(leg2)**2
        print res
    else:
        print "Input can only be numbers."
        
