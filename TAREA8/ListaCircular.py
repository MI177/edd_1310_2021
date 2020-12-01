class Nodo:
    def __init__(self, value, siguiente=None):
        self.data=value
        self.next=siguiente

class CircularList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        self.__size=0
        
    def is_empty(self):
        return self.__size==0

    def insert(self, value):
        nuevo=Nodo(value)
        if (self.__head==None):
            self.__head=nuevo
            curr_node=self.__tail
                
        else:
            curr_node=self.__head
            while curr_node.next!=None:
                curr_node=curr_node.next
            curr_node.next=nuevo#pendiente

    def transversal(self):
        curr_node=self.__head
        while curr_node.next != None:
            print(f" {curr_node.data} -->", end="")
            curr_node=curr_node.next
        print("")
