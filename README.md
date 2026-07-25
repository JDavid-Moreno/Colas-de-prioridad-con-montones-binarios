# Colas de prioridad usando montones binarios

Una cola de prioridad es una [Estructura de datos lineal](https://github.com/JDavid-Moreno/Estructuras-Lineales), está basada en una cola convencional, con la diferencia de que esta utiliza un valor de **prioridad**, por lo que el primer elemento en salir es aquel que tenga la mayor o menor (depende el caso y que se pida) prioridad, sin importar el orden de llegada, en caso de que 2 elementos tengan la misma prioridad, se definirá por quien primero (principio FIFO de las colas).

Este tema se abordó de manera superficial anteriormente, con la diferencia de que ahora usaremos un monton binario para hacerlo de manera completa.

## Monto binario

Un monto binario es un [arbol binario](https://github.com/JDavid-Moreno/Arboles-Binarios) completo que cumple una propiedad de orden, por lo que a diferencia de los árboles binarios normales, estos funcionan con otras reglas. Asi mismo, existen 2 tipos de montones binarios:

### Max Heap

El padre siempre es mayor o igual que sus hijos, asi mismo, el valor máximo se encuentra en la raiz:

![MaxHeap.jpeg](Recursos/MaxHeap.jpeg)

### Min Heap

El padre siempre es menor o igual que sus hijos, asi mismo, el valor minimo se encuentra en la raiz:

![MinHeap.jpeg](Recursos/MinHeap.jpeg)

---

Se utiliza un Heap, ya que una cola de prioridad necesita obtener y eliminar el elemento más prioritario lo más rapido posible. Por ejemplo, si queremos obtener el maximo de una lista normal costaria $O(n)$, mientras que con un heap sería de $O(1)$ para consultarlo al estar en la raiz.

Asi mismo, este debe cumplir una serie de reglas para funcionar correctamente, primero este debe ser un arbol completo o casi completo (todos los niveles del arbol deben estar completos excepto quizás el último, el cual se llena de izquierda a derecha).

![Valido-E-Invalido.jpeg](Recursos/Valido-E-Invalido.jpeg)

Estas normas hacen que un heap no sea un arbol binario convencional, ya que al no haber un orden izquierda/derecha de hermanos, solo la relación padre-hijo importa. Por lo cual, buscar un elemento cualquiera en un heap es $O(n)$, no $O(log(n))$.

---

## Representación como un arreglo

Aquí el heap no se guarda como nodos, sino que se guarda como una lista, por lo que un arbol como este:

![Ejemplo.jpeg](Recursos/Ejemplo.jpeg)

Se puede representar como: `[100, 50, 80, 20, 30, 40]`

Este arreglo representa cada elemento nivel por nivel, primero la raiz (nivel 0), luego sus hijos (nivel 1), luego los hijos de esos hijos (nivel 2), y asi sucesivamente.

Por lo que, gracias a esta estructura, tenemos unas fórmulas que nos ayudan a conocer las posiciones de casi cualquier nodo, suponiendo que un nodo está en la posición `i` entonces:

* **Encontrar el padre**: estará en la posición `(i - 1) // 2`
* **Encontrar el hijo izquierdo**: estará en la posición `(2 * i) + 1`
* **Encontrar el hijo derecho**: estará en la posición `(2 * i) + 2`

### Operaciones

