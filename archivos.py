#La siguiente función nos permite leer el archivo numbers.
def read():
    numbers = []
    with open("./archivos/numbers.txt", "r", encoding ="utf-8") as f: #encoding = "utf-8" sirve para poder leer simbolos raros como la ñ.
        for line in f:
            numbers.append(int(line))
    print(numbers)

#La siguiente función nos permite crear archivos y añadir información, en este caso, nombres.
def write():
    names = ["Abraham", "Miguel", "Pepe", "Christian", "Rocío"]
    with open("./archivos/names.txt", "a", encoding ="utf-8") as f:  # la letra "a" permite agregar, como append, las siguientes iteraciones.
        for name in names:
            f.write(name)
            f.write("\n") # "\n" sirve para dejar un espacio cada vez que se escribe un nombre.

def run():
    write()

if __name__ == "__main__":
    run()