class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value
        self.next=siguiente

class CircularList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        
    def is_empty(self):
        return self.__head==None

    def insert(self, value):
        nuevo=Nodo(value)
        if self.is_empty():
            self.__head=nuevo
            self.__tail=nuevo
            self.__tail.next=self.__head
        else:
            curr_node=nuevo
            curr_node.next=self.__head
            self.__head=curr_node
            self.__tail.next=self.__head

    def transversal(self):
        curr_node=self.__head
        while curr_node.next != self.__head:
            print(f" {curr_node.data} -->", end="")
            curr_node=curr_node.next
            #if curr_node==self.__head:
                #break

    #def search
    def remove(self, value):
        if self.is_empty():
            print("La lista se encuentra actualemnte vacia")
        else:
            if self.__head==self.__tail:
                self.__head=None
                self.__tail=None
            else:
                self.__head=self.__head.next
                self.__tail.next=self.__head

