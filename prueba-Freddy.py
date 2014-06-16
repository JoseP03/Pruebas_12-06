# Freddy Jose Herrera C.I: 21.336.172
import math
print("1 Sumar")
print("2 Restar")
print("2 Multiplicar")
print("4 Dividir")
print("5 Exponente")
print("6 Raiz")
print("0 Salir")
opc= int(raw_input("Seleccione Opcion"))
while opc >0:
   	
    if (opc==1):
        print ("La  Suma es:"+ str(x+y))s
	x=  float(raw_input("Ingrese Numero:\"))
        y=  float(raw_input("Ingrese Numero:\"))
    elif(opc==2):
        print ("La Resta es:"+ str(x-y)) 
        x=  float(raw_input("Ingrese Numero:\"))
        y=  float(raw_input("Ingrese Numero:\"))
	
    elif(opc==3):
        print ("La Multiplicacion es:"+ str(x*y)) 
        x=  float(raw_input("Ingrese Numero:"))
        y=  float(raw_input("Ingrese Numero:"))
    elif(opc==4):
	print ("La Divicion es:"+ str(x/y))
        x=  float(raw_input("Ingrese Numero:"))
        y=  float(raw_input("Ingrese Numero:"))
    elif(opc==5):
        x=  float(raw_input("Ingrese Numero:"))
        y=  int(raw_input("Ingrese Numero:"))
        y=y-1;
        print ("El resultado del Exponente es: "+ str(math.ldexp(x,y)))
    
    elif(opc==6):
        x=  float(raw_input("Ingrese Numero:"))
        print ("El resultado de la raiz es:  "+ str(math.sqrt(x)))

    print("1 Sumar")
    print("2 Restar")
    print("2 Multiplicar")
    print("4 Dividir")
    print("5 Exponente")
    print("6 Raiz")
    print("0 Salir")
    opc= int(raw_input("Seleccione Opcion"))
                
