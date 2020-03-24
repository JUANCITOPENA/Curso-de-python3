lista = [2,4]
numero = 10

try:
	print(lista[10])
	numero/0
except IndexError, ArithmeticError:
	print("Error en las operaciones")

else:
	print("Hola Else")
finally:
	print("Hola Final")


input()