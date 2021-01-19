class NodoArbol:
    def __init__(self,value,left=None,rigth=None):
        self.data=value
        self.left=left
        self.rigth=rigth

class BinarySearchTree:
    def __init__(self):
        self.__root=None

    def insert(self,value):
        #regla 1
        if self.__root==None:#equivalente a: self.__root is None
            self.__root=NodoArbol(value,None,None) #insertando raiz
        #regla 2
        else:
            self.__insert__(self.__root,value)

    def __insert__(self,nodo,value):
        if nodo.data == value:
            print("El dato ya existe, no se ingresa nada")
        elif value < nodo.data:
        #regla 1
            if nodo.left == None: #verificar si el nodo esta vacio
                nodo.left=NodoArbol(value)
        #regla 2
            else:
                self.__insert__(nodo.left,value)
        else:
            if nodo.right==None:
                nodo.right=NodoArbol(value)
            else:
                self.__insert__(nodo.right,value)

    def __recorrido_in(self,nodo):
        print("entrando a inorden")
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=",")
            self.__recorrido_in(nodo.right)

    def transversal(self,format="inorden"):
        if format=="inorden":
            self.__recorrido_in(self.__root)
        elif format=="preorden":
            print("recorrido en pre")
        elif format == "posorden":
            print("posorden")
        else:
            print("Errror, ese formato no existe")
        print("")
    
