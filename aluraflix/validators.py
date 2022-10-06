from re import search


def hex_valido(hex):
    return search(r'^#(?:[0-9a-fA-F]{3}){1,2}$', hex)