#!/usr/bin/python3
safe_print_integer = __import__('1-safe_print_integer').safe_print_integer

value = 89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = -89
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

value = "School"
has_been_print = safe_print_integer(value)
if not has_been_print:
    print("{} is not an integer".format(value))

print("Test 1: ", safe_print_integer(42))  # Doit imprimer "42" et retourner True
print("Test 2: ", safe_print_integer("42"))  # Doit retourner False car "42" est une chaîne, pas un entier
print("Test 3: ", safe_print_integer("abc"))  # Doit retourner False car "abc" n'est pas un entier
print("Test 4: ", safe_print_integer([1, 2]))  # Doit retourner False car ce n'est pas un entier
print("Test 5: ", safe_print_integer(None))
