# Professores
from typing import Dict, List


def exemplo_dicionario_dentro_lista():
    nomes = ["Chiquinho", "Sandra", "Renan"]
    materia = ["Python", "Mercado Trabalho", "Engenharia"]
    tempo_casa = [8, 10, 15]

    dados_chiquinho: Dict[str, str | int] = {  # noqa: F823
        "nome": "Chiquinho",
        "materia": "Python",
        "tempo_casa": 8
    }

    dados_sandra: Dict[str, str | int] = {
        "nome": "Sandra",
        "materia": "Mercado Trabalho",
        "tempo_casa": 10
    }

    dados_renan: Dict[str, str | int] = {
        "nome": "Renan",
        "materia": "Engenharia",
        "tempo_casa": 15
    }

    print("Apelido do Francisco: ", dados_chiquinho["nome"])
    print("Apelido de Sandra: ", dados_sandra["nome"])
    print("Apelido de Renan: ", dados_renan["nome"])

    professores: List[Dict[str, str | int]] = [  # noqa: F823
        dados_chiquinho,
        dados_sandra,
        dados_renan
    ]

    print(professores[0]["nome"])
    print(dados_chiquinho["nome"])# Professores
    from typing import Dict, List


    nomes = ["Chiquinho", "Sandra", "Renan"]  # noqa: F841
    materia = ["Python", "Mercado Trabalho", "Engenharia"]  # noqa: F841
    tempo_casa = [8, 10, 15]  # noqa: F841

    dados_chiquinho: Dict[str, str | int] = {
        "nome": "Chiquinho",
        "materia": "Python",
        "tempo_casa": 8
    }

    dados_sandra: Dict[str, str | int] = {
        "nome": "Sandra",
        "materia": "Mercado Trabalho",
        "tempo_casa": 10
    }

    dados_renan: Dict[str, str | int] = {
        "nome": "Renan",
        "materia": "Engenharia",
        "tempo_casa": 15
    }

    print("Apelido do Francisco: ", dados_chiquinho["nome"])
    print("Apelido de Sandra: ", dados_sandra["nome"])
    print("Apelido de Renan: ", dados_renan["nome"])

    professores: List[Dict[str, str | int]] = [
        dados_chiquinho,
        dados_sandra,
        dados_renan
    ]

    print(professores[0]["nome"])
    print(dados_chiquinho["nome"])

def exemplo_dicionario_somando():
    from typing import Dict, List

    salarios = [2000, 3000, 5000]

    soma = 0
    for salario in salarios:
        soma = soma + salario
    print("Soma de uma lista simples: ", soma)

    # chaves {} colchetes []
    professores: List[Dict[str, str | int]] = [
        {
            "nome": "chiquinho",
            "salario": 2000
        },
        {
            "nome": "sandra",
            "salario": 3000
        },
        {
            "nome": "renan",
            "salario": 5000
        }
    ]
    # lista => for nome in nomes
    # dicionario:
    #   for chave in seila.keys()
    #   for valor in seila.values()
    #   for chave, valor in seila.items()
    soma_salarios = 0
    for professor in professores:
        salario = professor["salario"]
        soma_salarios = soma_salarios + salario
    print("Soma de uma lista de dicionário: ", soma_salarios)


exemplo_dicionario_somando()
