from ListaDoble import DoubleLinkedList
    
l=DoubleLinkedList()
print(f"L esta vacioa? {l.empty()}")
l.append(11)
l.append(21)
l.append(77)
l.append(14)
l.append(29)
l.size()
l.transversal()
print("--------------------")
l.reverse_transversal()

l.remove_from_head(77)
l.size()

l.remove_from_tail(14)
l.size()
l.transversal()

#Nota error: from import/ self.__head=None self is not defined    :'(

