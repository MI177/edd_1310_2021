def CRegresiva(n):
    if n>=0:
        print(n)
        CRegresiva(n-1)

def main():
    num=int(input("Ingrese un valor entero positivo: "))
    CRegresiva(num)

main()

print("---------------Ejercicio_3_:c_------------------------------")

from Pila import Stack

def RPila(p,elem):
    p=Stack()
    mitad=p.lenght()/2
    #g=mitad.pop()
    #print(g)
    """for i in range(1,(p.length+1)):
            b=p.pop()
        return p.to_string"""
def mainP():
    num=Stack()
    num.push(1)
    num.push(2)
    num.push(3)
    print(num.to_string())
    """a=0
    c=0
    elem=int(input("Ingresse la cantidad de elementos que quiere en la pila: "))
    while c==elem:
        num=int(input("Ingrese un numero: "))
        a+=num
        c+=1
    print(p.length)"""
mainP()
