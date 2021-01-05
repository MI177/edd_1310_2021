from Colas import Queue

q1=Queue()
q1.enqueue(3)
q1.enqueue(33)
q1.enqueue(23)
print(q1.to_string())

print("Prueba 2 de cola")
c1={"id":1,"Nombre":"Mario","balance":20.5}
c2={"id":2,"Nombre":"Diana","balance":3456.5}
c3={"id":3,"Nombre":"Bartolo","balance":1000000.0}

atencion=Queue()
atencion.enqueue(c1)
atencion.enqueue(c2)
atencion.enqueue(c3)
print(atencion.to_string())
siguiente=atencion.dequeue()
print(f"Bienvenido sr.{siguiente{'Nombre']}, en que podemos servirle hoy")
print(atencion.to_string())

