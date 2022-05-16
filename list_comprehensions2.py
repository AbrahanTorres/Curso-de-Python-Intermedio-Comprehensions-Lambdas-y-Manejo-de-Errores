def run():
    # squares = []

    # for i in range(1, 101):  
    #     if i % 3 != 0:
    #         squares.append(i**2)

    squares = [i**2 for i in range(1, 101) if i % 3 !=0] #ListComprehensions: Se registran los números al cuadrado que al ser divididos entre  3, el resto de la división da diferente de cero. Es decir la lista de los números que no son divisibles entre  3.
    
    print(squares)


if __name__ == "__main__":
    run()