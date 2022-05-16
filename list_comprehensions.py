def run():
    squares = []   #Se crea la lista 
    for i in range(1, 101):   #Rango del 1 al 100
        squares.append(i**2)   #Se registra con append los números al cuadrado del 1 al 100

    print(squares)

if __name__=='__main__':
    run()