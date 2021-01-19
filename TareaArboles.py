"""
PARA EL ARBOL 1:

Prefijo: +, -, 5, 4, *, 3, 2
Comienza por la raiz (+) y lee lo que este
a la  izquierda, si dentro de ese nodo hay algun otro valor, lo lee primero
y luego procede a cambiar de lugar. En jerarquia de operaciones la resta se
puede hacer ante o despues de la suma de tal forma que se va a la izquierda
como 5 es mayor que 4 primero lee al 5.

Infijo: 5, -, 4, +, 3, *, 2
Comienza a leerse desde la ultima hoja de lado izquierdo, sigue a la parte
superior, si en el nodo tiene otra hoja al lado derecho la lee y pasa al
siguiente nodo, aplica el mismo  procedimiento y al ultimo lee la raiz.

Posfijo: 5, 4, -, 3, 2, *, +
Lee la ultima hoja del nodo de la izquierda primero, luego lee a su hoja
"hermano" y lee a su padre, despues se pasa al siguiente nodo y aplica el
mismo procedimiento para al ultimo leer la raiz.

PARA EL ARBOL 2:

Prefijo: 40, 30, 25, 35, 50, 45, 60
En este caso comienza con la raiz 40, como 30 es menor que 40 lo posiciona en
el lado izquierdo, 25 es menor que 30 asi que lo posiciona a la izquierda, 35
es mayor que 30 y lo posiciona en el lado derecho de ese nodo, como 50 es mayor
que 40 lo posiciona a la derecha, como 45 es mayor que 40 pero menor que 50 lo
posiciona a la izquierda y como 60 es mayor que 40, 50 y 45 lo posiciona a la
derecha en ese nodo.

Infijo: 25, 30, 35, 40, 45, 50, 60
Comienza con 25, como 30 es mayor que 25 lo posiciona arriba de el, esto
sigue de forma subsecuente hasta terminar de leer a 60 el numero mayor del arbol

Posfijo: 25, 35, 30, 45, 60, 50, 40
Comienza con 25 y continua de tal forma que completa primero el nodo de la
izquierda junto la raiz y finaliza con el nodo derecho.
"""
