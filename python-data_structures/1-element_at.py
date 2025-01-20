#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Récupère un élément d'une liste à un indice donné.

    :param my_list: La liste dans laquelle récupérer l'élément
    :param idx: L'indice de l'élément à récupérer
    :return: L'élément à l'indice spécifié, ou None si l'indice est invalide
    """
    if idx < 0:
        return None

    if idx >= len(my_list):
        return None

    return my_list[idx]
