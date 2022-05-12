def run():
    my_list =  [1, "Hello", True, 4.5] 

    my_dict = {"Firstname": "Abraham", "Lastname": "Torres"}

    super_list = [
        {"Firstname": "Abraham", "Lastname": "Torres"},
        {"Firstname": "Facundo", "Lastname": "García"},
        {"Firstname": "Pepe", "Lastname": "RodeloTorres"},
        {"Firstname": "Susana", "Lastname": "Martinezs"},
        {"Firstname": "José", "Lastname": "Serrao"} ]


    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "Integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

if __name__ == '__main__':
    run()