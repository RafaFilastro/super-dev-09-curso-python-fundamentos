import os
from typing import Dict, List


class Cachorro:
    # __init__ é o construtor da classe, que é executado
    # quando instanciamos um objeto da classe
    def __init__(self, apelido: str, raca: str, cor: str, peso: float, idade: int):
        self.apelido = apelido
        self.raca = raca
        self.cor = cor
        self.peso = peso
        self.idade = idade

    def apresentar_dados(self):
        print(f"Cachorro: {self.apelido}")
        print(f"Raça: {self.raca}")
        print(f"Cor: {self.cor}", end="\n\n\n")

    def fazer_aniversario(self):
        self.idade = self.idade + 1
        print("FELIZ ANIVERSÁRIO!!!!!!", self.apelido, "fez", self.idade, "anos")


def  exemplo_cachorro():
    tobi = Cachorro("Tobi", "Vira-lata", "caramelo", 25.60, 6)
    # Tobi aumentou de peso, fazendo dieta da água, tudo que da água na boca ele come, comeu tênis
    tobi.peso = 29.34
    tobi.apresentar_dados()

    thor = Cachorro(cor="capa preta", raca="Pastor alemão", peso=38, idade=8, apelido="Thor")
    thor.fazer_aniversario()
    thor.apresentar_dados()

    mogli = Cachorro("Mogli", "Vira-lata", "preto", 30, 6)
    mogli.apresentar_dados()


class Pokemon:
    # Construtor => __init__
    def __init__(self, nome: str, tipo: str):
        # Propriedades
        self.nome = nome
        self.tipo = tipo

    # Funções
    def apresentar_dados(self):
        print(f"""Pokemon: {self.nome}
Tipo: {self.tipo}
""")


# Orientação a objetos
def exemplo_pokedex():
    # Objeto chamado charizard que é instanciado da classe Pokemon
    charizard = Pokemon("Charizard", "Fogo")
    bulbasaur = Pokemon("Bulbasaur", "Planta")

    charizard.apresentar_dados()
    bulbasaur.apresentar_dados()

# exemplo_pokedex()


class Temperatura:
    def __init__(self, valor: float, origem: str):
        self.origem = origem
        self.valor = valor

    def converter(self, destino: str):
        if self.origem == "celsius":
            temperatura = self.__converter_celsius(destino)
        elif self.origem == "kelvin":
            temperatura = self.__converter_kelvin(destino)
        elif self.origem == "fahrenheit":
            temperatura = self.__converter_fahrenheit(destino)
        print(temperatura)

    def __converter_celsius(self, destino):
        if destino == "kelvin":
            temperatura = self.valor + 273.15
        elif destino == "fahrenheit":
            temperatura = self.valor * 1.8 + 32
        else:
            temperatura = None # None em python é o null
        return temperatura

    def __converter_kelvin(self, destino: str):
        temperatura = None
        if destino == "celsius":
            temperatura = self.__converter_kelvin_para_celsius()
        elif destino == "fahrenheit":
            temperatura = self.__converter_kelvin_para_celsius() * 1.8 + 32
        return temperatura

    def __converter_fahrenheit(self, destino: str):
        if destino == "celsius":
            return (self.valor - 32) * (5/9)
        elif destino == "kelvin":
            return (self.valor - 32) * (5/9) + 273.15
        return None

    def __converter_kelvin_para_celsius(self):
        return self.valor - 273.15

def exemplo_temperatura():
    # Instanciar um objeto
    temperatura: float = float(input("Digite a temperatura"))
    origem: str = input("Digite a unidade de medida de origem")
    destino: str = input("Digite a unidade de medida de destino")

    temperatura_35_celsius = Temperatura(temperatura, origem)
    temperatura_35_celsius.converter(destino)


# class Temperatura:
#     def __init__(self, valor: float):
#         self.valor = valor

#     def converter_celsius_kelvin(self):
#         return self.valor + 273.15

#     def converter_celsius_fahrenheit(self):
#         return self.valor * 1.8 + 32

#     def converter_kelvin_para_celsius(self):
#         return self.valor - 273.15

#     def converter_kelvin_fahrenheit(self):
#         return self.converter_kelvin_para_celsius() * 1.8 + 32

#     def converter_fahrenheit_celsius(self):
#         return (self.valor - 32) * (5/9)

#     def converter_fahrenheit_kelvin(self):
#         return (self.valor - 32) * (5/9) + 273.15


# temperatura: float = float(input("Digite a temperatura"))
# origem: str = input("Digite a unidade de medida de origem")
# destino: str = input("Digite a unidade de medida de destino")


# temperatura = Temperatura(35)
# if origem == "celsius" and destino == "kelvin":
#     temperatura.converter_celsius_kelvin()

# Encapsulamento
# private   def __calcular() ou _calcular()
# public    def calcular()


class Funcionario:
    # Construtor
    def __init__(self, nome: str, salario: float, horas_extras: float, cargo: str):
        # Funcionários sempre trabalham 220 horas sem contas horas extras
        self.horas_trabalhadas = 220
        self.nome = nome
        self.salario = salario
        self.horas_extras = horas_extras
        self.cargo = cargo

    def calcular_horas_extras(self):
        # Regra de horas extras
        # Administrativo    Bônus 60%
        # Efetivo           Bônus 5%
        # Supervisor        Bônus sem direito
        percentual = 0
        if self.cargo == "Administrativo":
            percentual = 1.60
        elif self.cargo == "Efetivo":
            percentual = 1.05
        elif self.cargo == "Supervisor":
            print(self.nome, "não tem direito a horas extras")
            return

        valor_hora = self.salario / self.horas_trabalhadas
        valor_horas_extras = valor_hora * self.horas_extras * percentual
        print("\n==============================")
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário: R$ {self.salario:.2f}")
        print(f"Horas trabalhadas: {self.horas_trabalhadas}")
        print(f"Horas extras: {self.horas_extras}")
        print(f"Valor da hora: R$ {valor_hora:.2f}")
        print(f"Valor das horas extras: R$ {valor_horas_extras:.2f}")
        print("==============================")


def exemplo_funcionario():
    malaquias = Funcionario("Malaquinho da galera", 9854.30, 6, "Administrativo")
    lukita = Funcionario("Lukita da galera", 1200.29, 40, "Efetivo")
    jack = Funcionario("Jack", 4000, 120, "Supervisor")

    malaquias.calcular_horas_extras()
    lukita.calcular_horas_extras()
    jack.calcular_horas_extras()


class Loja:
    def __init__(self, nome: str):
        self.nome = nome
        self.produtos: List[Dict[str, str | int | float]] = []

    def adicionar_produto(self, nome: str, quantidade: int, preco: float):
        produto = {
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco,
            "total": quantidade * preco
        }
        self.produtos.append(produto)

    def listar_produtos(self):
        print("\n===== PRODUTOS =====")

        if len(self.produtos) == 0:
            print("Nenhum produto cadastrado.")
            return

        for produto in self.produtos:
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Valor: R$ {produto['preco']:.2f}")
            print(f"Total: R$ {produto['total']:.2f}")
            print("-" * 30)

    def fechar_compra(self, cupom: str):
        # CUPONS ACEITOS
        # MINHA_CASA        => 5%
        # PRIMEIRA_COMPRA   => 20%
        total_produtos = 0
        for produto in self.produtos:
            total_produtos = total_produtos + produto["total"]

        percentual_desconto = 0
        if cupom == "MINHA_CASA":
            percentual_desconto = 5
        elif cupom == "PRIMEIRA_COMPRA":
            percentual_desconto = 20
        elif cupom != "":
            print("CUPOM INVÁLIDO")
            return

        desconto = total_produtos * (percentual_desconto / 100)
        total_compra = total_produtos - desconto
        print("\n----------- RESUMO -----------")
        print(f"Cupom: {cupom if cupom else 'Nenhum'}")
        print(f"Desconto: {percentual_desconto}%")
        print(f"Valor do desconto: R$ {desconto:.2f}")
        print(f"Total dos produtos: R$ {total_produtos:.2f}")
        print(f"Total da compra: R$ {total_compra:.2f}")
        print("==============================")


def exemplo_loja():
    milium = Loja("Milium")

    # milium é um OBJETO da classe LOJA
    milium.adicionar_produto("Makita", 1, 1200.3)
    milium.adicionar_produto("Chave de fenda", 3, 19.90)

    milium.fechar_compra(cupom="MINHA_CASA")


class MenuLoja:
    def __init__(self, nome: str):
        self.loja: Loja = Loja(nome)


    def apresentar_menu(self):
        print("""
----------------------------------------------------------------
|                             MENU                             |
----------------------------------------------------------------
| 1 - Adicionar produto no carrinho                            |
| 2 - Apresentar carrinho                                      |
| 3 - Apresentar dados da loja                                 |
| 4 - Configurações                                            |
| 5 - Fechar compra                                            |
| 6 - Sair                                                     |
----------------------------------------------------------------
""")

    def limpar_terminal(self):
        os.system("cls")

    def executar(self):

        menu_escolhido = None
        while menu_escolhido != 6:
            self.limpar_terminal()
            self.apresentar_menu()
            menu_escolhido: int = int(input("Digite o menu escolhido: "))
            self.limpar_terminal()

            if menu_escolhido == 1:
                self.cadastrar_produto()
            if menu_escolhido == 2:
                self.loja.listar_produtos()
            elif menu_escolhido == 3:
                self.apresentar_dados_loja()
            elif menu_escolhido == 4:
                self.mudar_configuracoes()
            elif menu_escolhido == 5:
                self.finalizar_pedido()
            input("Press Enter para continuar...")

    def cadastrar_produto(self):
        nome: str = input("Digite o nome do produto: ")
        quantidade: int = int(input("Digite a quantidade: "))
        preco: float = float(input("Digite o preço: "))
        self.loja.adicionar_produto(nome, quantidade, preco)

    def apresentar_dados_loja(self):
        print("Loja: ", self.loja.nome)

    def mudar_configuracoes(self):
        nome_loja: str = input("Digite o nome da loja: ")
        self.loja.nome = nome_loja

    def finalizar_pedido(self):
        cupom: str = input("Digite o nome do cupom: ")
        self.loja.fechar_compra(cupom)

def exemplo_loja_com_menu():
    nome_loja: str = input("Digite o nome da loja: ")

    menu = MenuLoja(nome_loja)
    menu.executar()

exemplo_loja_com_menu()
