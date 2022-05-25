# Curso-de-Python-Intermedio-Comprehensions-Lambdas-y-Manejo-de-Errores

# 1. Preparación antes de empezar

---

## Zen de Python

En la consola: import this

## Documentación de Python

La puedes encontrar en español:

[docs.python.org/es/3](http://docs.python.org/es/3) 

# 2. Entorno virtual

---

## ¿Qué es un entorno virtual?

Un Python aislado para cada proyecto, en el que puedes controlar las versiones y módulos instalados. Los módulos jamás se deben instalar en global, si no en entornos virtuales. Lo que pase dentro del virtual environment no afectará al Python global.

## El primer paso profesional: creación de un entorno virtual

- **code .** — abre VSCode en la carpeta que estás
1. Como buena práctica, inicializa la carpeta de tu proyecto como un entorno de Git.
    - **git init** — inicializa el repo
2. Crea el entorno virtual con:
    - **py -m venv venv** — en Python, llama al módulo venv (virtual environment) y guárdalo en la carpeta "venv".
3. Activa el venv para que la computadora trabaje con ese y no con el global:
    - **.\venv\Scripts\activate** — activa el venv y aparecerá un: "(venv)" en el inicio de cada línea de la terminal.
    - **alias avenv=.\venv\Scripts\activate** — en la terminal crea un shortcode para activar el venv de una manera más rápida, esto solo funciona con Cmder y queda guardado para siempre. La próxima solo deberás digitar: **avenv**
    - **deactivate** — desactiva el venv (desaparece el "(venv)").
4. Una buena práctica es ignorar el venv en el repositorio:
    - Crea un archivo en la carpeta principal llamado **.gitignore** y dentro pon: **venv/** y guárdalo. Notarás que ahora el nombre de la carpeta está en gris en VSCode.

## Instalación de dependencias con pip

PIP → Package Installer for Python

PIP instala módulos que no vienen dentro de Python. Por ejemplo:

- Requests y BeautifulSoup4 → sirven para webscraping
- Pandas y Numpy → se usan en data science para los datos
- Pytest → sirve para realizar testing

### Comandos de pip

PIP tiene que ser usada de la mano con venv y no debería ser usado fuera del mismo, porque va a instalar los módulos con pip solo dentro del proyecto.

- **pip freeze** — te muestra los módulos que tienes instalados en tu entorno virtual.
- **pip install pandas** — (pandas es el nombre del módulo) instala el módulo en el venv y ya lo puedes usar en cualquier archivo py dentro del venv. Pandas es un módulo que usa otros módulos para funcionar así que los instalará también.

*¿Qué pasa si quieres compartir tu proyecto?* Necesitas que los otros desarrolladores lo usen con exactamente las mismas dependencias y módulos.

- **pip freeze > requirements.txt** — este comando guarda todos tus módulos en su versión actual en un nuevo archivo dentro de la carpeta, llamado requirements.txt. Puedes verlo con **cat requirements.txt**.
- **pip install -r requirements.txt**  — instala todos los módulos dentro de requirements.txt (esto debe ejecutarlo la desarrolladora a la que le compartiste el proyecto)

## Una alternativa: Anaconda

Anaconda está desarrollado especialmente para data science, de hecho es la manera correcta de hacerlo en dicho campo. Es una distribución especial de Python que permite crear un venv e instalar dependencias, pero de manera gráfica.

[https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)

Clase para ver el proceso: [https://platzi.com/clases/2255-python-intermedio/36461-una-alternativa-anaconda/](https://platzi.com/clases/2255-python-intermedio/36461-una-alternativa-anaconda/)

# 3. Alternativa a los ciclos: comprehensions

---

## Listas y diccionarios anidados

Los diccionarios pueden almacenar listas y las listas pueden almacenar diccionarios.

```python
def run():
    my_list = [1, 'Hello', True, 4.5]
    my_dic = {'fistname': 'Tony', 'lastname': 'Manotoa'}

    super_list = [
        {'fistname': 'Tony', 'lastname': 'Manotoa'},
        {'fistname': 'Angie', 'lastname': 'Paladines'},
        {'fistname': 'Max', 'lastname': 'Medina'},
        {'fistname': 'Jandry', 'lastname': 'Camacho'},
        {'fistname': 'David', 'lastname': 'Beckam'}
    ]

    super_dic = {
        'natural_nums': [1, 2, 3, 4, 5],
        'integer_num': [-1, -2, 0, 1, 2],
        'float_nums': [1.1, 4.5, 6.43]
    }

    for key, value in super_dic.items(): # con .items() imprimes tanto el value como la key
        print(key, '-', value)

    print('\n' + '*' * 50 + '\n')

    for dicts in super_list:
        for key, value in dicts.items():
            print(f'{key} - {value}')
        print('-' * 50)
    
    print(my_list, my_dic)

if __name__ == '__main__':
    run()
```

## List comprehensions

A una lista puedes añadirle elementos con un ciclo for y un filtro condicional en una sola línea:

```python
natural_numbers = [i**2 for i in range(1, 101) if i % 3 != 0]
```

**Estructura:**

`[element for element in iterable if condition]`

```python
reto = [i for i in range(1, 100_000) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
```

## Dictionary comprehensions

Es muy parecido a las list comprehensions:

```python
dictionay_naturals = {i: i**3 for i in range(1, 101) if i % 3 != 0}
```

**Estructura:**

`{key: value for element in iterable if condition}`

```python
my_dic = {i: math.sqrt(i) for i in range (1, 1001)}
```

# 4. Conceptos avanzados de funciones

---

## Funciones anónimas: lambda

Hay una forma de crear funciones sin nombre, anónimas. Se las conoce como lambda functions. Pueden tener todos los argumentos necesarios, pero solo puede tener una línea de código.

**Estructura:**

`lambda argumentos: expresión`

```python
palindrome = lambda string: string == string[::-1]

print(palindrome("ana"))
```

No usa **return,** ya que por defecto guarda el resultado de la función anónima en la variable.

Para ejecutar la función, usa la variable en la que la guardaste y ponle como argumentos los señalados en lambda (en este caso, una string).

## High order functions: filter, map and reduce

Una función de orden superior es una función que recibe como parámetro a otra función.

Las funciones filter, map y reduce son muy importantes en una gran cantidad de lenguajes:

### Filter

La función filter recibe como parámetros una lambda function y una lista (en realidad un iterable). Devuelve un iterador que puedes guardar en otra lista.

*Imagina que quieres mostrar solo los números impares de una lista:*

```python
# Usando list comprehension:
my_list = [1, 4, 5, 6, 9, 13, 19, 21]
odd_comprehension = [i for i in my_list if i % 2 != 0]
print(odd_comprehension)

# Usando filter
odd_filter = list(filter(lambda i: i % 2 != 0, my_list))
print(odd_filter)

#Resultado
>>> [1, 5, 9, 13, 19, 21]
>>> [1, 5, 9, 13, 19, 21]
```

### Map

La estructura es muy parecida a filter.

*Crea una lista con los números al cuadrado de otra lista:*

```python
# Con list comprehension:
list1 = [1, 2, 3, 4, 5]
squares = [i**2 for i in list1]
print(squares)

# Con map:
squares_map = list(map(lambda i: i**2, list1))
print(squares_map)

#Resultado
>>> [1, 4, 9, 16, 25]
>>> [1, 4, 9, 16, 25]
```

### Reduce

Se necesita usar el módulo **functools** para poderlo usar. Hace que todos los números dentro de una lista hagan las operaciones, indicadas en la función, entre sí y devuelve 1 solo valor.

*Multiplica toda la lista.*

```python
from functools import reduce

my_list = [2, 2, 2, 2, 2,]
all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)

#Resultado
>>> 32
```

### Resumen

- **Filter**: filtra los datos de una lista retornando solo los que son True
- **Map**: manipula los datos de una lista
- **Reduce**: opera los datos de una lista entre sí para obtener 1 solo resultado

A continuación, un ejemplo de aplicación:

## Proyecto: filtrando datos

**Bonus:** `|` → este operador suma diccionarios de la misma manera que `+` suma listas.

Este código filtra datos de una base de datos usando list comprehensions y las high order functions filter() y map().

- Code
    
    ```python
    # una constante (es decir, que no se modificará) por lo que va por encima de la función run()
    DATA = [
        {
            'name': 'Facundo',
            'age': 72,
            'organization': 'Platzi',
            'position': 'Technical Coach',
            'language': 'python',
        },
        {
            'name': 'Luisana',
            'age': 33,
            'organization': 'Globant',
            'position': 'UX Designer',
            'language': 'javascript',
        },
        {
            'name': 'Héctor',
            'age': 19,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'ruby',
        },
        {
            'name': 'Gabriel',
            'age': 20,
            'organization': 'Platzi',
            'position': 'Associate',
            'language': 'javascript',
        },
        {
            'name': 'Isabella',
            'age': 30,
            'organization': 'Platzi',
            'position': 'QA Manager',
            'language': 'java',
        },
        {
            'name': 'Karo',
            'age': 23,
            'organization': 'Everis',
            'position': 'Backend Developer',
            'language': 'python',
        },
        {
            'name': 'Ariel',
            'age': 32,
            'organization': 'Rappi',
            'position': 'Support',
            'language': '',
        },
        {
            'name': 'Juan',
            'age': 17,
            'organization': '',
            'position': 'Student',
            'language': 'go',
        },
        {
            'name': 'Pablo',
            'age': 32,
            'organization': 'Master',
            'position': 'Human Resources Manager',
            'language': 'python',
        },
        {
            'name': 'Lorena',
            'age': 56,
            'organization': 'Python Organization',
            'position': 'Language Maker',
            'language': 'python',
        },
    ]
    
    def run():
        # usando list comprehensions
        # all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python']
        # all_Platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    
        # # usando filter() and map()
        # adults = list(filter(lambda worker: worker['age'] > 17, DATA))
        # adults = list(map(lambda worker: worker['name'], adults))
        # old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)) # el | sirve para sumar diccionarios
    
        #RETO inverso
        #filter() and map()
        all_python_devs = list(filter(lambda worker: worker['language'] == 'python', DATA))
        all_python_devs = list(map(lambda worker: worker['name'], all_python_devs))
    
        all_Platzi_workers = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
        all_Platzi_workers = list(map(lambda worker: worker['name'], all_Platzi_workers))
    
        #list comprehensions
        adults = [worker['name'] for worker in DATA if worker['age'] > 17]
    
        old_people = [worker | {'old': worker['age'] > 70} for worker in DATA]
    
        for worker in old_people:
            print(worker)
    
    if __name__ == '__main__':
        run()
    ```
    

# 5. Manejo de errores

---

## Los errores en el código

Hay errores que Python te avisa que te equivocaste, devolviendo un traceback (rastreo). Los mensajes traceback se deben leer desde la última línea hasta la primera.


Si hay un SyntaxError, el programa no se va a ejecutar. Por otro lado, si son excepciones, sí se ejecutará.

## Debugging

Depuración. Hacer esto es la manera correcta de encontrar los errores de tu código en lugar de ir revisando línea por línea. Esto se hace cuando Python **no te dice cuál es el error**, sino que el error es de tu algoritmo y debes revisar lo que escribiste.

Visual Studio Code tiene una función propia que te ayuda con esto. Dale a **run and debbug** y luego en el menú que te sale, dale a pausa para ir viendo línea a línea qué está pasando.

**Step over** te hace avanzar a cómo se está ejecutando el programa.

**Step into** te mete en la función sobre la que estés. En la parte izquierda sale una pestaña con todas las variables que hay en el código con los valores que contienen.

Si le das clic a una línea de código en específico, ya no hay necesidad de usar el botón de pausa, sino que el programa se ejecutará y luego se detendrá en el breakpoint que creaste. Puedes crear varios breakpoints.

## Manejo de excepciones

Para esto hay algunas palabras clave:

### Try and except

Cuando tengas un programa que es posible que haya algún error de excepción, por ejemplo en un formulario o en esta función 👇 que se deben ingresar strings, pero el usuario ingresó un number; puedes usar `try` para que intente ejecutar el programa. Y si hay un error, puedes poner debajo un `except error_name` y que el programa haga otra cosa para que no se dé el error. Si el error de excepción que se produce es diferente al que colocaste en el **except**, se producirá el error.

```python
def pailindrome(string):
    return string == string[::-1]

try:
    print(pailindrome(1))
except TypeError:
    print("Solo se puede ingresar strings")
```

Aquí pones un except TypeError en caso de que te pongan un Type que no sea strings.


### Raise

Eleva un error para en caso de que pase algo, lo invoque. En la definición se usa un try and except. En el try pon el error con un if (en este caso una cadena vacía) y luego convoca (eleva) un ValueError con `raise ValueError("mensaje")`. Y luego el return o la función como tal. En el except, vuelve a convocar el ValueError que creaste (el `as ve:` es una abreviación impuesta) y puedes hacer que se imprima el mensaje que pusiste y un return para la función:

```python
def pailindrome(string):
    try:
        if len(string) == 0:
            raise ValueError("No se puede ingresar una cadena vacía")
        return string == string[::-1]
    except ValueError as ve:
        print(ve)
        return False
try:
    print(pailindrome(" "))
except TypeError:
    print("Solo se puede ingresar strings")
```

### Finally

Es rara de encontrar. Se la usa al final de un try except para hacer cosas particulares como cerrar un archivo, cerrar una conexión a una base de datos o liberar recursos externos.

```python
try:
    f = open("archivo.txt")
    # hacer cualquier cosa con nuestro archivo
finally:
    f.close()
```

Abre un archivo y finalmente, haya error o no, cierra el archivo (creo que de Python).

## Poniendo a prueba el manejo de excepciones

```python
#RETO
def divisors(num):
    try:
        if num < 0:
            raise ValueError('Ingresa un número positivo')
        else:
            divisors = [i for i in range(1, num + 1) if num % i == 0]
            return divisors
    except ValueError as ve:
        return ve

def run():
    try:
        num = int(input('Ingresa un número: '))
        print(divisors(num))
        print('Termino mi programa')
    except ValueError:
        print('Debes ingresar un numero')
    

if __name__ == '__main__':
    run()
```

## Assert statements

Otra manera de manejar errores. Si bien es menos común que los anteriores, también se puede hacer.

Assert significa afirmar. Así que se lee: afirmo que esta condición es verdadera, si no, imprimo este mensaje de error.

```python
assert condición, mensaje de error

```

```python
def palindrome(string):
    assert len(string) > 0, "No se puede ingresar una cadena vacía"
    return string == string[::-1]

print(palindrome(""))

```

# 6. Manejo de archivos

---

## ¿Cómo trabajar con archivos?

Hay 2 tipos de archivos: los de texto y los binarios.

Los binarios tienen dentro bytes que representan cosas muy complejas. Son archivos con los que no se interactúa con los lenguajes de programación, sino con software especializado.

Hay 3 formas de abrir un archivo de texto con Python:

R -> Lectura
W -> Escritura
A -> Sobreescribir

A es append. Estos son los modos de apertura.

### Estructura para trabajar con archivos

```python

with open("./ruta/del/archivo.txt", "r") as f:

```

with + open('ruta', 'modo de apertura') as name: el nombre es como se va a llamar el archivo en el programa.

**with** — si se cierra el programa o script inesperadamente, hace que el archivo no se rompa.

```python
with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
```

## Trabajando con archivos de texto en Python

En este archivo, read() lee el archivo y lo va agregando a una lista. Recuerda que lo que lee lo trae en strings.

Write()  sobreescribe o hace append al archivo dependiendo si usas "w" o "a" en el modo de apertura. También, si en la ruta pones al final un archivo nuevo y estás en escritura, lo crea.

```python
def read():
    numbers = []
    with open('./archivos/numbers.txt', 'r', encoding='utf-8') as f:
        for i in f:
            numbers.append(int(i))
    print(numbers)

def write():
    names = ['Tony', 'Miguel', 'Pepe', 'Christian', 'Rocío']
    with open('./archivos/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')

def run():
    write()

if __name__ == '__main__':
    run()
```

# 7. Conclusión

---

## Reto final: Juego del Ahorcado o Hangman Game


```python
import random #This library permit to get random words from us data.txt list.
import os

def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper()) # ".strip()" Remove spaces at the beginning and at the end of the string. ".upper()" change each letter in capital letter.
    return words

def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data) #Here we chose the word randomly.
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list) #Here we assing underscores to each letter of the chosen word.
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter].append(idx)

    while True:
        os.system("clear") #If you are in Unix Max or Linux use clear, if you are in windoes use cls.
        print("Guess a word!")
        for element in chosen_word_list_underscores:
            print(element + " ", end="")
        print("\n")

        letter = input("Write a letter: ").strip().upper()
        assert letter.isalpha(), "Please, only use letters"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter
        if "_" not in chosen_word_list_underscores:
            os.system("clear")
            print("Yu WON! The word is", chosen_word)
            break

if __name__ == "__main__":
    run()
```