import json


def carregar_arquivo(nome):
    with open(nome) as arquivo:
        lista_objetos = json.load(arquivo)
    return lista_objetos


def salvar_arquivo(nome, lista_objetos):
    with open(nome, 'w') as arquivo:
        json.dump(lista_objetos, arquivo, indent=4)
    return 1
