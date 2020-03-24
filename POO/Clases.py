class Persona:
	edad = 0
	programa = False
	nombre = ""
	apellido = ""

	def __init__(self, nombre, apellido, edad, programa):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.programa = programa

	def __str__(self):
		return "Mi nombre es " + self.nombre + " " + self.apellido + " " + str(self.edad)




class Programador:
	def __init__(self, lenguaje1, lenguaje2):
		self.lenguaje1 = lenguaje1
		self.lenguaje2 = lenguaje2


	def python(self):
		print("Se programar en Python")

	def java(self):
		print("Se programar en java") 

class Genaro(Persona, Programador):

	def saludar(self):
		print("Hola")


genaro = Genaro("Genaro", "Gonzalez", 22, True)

print(genaro)

genaro.python()
genaro.java()

input()
