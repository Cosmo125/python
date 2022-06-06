class coche():
	def __init__(self):
		self.largoChasis=250
		self.anchoChais=120
		self.__rudas=4
		self.enmarcha=False


	def	arrancar(self,arrancamos):
		self.enmarcha=arrancamos
		if(self.enmarcha):
			chequeo=self.__chequeoInterno()
  
		if(self.enmarcha and chequeo):
			return "el coche essta en marcha"
		
		elif(self.enmarcha and chequeo==False):
			return "Algo anda mal en el chequeo. revise nuevamente"
		else:
			return "el coche esta etenido"
  		
	def estado(self):
		print("el coche tiene ",self.__rudas,"ruedas un ancho de ",self.anchoChais,'y un largo de ', self.largoChasis)

	def __chequeoInterno(self):
		print("Realizando chequeo interno")

		self.gasolina="ok"
		self.aceite="ok"
		self.puerta="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puerta=="cerradas"):
			return True	
		else:
			return False	
  
miCoche=coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("----------------a continuacion creamos el segundo objeto--------------------")

miCoche2=coche()
print(miCoche2.arrancar(False))
miCoche2.estado()