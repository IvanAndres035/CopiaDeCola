#Clase Cola
class cola:
    __listaCola = []
    __CopiaCola = []
#Metodo insertar que nos servira para insertar los datos
    def Insertar(self, elemento):
        self.__listaCola.append(elemento)
        return True
#Metodo quitar, nos servira para eliminar un elemento de una posicion
    def Quitar(self):
        if self.ColaVacia():
            return False
        else:
            return self.__listaCola.pop(0)
#Metodo ColaVacia, para comprobar si la cola esta vacia o no
    def ColaVacia(self):
        if len(self.__listaCola) == 0:
            return True
        else:
            return False
#Metodo LimpiarCola, para eliminar todos los elementos de la cola
    def LimpiarCola(self):
        self.__listaCola.clear()
#Metodo MostrarFrente, Muestra el elemento de la primera posicion
    def MostrarFrente(self):
        return self.__listaCola[0]
#Metodo MostrarCola, muestta la cantidad de datos que hay en la cola
    def MostrarTamCola(self):
        return len(self.__listaCola)
#Metodo HacerCopia, en este metodo implemento los que es un recorrido para saber cuantos elementos hay en la lista de la cola
    def HacerCopia(self):
# El ciclo For es para hacer un recorrido de la ListaCola para conocer sus elementos
        for x in range(0, len(self.__listaCola)):
#En esta linea se insertan los elementos que estan en la ListaCola, con el .append, para generar la copia.
            self.__CopiaCola.append(self.__listaCola[x])
        print('la cola a copiar es:', self.__CopiaCola)
        print('Su copia es: ',self.__CopiaCola)

cola = cola()
cola.Insertar(7.2)
cola.Insertar(5)
cola.Insertar(6.6)
cola.Insertar(7.3)
cola.Insertar(9)
cola.MostrarTamCola()
print(cola.MostrarTamCola())
#cola.HacerCopia()
#print(cola.MostrarFrente())
print(cola.HacerCopia())