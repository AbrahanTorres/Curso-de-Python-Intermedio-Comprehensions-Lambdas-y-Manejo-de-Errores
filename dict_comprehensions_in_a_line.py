def run():
    # my_dict = {}

    # for i in range(1, 101):
    #     if i % 3 !=0:         #Números que no son divisibles entre 3, usamos el módulo % 3 que nos da el resto y deberá ser diferente a 0.
    #         my_dict[i]= i**3


#Diccionario de los números del  1 al 100 que no son divisibles entre 3 y como llave, y el valor del diccionario elevado al cubo para cada llave.

    my_dict = {i: i**3 for i in range(1, 101) if i % 3 !=0} # i : i**3  son llave : valor del diccionario. 

    print(my_dict)

if __name__ == "__main__":
    run()
