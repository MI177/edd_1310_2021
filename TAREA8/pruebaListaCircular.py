from ListaCircular import CircularList

lc=CircularList()
print("Esta vacia?: ", lc.is_empty())

lc.insert(10)
lc.insert(20)
lc.insert(30)
print("Esta vacia?: ", lc.is_empty())

lc.transversal()
