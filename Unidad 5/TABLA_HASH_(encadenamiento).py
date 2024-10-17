import numpy as np
import random
class Nodo:
	__siguiente: object
	__clave: object

	def __init__(self, clave):
		self.__siguiente = None
		self.__clave = clave

	def get_siguiente(self):
		return self.__siguiente

	def get_clave(self):
		return self.__clave

	def set_siguiente(self, sig):
		self.__siguiente=sig

class Tabla_hash():
	__lista: np.ndarray
	__tamanio: int
	__colisiones: list

	def __init__(self, N=100, M=5):
		self.__tamanio = int(N/M)
		self.__colisiones=np.zeros(self.__tamanio, dtype=int)
		self.__lista = np.ndarray(self.__tamanio, dtype=object)

	def metodo_plegado(self, clave):
		clave_str = str(clave)
		suma=0
		for i in range(0, len(clave_str), 2):
			suma += int(clave_str[i:i+2])
		return suma % self.__tamanio

	def insertar(self, clave):
		direccion = self.metodo_plegado(clave)
		nodo = Nodo(clave)
		if self.__lista[direccion] is None:
			nodo.set_siguiente(None)
			self.__lista[direccion] = nodo
			print(f"Se inserto la clave '{clave}'.")
		else:
			aux = self.__lista[direccion]
			while aux.get_siguiente() is not None and aux.get_clave() != clave:
				aux = aux.get_siguiente()
			if aux.get_siguiente() is None:
				self.__colisiones[direccion]+=1
				aux.set_siguiente(nodo)
				print(f"Se inserto la clave '{clave}', hay {self.__colisiones[direccion]} claves colisionadas.")
			else: 
				print("Clave ya ingresada.")

	def buscar(self, clave):
		direccion = self.metodo_plegado(clave)
		cont=1
		if self.__lista[direccion] is not None:
			aux = self.__lista[direccion]
			while aux.get_siguiente() is not None and aux.get_clave() != clave:
				aux = aux.get_siguiente()
				cont+=1
			if aux.get_clave() == clave:
				print(f"Se ha encontrado la clave '{aux.get_clave()}', en {cont} intentos.'")
			else:
				print("Elemento no encontrado.")
		else: 
			print("Error.")

	def promedio_colisiones(self):
		suma=0
		for i in range(len(self.__colisiones)):
			suma += self.__colisiones[i]
		promedio=suma/self.__tamanio
		return promedio

if __name__ == '__main__':
	tabla = Tabla_hash()
	tabla.insertar('45635882')
	tabla.insertar('45635883')

	claves=[]
	for _ in range(100):
		claves.append(random.randint(45000000, 45999999))

	for clave in claves:
		tabla.insertar(clave)

	tabla.insertar('45635882')
	tabla.buscar('45635882')
	print(f"Promedio: {tabla.promedio_colisiones()}")