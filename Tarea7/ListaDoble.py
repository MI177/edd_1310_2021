class NodoDoble:
    def __init__(self, value, siguiente=None, anterior=None):
        self.data=value
        self.next=siguiente
        self.prev=anterior

class DoubleLinkedList:
    self.__head=None
    self.__tail=None
    self.__size=0

    def empty(self):
        return self.__head==None

    
    def get_size(self, value):
        value=self.__size
        if value==None:
            print("Lista vacia")
        else:
            return value

    def append(self, value):
        if self.__head():
            self.__head=self.__tail=NodoDoble(value)
        else:
            curr_node= self.__tail
            self.__tail=curr_node.next=NodoDoble(value)
            self.__tail.prev=curr_node
        self.__size += 1
        
    def remove_from_head(self):
        if self.empty():
            print("La lista esta vacia")
        else:
            if self.__head.next==None:
                self.__head=self.__tail=None
                self.size=0
            else:
                self.__head=self.__head.next
                self.__head.prev=None
                self.__size-=1

    def remove_from_tail(self):
        if self.empty():
            print("La lista esta vacia")
        else:
            if self.__head.next==None:
                self.__head=self.__tail=None
                self.__size=0
            else:
                self.__tail=self.__tail.prev
                self.__tail.next=None
                self.__size-=1

        
    def transversal(self):
        curr_node=self.__head
        while curr_node:
            print(curr_node.value)
            curr_node=curr_node.next

    def reverse_transversal(self):
        curr_node=self.__tail
        while curr_node:
            print(curr_node.data)
            curr_node=curr_node.prev


