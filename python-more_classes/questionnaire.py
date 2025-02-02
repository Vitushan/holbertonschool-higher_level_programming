#!/usr/bin/python3

score = 0
def ask_1():
    global score
    print("Quelle est la capitale de la france ?")
    print("(a) Marseille")
    print("(b) Nice")
    print("(c) Paris")
    print("(d) Bordeaux")
    print()
    answer = input("your response: ")
    if answer.lower() == "c":
        print("good answer")
        score += 1
    else:
        print("Revoie ta geographie")

def ask_2():
    global score
    print("Quelle est la capitale de la belgique?")
    print("(a) Gand")
    print("(b) Liege")
    print("(c) Antwerpen")
    print("(d) Brussel")
    print()
    answer = input("your response: ")
    if answer.lower() == "d":
        print("good answer")
        score += 1
    else:
        print("Revoie ta geographie")

def ask_3():
    global score
    print("Quelle est la capitale de la Croatie  ?")
    print("(a) Zagreb")
    print("(b) Dubrovnik")
    print("(c) Karlovac")
    print("(d) Ogulin")
    print()
    answer = input("your response: ")
    if answer.lower == "a":
        print("good answer")
        score += 1
    else:
        print("Revoie ta geographie")

def ask_4():
    global score
    print("Quelle est la capitale du Maroc ?")
    print("(a) Agadir")
    print("(b) Rabat")
    print("(c) Casablanca")
    print("(d) Al hoceima")
    print()
    answer = input("your response: ")
    if answer.lower() == "b":
        print("good answer")
        score += 1
    else:
        print("Revoie ta geographie")
ask_1()
ask_2()
ask_3()
ask_4()
print("vous avez obtenue {} de bonne reponse sur 4!".format(score))
