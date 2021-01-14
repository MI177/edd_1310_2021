class NodoArbol:
    def __init__(self,value,left=None,rigth=None):
        self.data=value
        self.left=left
        self.rigth=rigth

arbol=NodoArbol("R",NodoArbol("C"),NodoArbol("H"))
#("C",None/vacio o Valor nodo izq,None o Valor nodo d)Para agregar hijos dentro del hijo
print(arbol.left.data)
print(arbol.rigth.data)
print(arbol.data)

print("-----------------------------")
arbol2=NodoArbol(4,NodoArbol(3,NodoArbol(2,NodoArbol(2),None)),NodoArbol(5))
print(arbol2.data)
print(arbol2.left.data)
print(arbol2.rigth.data)

