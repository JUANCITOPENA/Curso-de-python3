import threading
import time

class Hilo(threading.Thread):
	def run(self):
		print("{} Inicio".format(self.getName))
		time.sleep(1)
		print("{} terminado".format(self.getName()))


if __name__ == "__main__":
	for x in range(9):
		hilo = Hilo(name = "Hilo - {}".format(x + 1))
		hilo.start()
		time.sleep(.5)

input()