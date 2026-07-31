# Criar um arquivo exercicios_for.py
# Ex.1: Criar uma função exercicio01
# Apresentar o texto "Bem vindo" 5 vezes utilizando for

def exercicio01():
    for i in range(0, 5):
        print("Bem vindo")


#exercicio01()

# Ex.2: Criar uma função exercicio02
# Apresentar os números de 15 até 30 utilizando for
# Exemplo de saída:
# 15
# 16
# 17
# ...
# 30

def exercicio02():
    for i in range(15, 31):
        print(i)


#exercicio02()


# Ex.3: Criar uma função exercicio03
# Solicitar um número inteiro para o usuário
# Utilizar for para apresentar a tabuada deste número de 1 até 10
# Não utilizar vetor/lista
# Exemplo:
# Digite um número: 5
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 10 = 50

def exercicio03():
    numero: int = int(input("Digite um número: "))
    for contador in range(1, 11):
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")



#exercicio03()


# Ex.4: Criar uma função exercicio04
# Solicitar 5 números inteiros para o usuário utilizando for
# Somar todos os números digitados
# Ao final, apresentar a soma total
# Não utilizar vetor/lista
# Exemplo:
# Digite o 1º número: 10
# Digite o 2º número: 5
# Digite o 3º número: 8
# Digite o 4º número: 2
# Digite o 5º número: 1
# Soma total: 26

def exercicio04():
    soma = 0
    for i in range(0, 5):
        numero: int = int(input("Digite um número: "))
        soma = soma + numero
    print(f"Soma total: {soma}")

#exercicio04()

#--------------------------------------------------
#Ex.5 - Criando um vetor com dados fixos
#--------------------------------------------------
#
#Função:
#exercicio05
#
#Objetivo:
#Criar um vetor chamado nomes e adicionar 4 nomes fixos, escritos diretamente no código.
#
#Regras:
#- Criar um vetor vazio chamado nomes
#- Adicionar os nomes utilizando append
#- Não utilizar for
#- Apresentar o vetor completo no final
#
#Exemplo:
#nomes = []
#nomes.append("Ana")
#nomes.append("Carlos")
#nomes.append("Maria")
#nomes.append("João")
#
#Saída esperada:
#["Ana", "Carlos", "Maria", "João"]

def exercicio05():
    nomes = []
    nomes.append("Ana")
    nomes.append("Carlos")
    nomes.append("Maria")
    nomes.append("João")

    print(f"Vetor posição 01 - {nomes[0]}")
    print(f"Vetor posição 02 - {nomes[1]}")
    print(f"Vetor posição 03 - {nomes[2]}")
    print(f"Vetor posição 04 - {nomes[3]}")

#exercicio05()


#--------------------------------------------------
#Ex.6 - Criando um vetor com frutas
#--------------------------------------------------
#
#Função:
#exercicio06
#
#Objetivo:
#Solicitar 3 frutas para o usuário e armazenar cada uma dentro de um vetor chamado frutas.
#
#Regras:
#- Criar um vetor vazio chamado frutas
#- Utilizar input para solicitar as frutas
#- Adicionar cada fruta no vetor utilizando append
#- Não utilizar for
#- Apresentar o vetor completo no final
#
#Exemplo:
#Digite a primeira fruta: Banana
#Digite a segunda fruta: Maçã
#Digite a terceira fruta: Uva
#
#Saída esperada:
#["Banana", "Maçã", "Uva"]

def exercicio06():
    frutas =[]

    primeira_fruta: str = input("Digite a primeira fruta: ")
    segunda_fruta: str = input("Digite a segunda fruta: ")
    terceira_fruta: str = input("Digite a terceira fruta: ")

    frutas.append(primeira_fruta)
    frutas.append(segunda_fruta)
    frutas.append(terceira_fruta)

    print(f"\nA primeira fruta digitada é: {frutas[0]}")
    print(f"A segunda fruta digitada é: {frutas[1]}")
    print(f"A terceira fruta digitada é: {frutas[2]}")


#exercicio06()

#--------------------------------------------------
#Ex.7 - Criando um vetor com números
#--------------------------------------------------
#
#Função:
#exercicio07
#
#Objetivo:
#Solicitar 4 números inteiros para o usuário e armazenar cada número dentro de um vetor chamado numeros.
#
#Regras:
#- Criar um vetor vazio chamado numeros
#- Utilizar input para solicitar os números
#- Converter cada valor digitado para int
#- Adicionar cada número no vetor utilizando append
#- Não utilizar for
#- Apresentar o vetor completo no final
#
#Exemplo:
#Digite o primeiro número: 10
#Digite o segundo número: 5
#Digite o terceiro número: 8
#Digite o quarto número: 2
#
#Saída esperada:
#[10, 5, 8, 2]

def exercicio07():
    numeros = []

    numero_um: int = int(input("Digite o primeiro número: "))
    numero_dois: int = int(input("Digite o segundo número: "))
    numero_tres: int = int(input("Digite o terceiro número: "))
    numero_quatro: int = int(input("Digite o quarto número: "))

    numeros.append(numero_um)
    numeros.append(numero_dois)
    numeros.append(numero_tres)
    numeros.append(numero_quatro)

    print(f"\nPrimeiro número digitado: {numeros[0]}")
    print(f"Segundo número digitado: {numeros[1]}")
    print(f"Terceiro número digitado: {numeros[2]}")
    print(f"Quarto número digitado: {numeros[3]}")
    print("O primeiro npumero", numeros[0])


#exercicio07()

#--------------------------------------------------
#Ex.8 - Manipulando um vetor de notas
#--------------------------------------------------
#
#Função:
#exercicio08
#
#Objetivo:
#Criar um vetor chamado notas, solicitar 4 notas para o usuário e depois realizar operações com esse vetor.
#
#Regras:
#- Criar um vetor vazio chamado notas
#- Utilizar input para solicitar as notas
#- Converter cada nota digitada para float
#- Adicionar cada nota no vetor utilizando append
#- Não utilizar for
#
#Depois de preencher o vetor, o programa deverá:
#
#1. Apresentar o vetor completo
#2. Apresentar a primeira nota digitada
#3. Apresentar a última nota digitada
#4. Alterar a segunda nota para 10
#5. Remover a terceira nota do vetor
#6. Apresentar o tamanho final do vetor
#7. Calcular a média das notas que ficaram no vetor
#8. Apresentar o vetor final
#9. Apresentar a média final
#
#Exemplo:
#Digite a primeira nota: 8
#Digite a segunda nota: 6
#Digite a terceira nota: 7
#Digite a quarta nota: 9
#
#Saída esperada:
#Vetor original: [8.0, 6.0, 7.0, 9.0]
#Primeira nota: 8.0
#Última nota: 9.0
#Vetor final: [8.0, 10.0, 9.0]
#Tamanho final: 3
#Média final: 9.0
#"""

def exercicio08():
    notas = []

    nota_um: float = float(input("Digite a primeira nota: "))
    nota_dois: float = float(input("Digite a segunda nota: "))
    nota_tres: float = float(input("Digite a terceira nota: "))
    nota_quatro: float = float(input("Digite a quarta nota: "))

    notas.append(nota_um)
    notas.append(nota_dois)
    notas.append(nota_tres)
    notas.append(nota_quatro)

    print(f"\nVetor original: {notas}")
    print(f"Primeira nota: {notas[0]}")
    print(f"Última nota: {notas[3]}")

    notas[1] = 10
    notas.pop(2)

    tamanho_final = len(notas)
    media_final = sum(notas) / tamanho_final

    print(f"\nVetor final: {notas}")
    print(f"Tamanho final: {tamanho_final}")
    print(f"Média final: {media_final}")


#exercicio08()

#==================================================
#EXERCÍCIOS DE PYTHON - FOR COM VETOR
#==================================================
#
#Arquivo:
#exercicios_for_vetores.py
#
#Orientações gerais:
#- Criar uma função para cada exercício.
#- Utilizar exatamente o nome da função indicado.
#- Utilizar vetor/lista.
#- Utilizar for.
#- Não utilizar while.
#- Testar uma função por vez, chamando a função no final do arquivo.
#
#
#
#--------------------------------------------------
#Ex.9 - Percorrendo um vetor de nomes
#--------------------------------------------------
#
#Função:
#exercicio09
#
#Objetivo:
#Criar um vetor chamado nomes com 5 nomes fixos e apresentar cada nome utilizando for.
#
#Regras:
#- Criar o vetor com dados escritos diretamente no código
#- Utilizar for para percorrer o vetor
#- Apresentar um nome por linha
#
#Exemplo de vetor:
#nomes = ["Ana", "Carlos", "Maria", "João", "Pedro"]
#
#Saída esperada:
#Ana
#Carlos
#Maria
#João
#Pedro

def exercicio09():
    nomes = ["Ana", "Carlos", "Maria", "João", "Pedro"]
    for nome in nomes:
        print(f"Os nomes cadastrados são: {nome}")


#exercicio09()

#--------------------------------------------------
#Ex.10 - Cadastrando frutas em um vetor
#--------------------------------------------------
#
#Função:
#exercicio10
#
#Objetivo:
#Solicitar 5 frutas para o usuário, armazenar dentro de um vetor e depois apresentar todas as frutas cadastradas.
#
#Regras:
#- Criar um vetor vazio chamado frutas
#- Utilizar for para solicitar as 5 frutas
#- Utilizar append para adicionar cada fruta no vetor
#- Utilizar outro for para apresentar as frutas cadastradas
#
#Exemplo:
#Digite uma fruta: Banana
#Digite uma fruta: Maçã
#Digite uma fruta: Uva
#Digite uma fruta: Laranja
#Digite uma fruta: Melancia
#
#Saída esperada:
#Frutas cadastradas:
#Banana
#Maçã
#Uva
#Laranja
#Melancia

def exercicio10():
    frutas = []
    for i in range(1, 6):
        frutas_digitadas: str = input("Digite uma fruta: ")
        frutas.append(frutas_digitadas)
    for fruta in frutas:
        print(f"As frutas digitadas são: {fruta}")


#exercicio10()

#--------------------------------------------------
#Ex.11 - Somando números de um vetor
#--------------------------------------------------

#Função:
#exercicio11
#
#Objetivo:
#Solicitar 5 números inteiros para o usuário, armazenar dentro de um vetor e apresentar a soma total.
#
#Regras:
#- Criar um vetor vazio chamado numeros
#- Utilizar for para solicitar os 5 números
#- Converter cada valor digitado para int
#- Adicionar cada número no vetor
#- Utilizar outro for para somar os valores do vetor
#- Apresentar o vetor completo
#- Apresentar a soma total
#
#Exemplo:
#Digite um número: 10
#Digite um número: 5
#Digite um número: 8
#Digite um número: 2
#Digite um número: 1
#
#Saída esperada:
#Números digitados: [10, 5, 8, 2, 1]
#Soma total: 26

def exercicio11():
    numeros = []
    for i in range(1, 6):
        numeros_inteiros: int = int(input("Digite um número: "))
        numeros.append(numeros_inteiros)

    soma_total = 0

    for numero in numeros:
        soma_total = soma_total + numero

    print(f"Os números digitados são: {numeros}")
    print(f"A soma de todos os numeros: {soma_total}")


#exercicio11()

#--------------------------------------------------
#Ex.12 - Contando números pares
#--------------------------------------------------

#Função:
#exercicio12
#
#Objetivo:
#Solicitar 6 números inteiros para o usuário, armazenar dentro de um vetor e contar quantos números pares foram digitados.
#
#Regras:
#- Criar um vetor vazio chamado numeros
#- Utilizar for para solicitar os 6 números
#- Converter cada valor digitado para int
#- Adicionar cada número no vetor
#- Utilizar outro for para verificar quais números são pares
#- Apresentar o vetor completo
#- Apresentar a quantidade de números pares
#
#Dica:
#Um número é par quando o resto da divisão por 2 é igual a 0.
#
#Exemplo:
#Digite um número: 4
#Digite um número: 7
#Digite um número: 10
#Digite um número: 3
#Digite um número: 8
#Digite um número: 1
#
#Saída esperada:
#Números digitados: [4, 7, 10, 3, 8, 1]
#Quantidade de números pares: 3

def exercicio12():
    numeros = []
    for i in range(1, 7):
        numeros_solicitados: int = int(input("Digite o número: "))
        numeros.append(numeros_solicitados)

    numeros_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            numeros_pares = numeros_pares + 1
            print(f"Os números pares são: {numero}")

    print(f"Números digitados: {numeros}")
    print(f"A quantidade de números pares: {numeros_pares}")


#exercicio12()

#--------------------------------------------------
#Ex.13 - Calculando média de notas
#--------------------------------------------------

#Função:
#exercicio13
#
#Objetivo:
#Solicitar 4 notas para o usuário, armazenar dentro de um vetor e calcular a média final.
#
#Regras:
#- Criar um vetor vazio chamado notas
#- Utilizar for para solicitar as 4 notas
#- Converter cada nota digitada para float
#- Adicionar cada nota no vetor
#- Utilizar outro for para somar as notas
#- Calcular a média
#- Apresentar o vetor completo
#- Apresentar a média final
#- Informar se o aluno foi aprovado ou reprovado
#
#Regra para aprovação:
#- Média maior ou igual a 7: aprovado
#- Média menor que 7: reprovado
#
#Exemplo:
#Digite uma nota: 8
#Digite uma nota: 7
#Digite uma nota: 6
#Digite uma nota: 9
#
#Saída esperada:
#Notas digitadas: [8.0, 7.0, 6.0, 9.0]
#Média final: 7.5
#Situação: Aprovado
#"""

def exercicio13():
    notas = []

    for i in range(1, 5):
        while True:
            notas_digitadas: float = float(input("Digite sua nota: "))

            if notas_digitadas < 0 or notas_digitadas > 10:
                print("Digite uma nota válida")
            else:
                notas.append(notas_digitadas)
                break

    soma_notas = 0

    for nota in notas:
        soma_notas = soma_notas + nota

    media_notas = soma_notas / len(notas)

    print(f"As notas digitadas são: {notas}")
    print(f"A média final: {media_notas}")

    if media_notas >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")


exercicio13()
