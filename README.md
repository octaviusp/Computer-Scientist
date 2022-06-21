# Computer-Scientist

## Computer science aprendizaje resumido:


### - Notacion N:
Se utiliza para determinar la escalabilidad y velocidad de un algoritmo.
N = Cantidad de datos
F(N) = Operaciones/Pasos
Tipos => 

### Constante

(en el grafico es una recta con pendiente 0, osea y = K, con K constante) => implica que el algoritmo funciona igual ya sea para N = 1 o N tendiendo a infinito
-----------------------------------------------
###### Log N => 
-implica que el algoritmo tiene muy buena escalabilidad, de hecho es la mejor que podriamos encontrar.
Ya que el logaritmo es => Log N en base 2 = Z, donde 2 ^ Z = N, la base del logaritmo es 2 siempre por la computacion
es decir el sistema binario que entiende la computadora.
Y el logaritmo implica que =>
Cantidad de data          Pasos para resolver
	2^n			Log2 (N) =
	2^4 = 16		   4
	2^5 = 32		   5
	...			  ...

-----------------------------------------------
######Raiz(n) 
- similar al logaritmo pero escala mas rapido, es bastante optimo un algoritmo asi tambien.
-----------------------------------------------
######N
-(Linea recta con pendiente = 1, de la forma y = x, ordenada 0) => Significa que para N cantidad  de data => N pasos
No es muy eficiente, pero mejor que otros es. Linear search
-----------------------------------------------
######N.log(n) -
- (hiperbola)=> La mayoria de algoritmos tienen esta escalabilidad
es aceptable. Merge sort, quick sort
-----------------------------------------------
###### n ^ 2 
-(parabola ineficiente pero mejor que los siguientes) = Bubble sort, insertion sort, selection sort.
-----------------------------------------------
###### 2^n
- (parabola muy ineficiente)
-----------------------------------------------
###### n! 
- (El peor de todos) demasiado ineficiente
-----------------------------------------------

### - Big O Notation =>
######- Forma rapida y accesible para determinar escalabilidad de un algoritmo propuesto

- X => F(x) / F(x) pertenece a las funciones anteriormente mencionadas.

o(x) (O chica) => Mas rapido que X (Suele utilizarse poco ya que no comunica un limite de eficiencia, es medio impreciso)
O(x) (O grande) => Igual o mas rapido que X (El mas utilizado, ya que como el peor de los casos es igual a X, por lo tanto
te impone un limite y sabrás cual es el punto MAXIMO de escalabilidad, punto muy importante, te otorga una vision a futuro)
0(x) (Theta) => Exactamente Igual a X
OMEGA(x) (OMEGA Grande) => Igual o peor que X
omega(x) (omega pequeño) => peor que X

------------------------------------------------

###### Array circular => 
- Array que tiene longitud fija y una vez lleno "circula" para ir metiendo los nuevos elementos,
Tiene un puntero seleccionando las principales posiciones front y back, cuando se modifica estos se modifican tambien.
(Ejemplos de vida real, un inventario limitado en un juego)

Ejemplo => [-,-,5,3,2]

Tiene un front (elemento principal)
Tiene un back (ultimo elemendo añadido al array)
Siempre se inserta un elemento al final, osea en el back.

Front = 5 - Back = 2, si añado un elemento generico llamado X => [X,-,5,3,2]
ahora X sera el back.
Si añado otro generico Y => [X,Y,5,3,2], ahora Y sera el back.

Si elimino el front, este pasara al elemento siguiente.
Si elimino el back, este pasara al elemento anterior.
#####------ CUIDADO con estas dos cosas, porque podria pasar => [-,-,5,-,2], si elimino el 5 el front no ira indice+1 ya que le daria
#####el front a un elemento vacio, deberia darle el puntero front al 2, y como hacemos eso? iterando hasta encontrar el siguiente numero
#####distinto de vacio.

------------------------------------------------

##### Array dinamico, como funciona un array dinamico?
Bien, se divide en 2 partes
Tamaño logico, tamaño fisico.
Tamaño logico => tamaño de la cantidad de elementos ACTUALES adentro del array
Tamaño fisico => tamaño en total de los elemtnos del array, no importa si estan vacio
Ejemplo => [5,9, -, -,3] , tamaño logico = 3, tamaño fisico = 5

Como funciona un array dinamico por abajo ?
Bien , una vez el tamaño logico == tamaño fisico , el compilador DUPLICA el tamaño fisico.
osea si tenemos [5,3,-] => tamaño fisico = 3, tamaño logico = 2, luego => [5,3,1] tamaño logico == tamaño fisico por lo tanto
=> Duplicar array => [5,3,1,-,-,-]
------------------------------------------------

##### ESTRUCTURAS DE DATOS IMPORTANTES >=

[ TODAS LAS LISTAS TIENEN UN HEAD, ES UN NODO PRINCIPAL, UN PUNTERO QUE APUNTA A ESTE NODO]

##### -- LISTAS ENLAZADAS 
{
LISTAS SIMPLEMENTE ENLAZADAS => NODOS UNIDOS CON UN PUNTERO SIGUIENTE QUE APUNTA AL NODO SIGUIENTE, EL NODO INICIAL SE LLAMA
GENESIS. EL ULTIMO NODO SIEMPRE APUNTARÁ A NULL (SERIA LO CORRECTO).

LISTAS DOBLEMENTE ENLAZADAS SIN TAIL POINTER => NODOS UNIDOS CON 2 PUNTEROS, 1 PARA NODO SIG Y OTRO NODO PREVIO,
EL NODO INICIAL TIENE PUNTERO PREVIO NULL! (CON ESTO NOS PODRIAMOS DAR CUENTA SI ES EL PRIMERO O COMPARANDO A HEAD)
ES MAS OPTIMO QUE LA LISTA SIMPLEMENTE ENLAZADA YA QUE PODRIAMOS REOCRRER Y ELIMINAR ELEMENTOS MAS RAPIDO, AL TENER
BIDIRECCION ES MAS RAPIDO TODO!

LISTAS DOBLEMENTE ENLAZADAS CON TAIL POINTER => IDEM LISTA ANTERIOR PERO CON PUNTERO INDICANDO CUAL ES EL ULTIMO NODO!
ESTO FACILITA AÑADIR NUEVOS NODOS, OSEA INSERCION DE NODOS. LO HAREMOS EN TIEMPO CONSTANTE.

- LAS LISTAS QUE NO TIENEN TAIL POINTER INSERTAR O ELIMINAR ELEMENTOS(en el back) LO HARAN EN 0(N)
- LAS LISTAS QUE NO TIENEN BIDIRECCION REMOVERAN ELEMENTOS RANDOM EN 0(N)
}

#####-- STACKS 
{

ESTRUCTURA DE DATO QUE ES UNA PILA, COMO UNA PILA DE LIBROS,
AMONTONAS TODOS Y PODES SACAR EL ULTIMO, LUEGO EL ANTEULTIMO Y ASI HASTA EL PRIMERO
ES LIFO, LAST INPUT FIRST OUTPUT.
	
}

#####-- QUEUES 
{

ESTRUCTURA DE DATO QUE ES UNA COLA, COMO UNA COLA DE UN SUPERMERCADO O PARA PAGAR UN SERVICIO,
EL PRIMERO QUE LLEGA ES EL PRIMERO QUE SALE, ES FIFO, FIRST INPUT FIRST OUTPUT.

}

#####-- ARBOLES 
{

ESTRUCTURA DE DATOS COMO GRAFOS PERO CON ORDEN DE JERARQUIA, TIENE UN ROOT O NODO PRINCIPAL QUE ES LA RAIZ,
DE ESTE DERIVAN TODOS LOS HIJOS, TAMBIEN TIENE HOJAS, QUE SON LOS NODOS SIN HIJOS.
TIENEN ALTURA O HEIGHT = CANTIDAD DE NIVELES O ALTURA HACIA ABAJO


- ARBOLES BINARIOS {
ARBOLES CON MAXIMO 2 HIJOS, EL IZQUIERDO ES MAS PEQUEÑO QUE EL DATO ADENTRO DEL NODO, EL DERECHO MAS GRANDE.
ESTO SIMPLIFICA LAS BUSQUEDAS => SEARCH = INSERT = DELETE = O(LOG N)

- TIENEN ALGORITMOS DE RECORRIDO O TRANVERSALS =>
L = LEFT NODE, R = RIGHT NODE, P = PARENT NODE
POST ORDER => LRP
IN ORDER => LPR
PRE ORDER => PLR

- HAY ARBOLES MAS AVANZADOS (VER LUEGO)
- AVL TREE, RED AND BLACK TREE


}

##### - HEAPS 
{
CASO ESPECIAL DE ARBOLES, EL NODO PADRE SIEMPRE ES > A LOS HIJOS.
POR LO TANTO ESTO CREARIA UNA JERARQUIA DEL NODO MAS REPRESENTATIVO
ARRIBA D ETODO, LLEGANDO HASTA LA RAIZ O ROOT.

CADA VEZ QUE SE INSERTA UN NUEVO NODO MAYOR, DBERIAMOS METERLO AL NODO PADRE,
INSERTANDO EN LOG(N) RUNTIME.

PARA QUE EL TREE O ARBOL ESTE COMPLETO DEBE SER BINARIO
OSEA TENER MAXIMO 2 HIJOS Y SI TIENE 1 ESTE TIENE QUE ESTAR EDL LADO IZQUIERDO.

RUN TIMES:
INSERT O(LOG N)
DELETE O(LOG N)
GETMAXNODE O(1) YA QUE SIEMPRE SERA EL ROOT.
}

#####- GRAPHS O GRAFOS:

UN GRAFO ES UN CONJUNTO DE NODOS UNIDOS POR ARISTAS,
LOS NODOS LLAMADOS VERTICES Y LAS ARISTAS.
UN GRAFO ES ADYACENTE A OTRO CUANDO TIENE UNA ARISTA QUE LO UNA.
EXISTEN LA MATRIZ DE ADYACENCIA, VER EN VIDEOS DE HERNAN.
Y TIENEN PROPIEDADES INTERESANTES.
ADEMÁS POSEEN ALGORITMOS COMO DIJKSTRA(ENCONTRAR LA RUTA MINIMA VIABLE)

EXISTEN =>
- GRAFOS DIRECCIONALES : POSEEN DIRECCION, PUEDE SER BIDIRECCIONAL O UNIDIRECCIONAL
- GRAFOS SIMPLES : POSEEN ARISTAS EN DOBLE SENTIDO
- GRAFOS WEIGHTED O CON PESO: GRAFOS SIMPLES O DIRECCIONALES QUE POSEEN PESOS EN LAS ARISTAS,
ESTOS PUEDEN SER KM PARA LLEGAR A LA OTRA CIUDAD, O COSTE DE UNA MATERIA PRIMA.

SON MUY UTILIZADOS.
