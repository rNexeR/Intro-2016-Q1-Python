nombre = raw_input("Ingrese nombre: ")
cant = input("Ingrese cantidad de platos: ")
precio = input("Ingrese precio por unidad: ")
tipo = input("Llevar [1] o Comer [0]")
tedad = input("Es tercera edad? [1 Si] [0 No]: ")
embarazada = input("Es embarazada? [1 Si] [0 No]: ")
disca = input("Es discapacitada? [1 Si] [0 No]: ")

subtotal = cant*precio

if tipo == 1:
	subtotal = subtotal + cant*5

descuento = 0

if tedad == 1:
	descuento += 0.1
if embarazada == 1:
	descuento += 0.1
if disca == 1:
	descuento += 0.1

descuento = descuento*subtotal

total = subtotal - descuento