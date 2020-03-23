def resivir_datos( ) :
	nombre = "Genaro"
	apellido = "Gonzalez"
	edad = 22
	localidad = "Aragua"
	return (nombre, apellido, edad, localidad)


def imprimir_datos( tupla):
	for i in tupla:
		print (i)

imprimir_datos(resivir_datos())





