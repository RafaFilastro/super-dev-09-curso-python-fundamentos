from typing import Dict, List

def exemplo_basico_Dicionario():
    carros = {}

    carros["bmw"] = "M5"
    carros["mercedes"] = "GLA 250"
    carros["fiat"] = "uno"

    carros["mercedes"] = "GLA 250"
    print("Dicionário: ", carros)

    # Obter as chaves que tenho no meu dicionário
    print(carros.values())

# função que tem um parâmetro do tipo dicionário
def obter_clientes_com_score_alto(clientes: Dict[str, Dict[str, float]]):
    # Descobrir quais clientes tem score alto(acima de 650)

    clientes_selecionados: List[str] = []
    for nome_cliente, dados_cliente in clientes.items():
        score = dados_cliente["score"]
        if score > 650:
            clientes_selecionados.append(nome_cliente)

    return clientes_selecionados


def somar_salarios(clientes: Dict[str, Dict[str, float]]) -> float:
    total = 0
    for dados in clientes.values():
        salario = dados["salario"]
        total = total + salario
    return total

def obter_nome_clientes(clientes: Dict[str, Dict[str, float]]) -> List[str]:
    nomes = []
    for nome_cliente in clientes.keys():
        nomes.append(nome_cliente)
    return nomes

def processar_disponibilidade_emprestimo():
    clientes: Dict[str, Dict[str, float]] = {
        "Amanda": {
            "salario": 2000,
            "id": 100,
            "score": 997
        },
        "Pedro": {
            "salario": 20_951.29,
            "id": 101,
            "score": 130
        },
        "Steffany": {
            "salario": 4593.29,
            "id": 102,
            "score": 520
        },
        "Rogério": {
            "salario": 17231.39,
            "id": 103,
            "score": 776
        }
    }
    clientes_aprovados_para_emprestimo = obter_clientes_com_score_alto(clientes)
    total_salarios = somar_salarios(clientes)
    nome_clientes = obter_nome_clientes(clientes)

    print("Clientes aprovados para empréstimo: ", clientes_aprovados_para_emprestimo)
    print("Total dos salários: ", total_salarios)
    print("Clientes: ", nome_clientes)


def exemplo_revisao():
    celular: Dict[str, str|float|int|bool] = {}
    celular["modelo"] = "Samsung A03"
    celular["armazenamento"] = 256
    celular["preco"] = 999.90
    celular["lancado"] = True

    print("Celular: ", celular["modelo"])


exemplo_revisao()



def obter_nomes_produtos(produtos):
    nomes_produtos = []

    for produto in produtos:
        nomes_produtos.append(produto["nome"])
    return nomes_produtos


def obter_produtos_com_estoque_baixo(produtos):
    produtos_estoque_baixo = []

    for produto in produtos:
        if produto["estoque"] < 10:
            produtos_estoque_baixo.append(produto["nome"])
    return produtos_estoque_baixo


def obter_produtos_por_categoria(produtos, categoria_pesquisada):
    produtos_filtrados = []

    for produto in produtos:
        if produto["categoria"] == categoria_pesquisada:
            produtos_filtrados.append(produto["nome"])
    return produtos_filtrados


def obter_produtos_acima_do_preco(produtos, preco_minimo):
    produtos_caros = []

    for produto in produtos:
        if produto["preco"] > preco_minimo:
            produtos_caros.append(produto["nome"])
    return produtos_caros


def somar_valor_total_estoque(produtos):
    total = 0

    for produto in produtos:
        preco = produto["preco"]
        estoque = produto["estoque"]
        valor_produto_estoque = preco * estoque
        total = total + valor_produto_estoque
    return total


def exercicio_10():
    produtos = [
        {
            "nome": "Placa de Video",
            "categoria": "Informática",
            "preco": 5450.00,
            "estoque": 5
        },
        {
            "nome": "Mouse Logitech",
            "categoria": "Informática",
            "preco": 850.00,
            "estoque": 10
        },
        {
            "nome": "Monitor 144hz",
            "categoria": "Informática",
            "preco": 700.00,
            "estoque": 10
        },
        {
            "nome": "Cadeira gamer",
            "categoria": "Móveis",
            "preco": 350.00,
            "estoque": 10
        },
        {
            "nome": "Memoria ram 16gb ddr5",
            "categoria": "Informática",
            "preco": 1780.10,
            "estoque": 5
        }
    ]

    nomes = obter_nomes_produtos(produtos)

    produtos_estoque_baixo = obter_produtos_com_estoque_baixo(
        produtos
    )

    categoria_pesquisada = "Informática"

    produtos_categoria = obter_produtos_por_categoria(
        produtos,
        categoria_pesquisada
    )

    preco_minimo = 100

    produtos_acima_preco = obter_produtos_acima_do_preco(
        produtos,
        preco_minimo
    )

    valor_total_estoque = somar_valor_total_estoque(produtos)

    print("Nomes dos produtos:")
    print(nomes)

    print("\nProdutos com estoque baixo:")
    print(produtos_estoque_baixo)

    print(f"\nProdutos da categoria {categoria_pesquisada}:")
    print(produtos_categoria)

    print(f"\nProdutos acima de R$ {preco_minimo}:")
    print(produtos_acima_preco)

    print("\nValor total em estoque:")
    print(valor_total_estoque)


#exercicio_10()
