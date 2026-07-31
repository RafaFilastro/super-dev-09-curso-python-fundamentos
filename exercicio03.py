import requests

url_base = "https://api.franciscosensaulas.com"

def consultar_empresa():
    url = f"{url_base}/api/v1/empresa"

    resposta = requests.get(url)

    print(f"Status Code: {resposta.status_code}")
    print(f"Response: {resposta.text}")


#consultar_empresa()

def consultar_empresa_por_id():
    id = 131

    url = f"{url_base}/api/v1/empresa/{id}"

    resposta = requests.get(url)

    print(f"Status Code: {resposta.status_code}")
    print(f"Response: {resposta.text}")


#consultar_empresa_por_id()


def consultar_produtos():
    url = f"{url_base}/api/v1/empresa/produtos"

    resposta = requests.get(url)

    print(f"Status Code: {resposta.status_code}")
    print(f"Response: {resposta.text}")


#consultar_produtos()


def consultar_produto_por_id():
    id = 32

    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    resposta = requests.get(url)

    print(f"Status Code: {resposta.status_code}")
    print(f"Response: {resposta.text}")


#consultar_produto_por_id()


def cadastrar_empresa():
    url = f"{url_base}/api/v1/empresa"

    empresa = {
        "nome": "Skol beats LTDA",
        "cnpj": "12345678000544"
    }

    resposta = requests.post(url, json=empresa)

    print(f"Status Code: {resposta.status_code}")
    print(f"Response: {resposta.text}")


#cadastrar_empresa()

def cadastrar_produto():
    url = f"{url_base}/api/v1/empresa/produtos"

    produto = {
        "nome": "Chinelo com prego",
        "preco": 540.50,
        "categoria": "Bem estar"
    }

    resposta = requests.post(url, json=produto)


    print(f"Status Code: {resposta.status_code}")
    print(f"Response: {resposta.text}")

#cadastrar_produto()

def editar_empresa():
    id = 207

    url = f"{url_base}/api/v1/empresa/{id}"

    empresa = {
        "nome": "Vinhos RF Ltda",
        "cnpj": "79865321111254"
    }

    resposta = requests.put(url, json=empresa)

    print(f"Status Code: {resposta.status_code}")


#editar_empresa()

def editar_produto():
    id = 35

    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    produto = {
        "nome": "Caneta Bic",
        "preco": 875.99,
        "categoria": "Material Escolar"
    }
    resposta = requests.put(url, json=produto)

    print(f"Status Code: {resposta.status_code}")


#editar_produto()

def apagar_empresa():
    id = 207
    url = f"{url_base}/api/v1/empresa/{id}"

    resposta = requests.delete(url)

    print(f"Status Code: {resposta.status_code}")


#apagar_empresa()

def apagar_produto():
    id = 35
    url = f"{url_base}/api/v1/empresa/produtos/{id}"

    resposta = requests.delete(url)

    print(f"Status Code: {resposta.status_code}")


#apagar_produto()
