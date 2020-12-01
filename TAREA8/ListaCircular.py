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
    """def insert_mayor(self, value):
        nuevo = Node(data) 
        if self.__head == None:            
            self.__head = nuevo
            self.__head.next = nuevo
            self.__tail = nuevo
            return

        if self.end != None:
            self.end.next_node = new_node
            new_node.next_node = self.head        
            self.end = new_node
            return

    def insert_menor(self, data):
        nuevo = Node(data)
        nuevo.next_node = self.__head        
        curr_node = self.__head

        if curr_node == None:            
            self.__head = nuevo
            self.__tail = nuevo
            self.__head.next = nuevo
            return
        
        if self.__tail != None:
            self.__tail.next = nuevo
            nuevo.next_node = self.__head        
            self.__head = nuevo
            return

    def insert_medio(self, value):

        if curr_node == self.__tail:
            self.insert_menor(data)
            return

        nuevo = Node(data)            
        curr_node = curr_node.next        
        curr_node.next = nuevo
        nuevo.next = curr_node.next

    def insert(self, value):
        if nuevo >= self.__head.data:
            inser_mayor()
        else:
            if nuevo >= self.__head.data and nuevo <= self.__tail.data:
                insert_medio()
            else:
                if nuevo<=self.__tail.data:
                    inser_menor()
                    return"""


    def transversal(self):
        curr_node=self.__head
        while curr_node.next != self.__head:
            print(f" {curr_node.data} -->", end="")
            curr_node=curr_node.next
            if curr_node==self.__head:
                break

    def search(self, value):
        curr_node=self.__head
        i=1
        f=False
        if(self.__head == None):
            print("Lista vacia");    
        else:    
            while(True):
                if(curr_node.data ==  value):    
                    f = True;    
                    break;    
                curr_ndde = curr_node.next;    
                i+=1    
                if(curr_node == self.__head):    
                    break;    
            if(f):    
                print("Valor en la posicion :  " + str(i));    
            else:    
                print("El valor no esta en la lista")
                
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
