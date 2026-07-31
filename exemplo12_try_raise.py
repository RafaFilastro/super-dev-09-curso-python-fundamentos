#Lançar um erro simples
def validar_idade(idade: int):
    print("Validando idade")
    if idade < 0:
        raise ValueError("A idade não deve ser menor que zero.")
    print("Idade validada com sucesso")


def testar_validade_idade():
    try:
        validar_idade(-1)
    except ValueError as erro:
        print("Erro: ", erro)
    print("Aplicação encerrou com sucesso")

#criar uma exceção customizada
class SaldoInsuficienteError(Exception):
    def __init__(self, saldo, valor):
        self.saldo = saldo
        self.valor = valor
        self.faltam = valor - saldo
        super().__init__(
            f"Saldo insuficiente: saldo R$ {self.saldo:.2f}, "
            f"saque R$ {self.valor:.2f} (faltam R$ {self.faltam:.2f})"
        )


def sacar(saldo, valor):
    print("Realizandoi saque")
    if not isinstance(valor, (float, int)):
        raise TypeError("O valor deve ser um número real ou inteiro")

    if valor <= 0:
        raise ValueError("O valor deve ser superior a R$ 0,00")

    if valor > saldo:
        # raise ValueError(f"Saldo insuficiente, Saldo atual: R$ {saldo:.2f}")
        raise SaldoInsuficienteError(saldo, valor)

    saldo -= valor
    print("Saque realizado com sucesso")


def exemplo_tipos_erros():
    saldo:float = float(input("Digite o saldo: ").replace(",", "."))
    valor_saque: float = float(input("Digite o valor: ").replace(",", "."))

    try:
        sacar(saldo, valor_saque)
    except TypeError as erro:
        print("Erro: ", erro)
    except ValueError as erro:
        print("Erro: ", erro)
    except SaldoInsuficienteError as erro:
        print("Erro: ", erro)

exemplo_tipos_erros()
