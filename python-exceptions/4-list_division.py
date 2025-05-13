#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    # Utilisation de la taille maximum entre les deux listes
    for i in range(list_length):
        try:
            # Vérification si l'index dépasse la taille de l'une des listes
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError

            a = my_list_1[i]
            b = my_list_2[i]

            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                result.append(0)
            else:
                result.append(a / b)

        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)

    return result
