import numpy as np
import random
class tabla_hash:
    __lista: np.array
    __M: object
    
    def __init__(self,primoo ,N = 100):
        if primoo:
            self.__M = self.primo(int(N / 0.7)) 
        else:
            self.__M = int(N / 0.7)
        self.__lista = np.ndarray(self.__M, dtype=object)
        
    def metodo_division(self,clave):
        return int(clave) % self.__M 
    
    def metodo_extraccion(self,clave):
        return int(clave[-3:])
    
    def metodo_plegado(self,clave):
        clave_str = str(clave)
        suma = 0
        # Vamos sumando los dígitos en bloques de 2
        for i in range(0, len(clave_str), 2):
            suma += int(clave_str[i:i+2])
        # Retornamos la suma módulo del tamaño de la tabla
        return suma % self.__M
    
    def metodo_cuadrado_medio(self,clave):
        cuadrado = str(int(clave )** 2)
        # Extraemos los dígitos centrales
        mid_index = len(cuadrado) // 2
        if len(cuadrado) > 2:
            resultado = int(cuadrado[mid_index - 1: mid_index + 1])
        else:
            resultado = int(cuadrado)
        return resultado % self.__M
    
    def metodo_alfanumerico(self,clave):
        suma = 0
        for char in str(clave):
            suma += ord(char)  # ord() devuelve el valor ASCII de un carácter
        return suma % self.__M
    
    def insertar(self,clave,metodo):
        cont = 1
        if metodo == 1:
            direccion = self.metodo_division(clave)
        elif metodo == 2:
            direccion = self.metodo_extraccion(clave)
        elif metodo ==3:
            direccion = self.metodo_plegado(clave)
        elif metodo == 4:
            direccion = self.metodo_cuadrado_medio(clave)
        elif metodo == 5:
            direccion = self.metodo_alfanumerico(clave)
        else:
            print("Opcion ingresada incorrecta\n")
            return
        while self.__lista[direccion] is not None and cont != self.__M:
            cont+=1
            direccion = (direccion+1) % self.__M
        if cont != self.__M:
            self.__lista[direccion] = clave
            print(self.__lista[direccion])
            print(f"Comparaciones que ocupó: {cont}")
        else:
            print("Tabla llena")
            
    def buscar(self,clave):
        print("Buscando")
        direccion = self.metodo_division(clave)
        cont = 1
        band = False
        while self.__lista[direccion] is not None  and cont != self.__M:
            if self.__lista[direccion] == clave:
                print(f"el valor: {self.__lista[direccion]} se encontró en {cont} comparaciones\n")
                cont = self.__M
                band = True
            else:
                direccion = (direccion+1) % self.__M
                cont+=1
        if not band:
            print("No se encontró")
            
    def primo(self,x):
        i = 2
        # Verificamos si el número 'x' es primo
        while i < x and x % i != 0:
            i += 1
        
        # Si es primo, devolvemos 'x'
        if i == x:
            return x
        else:
            # Si no es primo, buscamos el siguiente número primo
            return self.primo(x + 1)

if __name__ == '__main__':
    op = int(input("Ingrese una opcion: 1_hash con primo 2_hash sin primo\n"))
    op_metodo = int(input("Elección de la Función de Transformación:\n 1_Division\n 2_Extración\n 3_Plegado\n 4_Cuadrado medio\n 5_Alfanumerico\n"))
    while op!=0:
        if op ==1:
            tabla = tabla_hash(True) #para que sea primo el tamaño
            for _ in range(1,100):
                tabla.insertar(str(random.randint(46000000,46999999)),op_metodo)
            
        elif op==2:
            tabla = tabla_hash(False) #para que no sea primo el tamaño
            for _ in range(1,100):
                tabla.insertar(str(random.randint(46000000,46999999)),op_metodo)
        op = int(input("Ingrese una opcion: 1_hash con primo 2_hash sin primo\n"))
        op_metodo = int(input("Elección de la Función de Transformación:\n 1_Division\n 2_Extración\n 3_Plegado\n 4_Cuadrado medio\n 5_Alfanumerico\n"))