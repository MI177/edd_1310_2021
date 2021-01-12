def factorial(n):
    if n==0:
        return 1
    else:
        return factorial(n-1)*n

def printRev(n):
    if n>0:
        #print(n)
        printRev(n-1)#Llamada recursiva
        print(n)

        """
        Inicia llamando/evaluando a 3 se resuellve ahora
        evalua a 2 se resuelve
        evalua a 1 se resuelve todo
        por lo que imprime n regresa e imprime,
        regresa imprime termina la funcion
        y finaliza el programa"""

def fibonacci(n):
    if  n==1 or n==0:
        return n
    if n>1:
        return (fibonacci(n-1)+fibonacci(n-2))

def main():
    for num in range (1,11,1):
        r=factorial(num)
        print(f"El factorial de {num} es {r}")

def main2():
    printRev(3)

def main3():
    for num in range(11):
        print(str(fibonacci(num))+",",end="")
    print("")

#main()
#main2()
main3()
