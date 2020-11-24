def get(self,posicion=None): #Por defecto regresa el ultimo
        contador=0
        dato=0
        i=0
        if posicion == None:
            dato=self.tail().data
        else:
            if posicion != None:
                while i <= curr_node:
                    contador=contador+1
                    print("La posicion es "+contador)
        return dato
