from ListaCircular import CircularList

lc=CircularList()
print("Esta vacia?: ", lc.is_empty())

lc.insert(10)
lc.insert(20)
lc.insert(30)
lc.insert(40)
lc.insert(45)
lc.insert(50)
print("Esta vacia?: ", lc.is_empty())

lc.transversal()
lc.remove(45)
lc.transversal()


