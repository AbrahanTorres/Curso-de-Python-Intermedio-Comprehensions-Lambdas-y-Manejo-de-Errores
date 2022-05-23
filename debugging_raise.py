def divisors(num):
    divisors = []
    for i in range(1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    while True:
        try:
            num = int(input("Ingresa un número: "))
            if num < 0:  #Si el numero es menor a cero, es un número negativo y no está permitido, se eleva un mensaje de erro ValueError.
                raise ValueError
            print(divisors(num))
            print("Terminó mi programa")
            break
        except ValueError:
            print("Debes ingresar un entero positivo")

if __name__ == "__main__":
    run()