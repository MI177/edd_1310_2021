from Colas import Queue, BoundedPriorityQueue, PriorityQueue

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
"""siguiente=atencion.dequeue()
print(f"Bienvenido sr.{siguiente{'Nombre']}, en que podemos servirle hoy")
print(atencion.to_string())"""

print("Pruebas de las colas con prioridad acotada")

maestres={"prioridad":4,"descripcion":"Mestre","personas":["Juan P","Diego H"]}
ninos={"prioridad":2,"descripcion":"ninos","personas":["Santi H","Angel H"]}
mecanicos={"prioridad":4,"descripcion":"Mecanicos","personas":["Diana T","Maria Z"]}
print("------------------------TAREA--------------------------------")
vigia={"prioridad":4,"descripcion":"Vigiass","personas":["Samuel L","Guillermo D"]}
timonel={"prioridad":4,"descripcion":"Timonel","personas":["Alex O "]}
mujeres={"prioridad":3,"descripcion":"Mujeres","personas":["Daniela J","Luisa Z","Paulina R"]}
tercera={"prioridad":2,"descripcion":"Tercera Edad","personas":["Andrian B","Federico N","Juan G"]}
hombres={"prioridad":3,"descripcion":"Hombres","personas":["Axel T","Carlos Z"]}
ninas={"prioridad":1,"descripcion":"Ninas","personas":["David C","Mario A"]}
capitan={"prioridad":5,"descripcion":"Capitan","personas":["Luffy D."]}

cpa=BoundedPriorityQueue(7)
cpa.enqueue(maestres['prioridad'],maestres)
cpa.enqueue(ninos['prioridad'],ninos)
cpa.enqueue(mecanicos['prioridad'],mecanicos)

cpa.enqueue(vigia['prioridad'],vigia)
cpa.enqueue(timonel['prioridad'],timonel)
cpa.enqueue(mujeres['prioridad'],mujeres)
cpa.enqueue(tercera['prioridad'],tercera)
cpa.enqueue(hombres['prioridad'],hombres)
cpa.enqueue(ninas['prioridad'],ninas)
cpa.enqueue(capitan['prioridad'],capitan)
cpa.to_string()
"""i=int(7)
if cpa.is_empty() == False:
    while True:
        cpa.dequeue
        print("Barco abandonado")
        if(i>=7):
            break
else:
    print("Barco vacio")"""

cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()
cpa.dequeue()

