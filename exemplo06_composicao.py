class Motor:
    # Construtor
    def __init__(self, potencia: int, combustivel: str):
        self.potencia = potencia
        self.combustivel = combustivel


class Carro:
    def __init__(self, modelo: str, ano_lancamento: int, motor: Motor):
        self.modelo = modelo
        self.ano_lancamento = ano_lancamento
        self.motor = motor


def exemplo_carro():
    motor_golf_tsi = Motor(140, "flex")

    golf_tsi = Carro("Golf TSI", 2013, motor_golf_tsi)

    print(golf_tsi.modelo) # Modelo pertence ao carro
    print(golf_tsi.ano_lancamento) # Ano de lançamento pertence ao carro
    print(golf_tsi.motor.potencia) # Potencia pertence ao motor
    print(golf_tsi.motor.combustivel)


class Bateria:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade
        # Definimos que o celular já tem a carga em 100%
        self.carga = 100 # 100% de bateria

    def utilizar(self, consumo: int):
        self.carga = self.carga - consumo

    def apresentar_dados(self):
        print(f"""Bateria:
Capacidade: {self.capacidade}mAh
Carga: {self.carga}%
""")


class Armazenamento:
    def __init__(self, capacidade: int):
        self.capacidade = capacidade

    def apresentar_dados(self):
        print(f"Armazenamento: {self.capacidade}GB")


class Celular:
    def __init__(self, modelo: str, preco: float, cor: str, bateria: Bateria, armazenamento: Armazenamento):
        self.modelo = modelo
        self.preco = preco
        self.cor = cor
        self.bateria = bateria
        self.armazenamento = armazenamento

    def navegar_youtube(self, minutos):
        # Simular bateria viciada
        print("Navegando no youtube")
        descarregamento_por_minuto = 2
        nivel_consumo = minutos * descarregamento_por_minuto
        self.bateria.utilizar(nivel_consumo)


    def apresentar_dados(self):
        print(f"""Celular:
Modelo: {self.modelo}
Preço: R$ {self.preco:.2f}
Cor: {self.cor}
""")
        self.bateria.apresentar_dados()
        self.armazenamento.apresentar_dados()

def exemplo_celular():

    bateria_iphone = Bateria(capacidade=3349) # 3.349mAh  de bateria
    armazenamento_iphone = Armazenamento(capacidade=128) # 128GB

    iphone_15 = Celular(
        modelo="iPhone 15",
        preco=4200.98,
        cor="Azul pastel",
        bateria=bateria_iphone,
        armazenamento=armazenamento_iphone,
    )

    iphone_15.apresentar_dados()
    iphone_15.navegar_youtube(minutos=30)
    iphone_15.apresentar_dados()
    # Alterantiva 1
    # bateria_iphone_lukita.apresentar_dados()
    # armazenamento_iphone_lukita.apresentar_dados()
    # Alterantiva 2
    # iphone_15.bateria.apresentar_dados()
    # iphone_15.armazenamento.apresentar_dados()
