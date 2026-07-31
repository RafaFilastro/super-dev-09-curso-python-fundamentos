import time
import os

def exemplo_string():
    #declarando uma variavel do tipo string
    nome_livro_comeco: str = "harry potter"
    nome_livro_final: str = "AS reliquias da morte"
    # declarando uma string e armazenando a concatenação
    # title => Pascal CAse
    # Upper => UPPER CASE
    # lower => lower case
    # capitalize => Abacate com pera e limão
    nome_livro: str = nome_livro_comeco.title() + " " + nome_livro_final.upper()
    print("Livro das filhas da Miranda:", nome_livro)


def primeiro_exemplo():
    print("Olá Mundo")
    fruta: str = "Abacate"
    carro: str = "Corsa"
    quantidade_fruta: int = 6
    preco_unitario_fruta: float = 2.53
    print("Fruta:", fruta)
    print("Carro:", carro)
    print("Quantidade:", quantidade_fruta)
    print("Preço unitário:", preco_unitario_fruta)
    print("Preço total:", quantidade_fruta * preco_unitario_fruta)
    print("O carro", carro, " comprou a fruta:", fruta)


primeiro_exemplo()
exemplo_string()

def exemplo_solicitar_dados():
    # convertendo para letra minúscula o que o usúario digitou
    # removendo os espaços do começo e do fim
    console: str = input("Digite o nome do console: [XBOX/PS5]").upper().strip()
    quantidade: int = int(input("Digite a quantidade:"))

    preco : float = 0
    if console == "XBOX":
        preco = 6696.00
    # elif é `else if`
    elif console == "PS5":
        preco = 4277.07
    else:
        print("Console inválido")
        return

    print("Preço:", preco)
    print("Quantidade:", quantidade)
    print("Total:", preco * quantidade)


def exemplo_if_alunos():
    nota1: float = float(input("Digite a nota 1: "))
    nota2: float = float(input("Digite a nota 2: "))
    nota3: float = float(input("Digite a nota 3: "))

    media: float = (nota1 + nota2 + nota3) / 3
    aprovado: bool = 6 <= media <= 10

    print("Média:", media)

    if aprovado:
        print("Aprovado: sim")
    else:
        print("Aprovado: não")

def exemplo_while():
    def contar_ate_5():
        i = 0
        # Apresentar de 0 até 4
        while i < 5:
            print(i)
            # i = i + 1 Incrementar
            i += 1

    def contagem_regressiva():
        i = 5
        print("Contagem regressiva")
        # Apresentar de 5 até 0
        while i >= 0:
            print(i)
            # i = i - 1 Decrementar
            i -= 1

    def solicitar_dados():
        i = 0
        total_mensal_salarios = 0
        while i < 3:
            jogador: str = input("Nome do jogador de futebol: ")
            #posicao: str = input("Posição do jogar: ")
            salario_anual: float = float(input("Salário anual: "))

            salario_mensal = salario_anual / 12
            # separator permite mudar o comportamento de como será concatenado os dados no print
            # end permite mudar o que acontece depois que terminou de imprimir no terminal
            print("Jogador:", jogador, "ganha R$", salario_mensal, sep="  ", end="\n\n\n\n")

            total_mensal_salarios = total_mensal_salarios + salario_mensal
            i += 1
        print("Total mensal dos salários:", total_mensal_salarios)

    def escrever_arquivo_copa_mundo():
        # Criar arquivo CSV com os dados que o usuário digitar
        texto_arquivo = "Time1;Time2;Placar\n"

        i = 0
        while i < 3:
            time1: str = input("Time 1: ")
            time1_gols: int = int(input("Gols " + time1 + ": "))

            time2: str = input("Time 2: ")
            time2_gols: int = int(input("Gols " + time2 + ": "))

            placar = str(time1_gols) + "x" + str(time2_gols)

            # texto_arquivo = texto_arquivo + time1 + ";" + time2 + ";" + placar + "\n"
            # Interpolação de string (forma simplificada da linha acima)
            texto_arquivo += f"{time1};{time2};{placar}\n"
            print("\n\n\n--------------------------------")

            if time1_gols > time2_gols:
                print(f"Resultado: Time {time1} ganhou")
            elif time2_gols > time1_gols:
                print(f"Resultado: Time {time2} ganhou")
            else:
                print("Resultado: Empate")

            time.sleep(2)

            limpar_terminal = input ("Deseja limpar terminal: [y/n]")
            if limpar_terminal == "y":
                os.system("clear")

            i = i + 1

        # criar arquivo em python
        with open("placar.csv", "w", encoding="utf-8") as arquivo:
            arquivo.write(texto_arquivo)
            print("Arquivo 'placar.csv' criado com sucesso")

    escrever_arquivo_copa_mundo()


def exemplo_if():
    pass
exemplo_while()

