from ArbolesBinarios import BinarySearchTree

abb=BinarySearchTree()
abb.insert(50)
abb.insert(30)
abb.insert(60)
abb.insert(35)
abb.insert(89)
abb.insert(70)

abb.transversal()
abb.transversal("preorden")
abb.transversal("posorden")
res=abb.search(35)
print(f"El valor es: {res}")
abb.remove(35)
abb.transversal()

