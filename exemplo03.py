# GUI => Graphical User interface
# UI => User Interface

# Instalar a biblioteca rich: `pip install rich`
# Instalar a biblioteca questionary: `pip install questionary`

from rich.console import Console
from rich.table import Table
import requests
import questionary
import os

url_base = "https://api.franciscosensaulas.com"

def menu():
    opcoes_menu = [
        "Consultar Categorias",
        "Cadastrar Categoria",
        "Editar Categoria",
        "Apagar Categoria",
        "Sair" 
    ]

    menu_escolhido = ""
    while menu_escolhido != "Sair":
        menu_escolhido = questionary.select("Menu", choices=opcoes_menu).ask()
        limpar_terminal()

        if menu_escolhido == "Consultar Categorias":
            consultar_categorias()
        elif menu_escolhido == "Cadastrar Categoria":
            cadastrar_categoria()
        elif menu_escolhido == "Apagar Categoria":
            apagar_categoria()

        if menu_escolhido != "Sair":
            questionary.press_any_key_to_continue(
                "Digite qualquer tecla para continuar..."
            ).ask()
            limpar_terminal()


def limpar_terminal():
    os.system("cls")


# Consultar categorias
def consultar_categorias():
    url = f"{url_base}/api/v1/biblioteca/categorias"

    resposta = requests.get(url)

    console = Console()

    table = Table(show_header=True, header_style="bold blue", show_lines=True)
    table.add_column("Código")
    table.add_column("Nome")

    categorias = resposta.json()

    for categoria in categorias:
        table.add_row(str(categoria["id"]), categoria["nome"])

    console.print(table)


def cadastrar_categoria():
    url = f"{url_base}/api/v1/biblioteca/categorias"
    nome_categoria: str = questionary.text("Digite o nome da categoria:").ask()

    categoria = {
        "nome": nome_categoria
    }

    resposta = requests.post(url, json=categoria)
    # print("Status Code: ", resposta.status_code)
    if resposta.status_code == 201:
        print("Categoria cadastrada com sucesso")
    else:
        print("Não foi possível cadastrar a categoria")


def apagar_categoria():
    id = int(questionary.text("Digite o código da categoria para apagar:").ask())
    url = f"{url_base}/api/v1/biblioteca/categorias/{id}"

    resposta = requests.delete(url)

    if resposta.status_code == 204:
        print("Categoria apagada com sucesso")
    elif resposta.status_code == 404:
        print("Não foi possível encontrar a categoria com este código")
    else:
        print("Não foi possível apagar a categoria")
    # print("Status Code:", resposta.status_code)

menu()
