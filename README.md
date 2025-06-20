# Intérprete de LIS+Fallas+I/O
#### Andrés Valentino Ferrero

### Estructura de los archivos
- datatypes.py: tiene las definiciones de Omega y de State.
- intexp.py: definición e implementación del módulo de expresiones enteras.
- boolexp.py: definición e implementación del módulo de expresiones booleanas.
- comm.py: definición e implementación del módulo de comandos.
- program_tests.py: testing de 7 programas que abarcan todos los comandos. Para ver cuáles programas se prueban, ver el archivo.
- main.py: auxiliar para probar programas a mano. Simplemente cambiando el prog = AST, se puede ejecutar el intérprete con ese programa.
- correr tests con python3 -m unittest _testfile.py_.
### Aclaraciones
- Elegí implementar este intérprete en Python, ya que es el lenguaje con el que me siento más cómodo.
Implementé LIS+fallas+input/output completo.
- Se asume que el usuario ingresa programas válidos, es decir, ASTs correctamente armados. No me pareció necesario implementar chequeos sobre inputs malformados, ya que hacía más engorroso el código y no era el objetivo del trabajo. Me concentré en el caso positivo. Sin embargo, se hacen algunos chequeos básicos, como en el caso de input, donde se chequea que el usuario ingrese un número entero.
- Definí una abstracción del Omega de LIS, con una clase que tiene 3 atributos:
1. status: Indica si la instancia de Omega es normal (i.e iota_term, iota_out y iota_in), o si es abort (iota_abort)
2. state: Estado _var_ -> Z. Es un diccionario
3. out: Lista que deja reflejada los outputs del lenguaje, similar al teórico. En este caso, no identificamos elementos del tipo iota_in, simplemente le pedimos al usuario que ingrese un valor en el momento de ejecución del programa.
Más detalles sobre esto se pueden ver en un comentario en el archivo datatypes.py
- Con respecto a los estados, el diccionario State comienza siendo vacío, y se va llenando a medida que se van ejecutando los comandos. En el caso de que se cree una variable de intexp que no exista, se agrega al diccionario y se le asigna el valor 0. Esta fue una decisión de diseño que tomé, ante la diferencia que tiene la semántica teórica de LIS, que es un mapeo de todas las variables a Z.
- Definí las funciones de transferencia de control * y + como funciones auxiliares dentro de _comm.py_. A la daga no la definí porque me pareció mejor implementar la lógica de esta función dentro del comando newvar.
- Usé type hinting para que sea más legible el código y para que se pueda ver qué tipo de datos espera cada función.
