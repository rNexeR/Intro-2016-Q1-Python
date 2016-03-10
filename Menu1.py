#DOs numeros ingresados por el usuario
#Sumas, Restar, Dividir, Multiplicar

num1 = input("Ingrese numero1: ");
num2 = input("Ingrese numero2: ");

opcion = 1

while opcion>0 and opcion <= 5:
	print("1- Sumar \n2- Restar\n3- Dividir \n4- Multiplicar\n5- Salir")
	opcion = input("Ingrese opcion: ")
	if(opcion == 1):
		print ("La suma es: " + str(num1+num2))
	elif (opcion == 2):
		print ("La resta es: " + str(num1-num2))
	elif (opcion == 3):
		print ("La division es: " + str(num1/num2))
	elif (opcion == 4):
		print ("La multiplicacion es: " + str(num1*num2))
	elif (opcion ==5):
		print ("Adios")
		break

