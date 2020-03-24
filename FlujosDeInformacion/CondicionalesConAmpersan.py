a = 5
b = 4
c = 6

if a == b == c:
	print("Todos son iguales")

elif a != b != c:
	print("Todos son diferentes")

elif a <= b >= c:
	print("El valor de B es: " + b)

elif not((a != b) and (a != c)):
	print("El valor de A es: " , a)