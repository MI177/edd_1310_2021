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
            if nodo.right == None:
                nodo.right=NodoArbol(value)
            else:
                self.__insert__(nodo.right,value)

    def __recorrido_in(self,nodo):
        print("entrando a inorden")
        if nodo != None:
            self.__recorrido_in(nodo.left)
            print(nodo.data, end=",")
            self.__recorrido_in(nodo.right)

    def __recorrido_pos(self,nodo):
        if nodo:
            self.__recorrido_pos(nodo.lefth)
            self.__recorrido_pos(nodo.right)
            print(nodo.data,end=",")

    def __recorrido_pre(self,nodo):
        if nodo:
            print(nodo.data,end=",")
            self.__recorrido_pre(nodo.left)
            self.__recorrido_pre(nodo.right)

    def transversal(self,format=""):
        if format=="inorden":
            self.__recorrido_in(self.__root)
        elif format=="preorden":
            print("recorrido en pre")
            self.__recorrido_pre(self.__root)
        elif format == "posorden":
            print("posorden")
            self.__recorrido_pos(self.__root)
        else:
            print("Error, ese formato no existe")
        print("")
    
    def search(self,value):
        if self.__root== None:
            return None
        else:
            return self.__search(self.__root,value)

    def __search(self,nodo,value):
        if nodo == None: #vacio?? caso base de recursividad
            return None
        elif nodo.data == value:#caso base de recursividad
            print("Encontrado")
            return nodo
        elif value < nodo.data:
            print("buscar a la izquierda")
            return self.__search(nodo.left,value)
        else:
            print("Buscar a la derecha")
            return self.__search(nodo.right,value)

    def remove(self,value):
        if self.__root == None:
            print("Nada que eliminar")
        else:
            self.__remove(None,None,self.__root,value)

    def __remove(self,padre_hi,padre_hd,actual,value):
        if actual==None:
            print("Caso base")
            return None
        elif actual.data==value:
            print("Encontrado: ", actual.data)
            #caso 1 hoja
            if actual.left ==None and actual.right ==None:
                if padre_hi != None:
                    padre_hi.left=None
                else:
                    padre_hd.right = None

            #caso 2 con un hijo
            if (actual.left != None and actual.right ==None) or (actual.left == None and actual.right !=None):
                print("es un nodo con un hijo", actual.data)
                if actual.left != None:
                    actual.data=actual.left.data
                    actual.left=None
                else:
                    actual.data=actual.right.data
                    actual.right=None  

            #caso 3 con ambos hijos
            
            
        elif value< actual.data:
            print("Buscar a la izquierda")
            self.__remove(actual,None,actual.left,value)
        else:
            print("Buscar a la derecha")
            self.__remove(actual,None,actual.right,value)
    
        
