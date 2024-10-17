import numpy as np
import random
class Tabla_hash():
    __primaria: np.ndarray
    __tamanio: int
    __capacidad_buckets: int
    __contadores: np.ndarray
    __overflow: np.ndarray
    
    def __init__(self, tamanio=1000, registros=4):
        self.__capacidad_buckets = registros
        self.__dir_overflow = int((tamanio//registros))
        self.__tamanio = (tamanio//registros) + int((tamanio//registros)*0.20)
        self.__contadores = np.zeros(self.__tamanio, dtype = int)
        #tabla primaria
        self.__primaria = np.zeros((self.__tamanio, self.__capacidad_buckets), dtype = object)
    
    def hash(self, clave):
        return int(clave[-2:])
    
    def insertar(self, clave):
        direccion = self.hash(clave)
        if self.__contadores[direccion] < self.__capacidad_buckets:
            self.__primaria[direccion][self.__contadores[direccion]] = clave
            self.__contadores[direccion] += 1
            print(f"Se inserto la clave '{clave}' en el bucket '{direccion}'.")
        else:
            aux = self.__dir_overflow 
            while self.__contadores[aux] >= self.__capacidad_buckets and aux < self.__tamanio-1:
                aux+=1
            if aux < self.__tamanio-1:
                self.__primaria[aux][self.__contadores[aux]] = clave
                self.__contadores[aux] += 1
                print(f"Se inserto la clave '{clave}' en el area de overflow.")

    def busqueda(self, clave):
        direccion = self.hash(clave)
        comparaciones = 0        
        bucket = self.__primaria[direccion]
        encontrado = False
        i = 0
        while i < len(bucket) and not encontrado:
            comparaciones += 1
            if bucket[i] == clave:
                encontrado = True
                print(f"Se encontro la clave '{clave}' en el bucket '{direccion}', con '{comparaciones}' comparaciones.")
            i+=1
        if not encontrado:
            aux = self.__dir_overflow
            while aux < self.__tamanio - 1 and not encontrado:
                j = 0
                bucket_desborde = self.__primaria[aux]
                while j < self.__capacidad_buckets and not encontrado:
                    comparaciones += 1
                    if bucket_desborde[j] == clave:
                        print(f"Se encontro la clave '{clave}' en el area de overflow, con '{comparaciones}' comparaciones.")
                    j += 1
                aux += 1

    def desbordados(self):
        desbordados = overflow = 0
        aux = self.__dir_overflow
        for i in range(len(self.__contadores)):
            if self.__contadores[i] == self.__capacidad_buckets:
                desbordados += 1
                if i>=aux:
                    overflow += 1
                    aux += 1 
        print(f"Cantidad de buckets desbordados: {desbordados}, en overflow {overflow}")
    
    def subocupados(self):
        subocupados = 0
        for i in range(len(self.__contadores)):
            if self.__contadores[i] < int(self.__capacidad_buckets / 3):
                subocupados += 1
        print(f"Cantidad de buckets subocupado: {subocupados}")  
    
    def otros(self):
        cont = 0
        for num in self.__contadores:
            if num < self.__capacidad_buckets and num > int(self.__capacidad_buckets / 3):
                cont += 1
        print(f"Buckets que no estan subocupados ni desbordados: {cont}")
        
if __name__ == '__main__':
    tabla=Tabla_hash()
    claves = []
    for _ in range(200):
        clave_random = str(random.randint(45000000, 45999999))
        tabla.insertar(clave_random)
    tabla.insertar('45635882')
    for _ in range(799):
        clave_random = str(random.randint(45000000, 45999999))
        tabla.insertar(clave_random)
        
    print("-----------")
    tabla.busqueda('45635882')

    tabla.desbordados()
    tabla.subocupados()
    tabla.otros()         