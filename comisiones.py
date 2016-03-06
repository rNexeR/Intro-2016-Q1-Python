empleado = raw_input("Ingrese nombre del empleado: ")
ventas = input("Ingrese total de ventas: ")
zona = raw_input("Ingrese zona: ")

if zona == "a":
	comision = ventas * 0.15
elif zona == "b":
	comision = ventas*0.10
elif zona == "c":
	comision = ventas * 0.05
else:
	comision = 0

rap = comision*0.035
total = comision - rap

print("Nombre: " + empleado + "\nComision: " + str(comision) + "\nRAP: " + str(rap) + "\nTotal: " + str(total))