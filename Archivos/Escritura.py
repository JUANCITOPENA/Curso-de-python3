def file_write():
	archivo = open("Archive.gg", "a")
	archivo.write("Este es mi primer archivo en python")
	archivo.write("\nGenaroGG")
	archivo.close()

file_write()