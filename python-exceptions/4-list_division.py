def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        result = 0
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                print("wrong type")
                raise TypeError
            result = a / b
        except IndexError:
            print("out of range")
        except TypeError:
            pass  # Message already printed before raising
        except ZeroDivisionError:
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
