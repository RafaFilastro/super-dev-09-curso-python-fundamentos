def exemplo_sem_tratamento():
    print("Divisão: ", 10 / 0)
    print("Mensgem depois da divisão")
    # Lança a excessão: ZeroDivisionError: division by zero


def exemplo_com_tratamento():
    try:
        print("Divisão: ", 10 / 0)
    except ZeroDivisionError:
        print("Não é possível dividir um número por zero.")

    print("O programa continuou normalmente")


def exemplo_com_tratamento_conversao():
    numero_digitado: str = "dois"
    try:
        # converter de str para int
        numero: int = int(numero_digitado)
        print("Número digitado: ", numero)
    except ValueError:
        print("Texto digitado não é um número válido")
    print("Acabou")


def exemplo_com_multiplos_tratamentos():
    numero1_digitado = "vinte e oito"
    numero2_digitado = "nove"

    try:
        resultado: int = int(numero1_digitado) / int(numero2_digitado)
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero")
    except ValueError:
        print("Erro: os valores precisam ser números")

    print("Obrigado por utilizar nosso sistema")


def exemplo_mensagem_erro():
    try:
        aluno = {"nome": "Pedro", "nota1": 9.75}
        media_aluno = aluno["media"]
        print(media_aluno)
    except KeyError as erro: # 'as' serve para pegar a variável do erro que ocorreu
        print("Mensagem de erro tentar acessar a chave:", erro)


# Ponto de entrada da aplicação, deve ter um único da aplicação inteira
if __name__ == "__main__":
    exemplo_mensagem_erro()
