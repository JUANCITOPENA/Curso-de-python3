def file_reader():
	archivo = open("Archive.gg","r")
	linea = archivo.readline()

	while linea != "":
		print(linea)
		linea = archivo.readline()

	archivo.close()

file_reader()

input()