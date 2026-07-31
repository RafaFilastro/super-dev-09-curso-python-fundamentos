#EXERCÍCIOS DE PYTHON — PARTE 2
#
#Conteúdos:
#
#Revisão de while
#Contadores
#Acumuladores
#Validação de dados
#Maior e menor valor
#Menus
#for
#range()
#Listas
#append()
#remove()
#Operador in
#Percorrer listas
#Separar informações em listas
#
#Cada exercício deve ser feito dentro de uma função.
#
#Depois de criar a função, chame-a no final do arquivo para testar.
#
#Exemplo:
#
#def exercicio_31_exemplo():
#    print("Olá")
#
#
#exercicio_31_exemplo()
#Para testar apenas um exercício por vez, deixe somente a função desejada sendo chamada no final do arquivo.
#EXERCÍCIO 31 — Contar positivos, negativos e zeros
#Função:
#def exercicio_31_classificar_numeros():
#
#Peça 10 números inteiros ao usuário usando while.
#
#Durante a repetição, verifique se cada número é:
#
#Positivo
#Negativo
#Igual a zero
#
#Ao final, mostre quantos números de cada tipo foram digitados.
#
#Exemplo:
#
#Digite o número 1: 5
#Digite o número 2: -3
#Digite o número 3: 0
#Digite o número 4: 8
#Digite o número 5: -1
#Digite o número 6: 4
#Digite o número 7: 0
#Digite o número 8: 9
#Digite o número 9: -7
#Digite o número 10: 2
#
#Quantidade de positivos: 5
#Quantidade de negativos: 3
#Quantidade de zeros: 2
#
#Neste exercício, será necessário:
#
#Criar um contador para controlar as 10 repetições
#Criar um contador de positivos
#Criar um contador de negativos
#Criar um contador de zeros
#Usar if, elif e else
#Somar 1 no contador correspondente
#
#Sugestão de variáveis:
#
#contador = 1
#quantidade_positivos = 0
#quantidade_negativos = 0
#quantidade_zeros = 0
#
#Atenção:
#
#Não some o número digitado nos contadores.
#Os contadores devem aumentar apenas de 1 em 1.
#
#Exemplo:
#
#quantidade_positivos = quantidade_positivos + 1
#
#Não use for neste exercício.

def classificar_numeros():
    contador = 1

    quantidade_positivos = 0
    quantidade_negativos = 0
    quantidade_zeros = 0

    while contador <= 10:
        numero = int(input(f"Digite o número {contador}: "))

        if numero > 0:
            quantidade_positivos = quantidade_positivos + 1
        elif numero < 0:
            quantidade_negativos = quantidade_negativos + 1
        else:
            quantidade_zeros = quantidade_zeros + 1

        contador = contador + 1

    print()
    print("Quantidade de positivos:", quantidade_positivos)
    print("Quantidade de negativos:", quantidade_negativos)
    print("Quantidade de zeros:", quantidade_zeros)

#classificar_numeros()

#EXERCÍCIO 32 — Encontrar o maior e o menor número
#
#Função:
#
#def exercicio_32_maior_menor():
#
#Peça 6 números inteiros ao usuário usando while.
#
#Depois, mostre:
#
#O maior número digitado
#O menor número digitado
#
#Exemplo:
#
#Digite o número 1: 8
#Digite o número 2: -2
#Digite o número 3: 15
#Digite o número 4: 4
#Digite o número 5: 20
#Digite o número 6: 1
#
#Maior número: 20
#Menor número: -2
#
#Neste exercício, será necessário:
#
#Criar um contador
#Pedir 6 números
#Guardar o primeiro número como maior e menor
#Comparar os próximos números
#Atualizar o maior quando necessário
#Atualizar o menor quando necessário
#
#Dica importante:
#
#No primeiro número digitado, faça:
#
#if contador == 1:
#    maior = numero
#    menor = numero
#
#Depois, nos próximos números:
#
#if numero > maior:
#    maior = numero
#
#if numero < menor:
#    menor = numero
#
#Não comece o maior com zero, pois o usuário pode digitar apenas números negativos.
#
#Exemplo problemático:
#
#maior = 0
#
#Se o usuário digitar:
#
#-10
#-5
#-3
#-8
#-20
#-6
#
#O programa mostraria zero como maior, mesmo que zero não tenha sido digitado.
#
#Não use max() nem min() neste exercício.

def maior_menor():
    contador = 1

    maior = 0
    menor = 0

    while contador <= 6:
        numero: int = int(input("Digite o número: "))

        if contador == 1:
            maior = numero
            menor = numero
        else:
            if numero > maior:
                maior = numero
            if numero < menor:
                menor = numero


        contador = contador + 1

    print()
    print("Maior número digitado:", maior)
    print("Menor número digitado:", menor)

#maior_menor()

#EXERCÍCIO 33 — Média de notas com validação
#
#Função:
#
#def exercicio_33_media_validada():
#
#Peça 4 notas ao usuário usando while.
#
#Cada nota deve estar entre 0 e 10.
#
#Se a nota for inválida, mostre:
#
#Nota inválida. Digite novamente.
#
#Uma nota inválida não deve:
#
#Ser somada
#Aumentar o contador
#
#Depois de receber as 4 notas válidas, calcule a média.
#
#Regras:
#
#Média maior ou igual a 7: aluno aprovado
#Média maior ou igual a 5 e menor que 7: aluno em recuperação
#Média menor que 5: aluno reprovado
#
#Exemplo:
#
#Digite a nota 1: 8
#Digite a nota 2: 15
#Nota inválida. Digite novamente.
#
#Digite a nota 2: 6
#Digite a nota 3: -2
#Nota inválida. Digite novamente.
#
#Digite a nota 3: 7
#Digite a nota 4: 5
#
#Média: 6.5
#Aluno em recuperação.
#
#Neste exercício, será necessário:
#
#Criar uma variável de soma
#Criar um contador
#Validar cada nota
#Somar apenas notas válidas
#Calcular a média depois do while
#Usar if, elif e else
#
#Sugestão:
#
#contador = 1
#soma = 0.0
#
#A validação pode ser feita assim:
#
#if nota >= 0 and nota <= 10:
#
#Ou assim:
#
#if 0 <= nota <= 10:
#
#Somente dentro dessa condição você deve:
#
#soma = soma + nota
#contador = contador + 1
#
#Não use listas neste exercício.

def media_validada():
    contador: int = 1
    soma: float = 0.0


    while contador <= 4:
        nota: float = float(input(f"Digite a nota {contador}: "))

        if 0 <= nota <= 10:
            soma = soma + nota
            contador = contador + 1
        else:
            print("Nota inválida. Digite novamente.")

    media: float = soma / 4

    print()
    print("Média:", media)

    if media >= 7:
        print("Aluno aprovado.")
    elif media >= 5:
        print("Aluno em recuperação.")


#media_validada()

#EXERCÍCIO 34 — Caixa eletrônico
#Função:
#def exercicio_34_caixa_eletronico():
#Crie um programa que simule um caixa eletrônico.
#O saldo inicial deve ser:
#saldo = 1000.0
#Mostre o seguinte menu:
#1 - Consultar saldo
#2 - Depositar dinheiro
#3 - Sacar dinheiro
#0 - Sair
#O menu deve continuar aparecendo até o usuário escolher a opção 0.

#Regras:

#Opção 1 — Consultar saldo
#Mostre:
#Saldo disponível: R$ 1000.00
#Opção 2 — Depositar
#Peça o valor do depósito.
#O valor deve ser maior que zero.
#Se for válido, adicione-o ao saldo.
#Exemplo:

#Digite o valor do depósito: 250
#Depósito realizado com sucesso.
#Novo saldo: R$ 1250.00
#Se o valor for zero ou negativo:
#Valor de depósito inválido.
#Opção 3 — Sacar
#Peça o valor do saque.
#O saque deve:
#Ser maior que zero
#Não ser maior que o saldo disponível
#Se o saque for válido:
#Saque realizado com sucesso.
#Novo saldo: R$ 800.00
#Se for maior que o saldo:
#Saldo insuficiente.
#Se for zero ou negativo:
#Valor de saque inválido.
#Opção 0 — Sair
#Mostre:

#Caixa eletrônico encerrado.
#Qualquer outra opção
#Mostre:

#Opção inválida.
#Neste exercício, será necessário:
#Usar while
#Criar um menu
#Usar if, elif e else
#Atualizar o saldo
#Validar depósitos
#Validar saques
#Usar soma e subtração
#Para depositar:
#saldo = saldo + valor_deposito
#Para sacar:
#saldo = saldo - valor_saque

def caixa_eletronico():
    opcao: int = -1
    saldo: float = 1000.00

    while opcao != 0:
        print("\n====== CAIXA ELETRÔNICO ======")
        print("1 - Consultar saldo")
        print("2 - Depositar dinheiro")
        print("3 - Sacar dinheiro")
        print("0 - Sair")
        opcao = int(input("Digite a opção: "))

        if opcao == 1:
            print(f"\nSaldo disponível: R$ {saldo:.2f}")

        elif opcao == 2:
            valor_depositado:float = float(input("Digite o valor do depósito: R$ "))
            if valor_depositado > 0:
                saldo = saldo + valor_depositado
                print("Valor depositado com sucesso")
                print(f"Novo saldo: R$ {saldo:.2f}")
            else:
                print("Valor de depósito inválido.")

        elif opcao == 3:
            valor_saque: float = float(input("Digite o valor de saque: R$ "))

            if valor_saque <= 0:
                print("Valor de saque inválido.")
            elif valor_saque > saldo:
                print("Valor insuficiente.")
            else:
                saldo = saldo - valor_saque
                print("Saque realizado com sucesso")
                print(f"Novo saldo: R$ {saldo:.2f}")

        elif opcao == 0:
            print("\nPrograma encerrado")
        else:
            print("Opção inválida!")


#caixa_eletronico()


#EXERCÍCIO 35 — Número secreto com limite de tentativas
#
#Função:
#
#def exercicio_35_numero_secreto_tentativas():
#
#Crie um número secreto diretamente no código:
#
#numero_secreto = 27
#
#O usuário terá no máximo 5 tentativas para acertar.
#
#A cada tentativa:
#
#Se o número for menor, informe que o número secreto é maior
#Se o número for maior, informe que o número secreto é menor
#Se acertar, encerre a repetição
#
#Exemplo:
#
#Tentativa 1 de 5
#Digite um número: 10
#O número secreto é maior.
#
#Tentativa 2 de 5
#Digite um número: 40
#O número secreto é menor.
#
#Tentativa 3 de 5
#Digite um número: 27
#Parabéns! Você acertou em 3 tentativas.
#
#Se o usuário errar as 5 tentativas:
#
#Suas tentativas acabaram.
#O número secreto era 27.
#
#Neste exercício, será necessário:
#
#Criar um contador de tentativas
#Usar while
#Verificar se o usuário acertou
#Controlar o limite de tentativas
#Mostrar quantas tentativas foram utilizadas
#Encerrar antes das 5 tentativas caso acerte
#
#Sugestão de variáveis:
#
#tentativas = 0
#acertou = False
#
#A repetição pode continuar enquanto:
#
#while tentativas < 5 and acertou == False:
#
#Ou, de forma mais simples:
#
#while tentativas < 5 and not acertou:
#
#Quando o usuário acertar:
#
#acertou = True

def numero_secreto():
    numero_secreto: int = 27
    tentativas: int = 0
    acertou: bool = False
    while tentativas < 5 and not acertou:
        tentativas = tentativas + 1

        print(f"\nTentativa {tentativas} de 5")
        numero = int(input("Digite um numero: "))

        if numero < numero_secreto:
            print("O numero secreto é maior.")
        elif numero > numero_secreto:
            print("O numero secreto é menor.")
        else:
            acertou = True
            print(f"Parabéns! Você acertou em {tentativas} tentativas.")
    if not acertou:
        print("\nSuas tentativas acabaram.")
        print(f"O número secreto era {numero_secreto}.")


#numero_secreto()

#EXERCÍCIOS COM FOR
#
#O for é usado para repetir uma ação percorrendo uma sequência.
#
#Exemplo:
#
#for numero in range(1, 6):
#    print(numero)
#
#Saída:
#
#1
#2
#3
#4
#5
#
#Atenção:
#
#O último número do range() não é incluído.
#
#Por isso:
#
#range(1, 6)
#
#gera:
#
#1, 2, 3, 4, 5

def numero_1_ate_20():
    for numero in range(1, 21):
        print(numero)


#numero_1_ate_20()


#EXERCÍCIO 37 — Mostrar números pares de 2 até 50
#
#Função:
#
#def exercicio_37_pares_com_for():
#
#Mostre todos os números pares de 2 até 50 usando for.
#
#Saída esperada:
#
#2
#4
#6
#8
#10
#...
#48
#50
#
#Faça duas versões.
#
#Versão 1
#
#Percorra todos os números de 1 até 50.
#
#Dentro do for, use if para descobrir se o número é par.
#
#Um número é par quando:
#
#numero % 2 == 0
#Versão 2
#
#Configure o próprio range() para aumentar de 2 em 2.
#
#Estrutura:
#
#range(inicio, fim, passo)
#
#Exemplo:
#
#range(2, 11, 2)
#
#gera:
#
#2, 4, 6, 8, 10
#
#Não use while.
#

def numero_par_1_50():
    for numero in range(1, 51):
        if numero % 2 == 0:
            print(numero)

    print("\nVersão com o range: ")
    for numero1 in range(2, 51, 2):
        print(numero1)


#numero_par_1_50()

#EXERCÍCIO 38 — Contagem regressiva
#
#Função:
#
#def exercicio_38_contagem_regressiva():
#
#Faça uma contagem regressiva de 10 até 1 usando for.
#
#Depois, mostre:
#
#Fogo!
#
#Saída esperada:
#
#10
#9
#8
#7
#6
#5
#4
#3
#2
#1
#Fogo!
#
#Neste exercício, será necessário usar o passo negativo do range().
#
#Exemplo:
#
#range(5, 0, -1)
#
#gera:
#
#5, 4, 3, 2, 1
#
#Atenção:
#
#Quando o passo é negativo, o número inicial deve ser maior que o número final.
#

def contagem_regressiva():
    for numero in range(10, 0 , -1):
        print(numero)
    print("Fogo!")


#contagem_regressiva()

#EXERCÍCIO 39 — Tabuada usando for
#
#Função:
#
#def exercicio_39_tabuada_for():
#
#Peça um número inteiro ao usuário.
#
#Depois, mostre a tabuada desse número de 1 até 10 usando for.
#
#Exemplo:
#
#Digite um número: 7
#
#7 x 1 = 7
#7 x 2 = 14
#7 x 3 = 21
#7 x 4 = 28
#7 x 5 = 35
#7 x 6 = 42
#7 x 7 = 49
#7 x 8 = 56
#7 x 9 = 63
#7 x 10 = 70
#
#Neste exercício, será necessário:
#
#Pedir um número
#Converter para int
#Usar for
#Usar range()
#Multiplicar o número pelo contador
#
#Sugestão:
#
#resultado = numero * contador
#
#Não use while.
#

def tabuada_com_for():
    numero: int = int(input("Digite um numero: "))
    for contador in range(1, 11):
        resultado = numero * contador
        print(f"{numero} x {contador} = {resultado}")

#tabuada_com_for()

#EXERCÍCIO 40 — Somar números de 1 até N usando for
#
#Função:
#
#def exercicio_40_somar_com_for():
#
#Peça um número inteiro positivo ao usuário.
#
#Depois, some todos os números de 1 até o número informado.
#
#Exemplo:
#
#Digite um número: 5
#
#1 + 2 + 3 + 4 + 5 = 15
#
#Soma total: 15
#
#Neste exercício, será necessário:
#
#Criar uma variável acumuladora
#Usar for
#Usar range()
#Somar o número atual ao total
#
#Sugestão:
#
#soma = 0
#
#Dentro do for:
#
#soma = soma + numero
#
#Atenção:
#
#A variável soma deve ser criada antes da repetição.
#
#O resultado final deve ser mostrado depois do for.
#

def somar_com_for():
    soma = 0
    numero_inteiro: int = int(input("Digite um número: "))
    for numero in range(1, numero_inteiro + 1):
        soma = soma + numero
    print(soma)


#somar_com_for()


#EXERCÍCIO 41 — Contar números pares e ímpares
#
#Função:
#
#def exercicio_41_pares_impares():
#
#Peça 8 números inteiros usando for.
#
#Para cada número digitado, verifique se ele é par ou ímpar.
#
#Ao final, mostre a quantidade de pares e ímpares.
#
#Exemplo:
#
#Digite o número 1: 5
#Digite o número 2: 8
#Digite o número 3: 2
#Digite o número 4: 9
#Digite o número 5: 11
#Digite o número 6: 6
#Digite o número 7: 4
#Digite o número 8: 3
#
#Quantidade de pares: 4
#Quantidade de ímpares: 4
#
#Neste exercício, será necessário:
#
#Criar um contador de pares
#Criar um contador de ímpares
#Usar for
#Usar %
#Usar if e else
#
#Sugestão de variáveis:
#
#quantidade_pares = 0
#quantidade_impares = 0
#
#Para descobrir se é par:
#
#if numero % 2 == 0:

def numero_par_impar_com_for():
    numero_par = 0
    numero_impar = 0
    for repeticao in range(1, 9):
        numero: int = int(input("Digite um numero"))
        while numero <= 0:
            print("Número incorreto")
            numero: int = int(input("Digite um número novamente: "))
        if numero % 2 == 0:
            numero_par = numero_par + 1
        else:
            numero_impar = numero_impar + 1
    print(f"\nQuantidade de numeros par: {numero_par}")
    print(f"Quantidade de numeros impera: {numero_impar}")


#numero_par_impar_com_for()


#EXERCÍCIO 42 — Média da turma
#
#Função:
#
#def exercicio_42_media_turma():
#
#Primeiro, pergunte quantos alunos existem na turma.
#
#Depois, peça a nota de cada aluno usando for.
#
#Ao final, mostre:
#
#A média da turma
#A quantidade de alunos com nota maior ou igual a 7
#A quantidade de alunos com nota menor que 7
#
#Exemplo:
#
#Digite a quantidade de alunos: 4
#
#Digite a nota do aluno 1: 8
#Digite a nota do aluno 2: 5
#Digite a nota do aluno 3: 7
#Digite a nota do aluno 4: 9
#
#Média da turma: 7.25
#Alunos com nota maior ou igual a 7: 3
#Alunos com nota menor que 7: 1
#
#Neste exercício, será necessário:
#
#Pedir a quantidade de alunos
#Criar uma variável para somar as notas
#Criar dois contadores
#Usar for
#Calcular a média depois da repetição
#
#Sugestão:
#
#soma_notas = 0.0
#aprovados = 0
#reprovados = 0
#
#Para calcular a média:
#
#media = soma_notas / quantidade_alunos
#
#Desafio adicional:
#
#Valide cada nota para aceitar somente valores entre 0 e 10.

def notas_alunos():
    soma_notas: float = 0.0
    reprovados: int = 0
    aprovados: int = 0

    alunos: int = int(input("Digite a quantidade de alunos: "))

    while alunos <= 0:
        print("Quantidade de alunos inválida.")

        alunos = int(input("Digite uma quantidade maior que zero: "))

    for sala_aula in range(1, alunos + 1):
        nota: float = float(input(f"Digite a nota do aluno {sala_aula}: "))

        while nota < 0 or nota > 10:
            print("Nota inválida, Digite uma nota entre 0 e 10.")
            nota = float(input(f"Digite novamente a nota do aluno {alunos}: "))

        soma_notas = soma_notas + nota

        if nota >= 7:
            aprovados = aprovados + 1
        else:
            reprovados = reprovados + 1

    media_notas: float = soma_notas / alunos
    print(f"QUantidade de alunos aprovados: {aprovados}")
    print(f"Quantidade de alunos reprovados: {reprovados}")
    print(f"A media da turma ficou em: {media_notas}")


#notas_alunos()

#
#EXERCÍCIOS COM LISTAS
#
#Em Python, o conteúdo que muitas vezes é chamado de vetor é normalmente trabalhado com uma lista.
#
#Exemplo:
#
#nomes = ["Ana", "Carlos", "Maria"]
#
#Uma lista vazia é criada assim:
#
#nomes = []
#
#Para adicionar um valor:
#
#nomes.append("João")
#
#Para percorrer a lista:
#
#for nome in nomes:
#    print(nome)

def lista_nomes():
    nomes = []
    nomes.append("Rafael")
    nomes.append("Morgana")

    for nome in nomes:
        print(nome)


#lista_nomes()


#EXERCÍCIO 43 — Cadastrar nomes em uma lista
#
#Função:
#
#def exercicio_43_lista_nomes():
#
#Crie uma lista vazia.
#
#Depois, peça 5 nomes ao usuário usando for.
#
#Cada nome digitado deve ser adicionado à lista.
#
#Ao final, mostre todos os nomes cadastrados.
#
#Exemplo:
#
#Digite o nome 1: Ana
#Digite o nome 2: Carlos
#Digite o nome 3: Maria
#Digite o nome 4: João
#Digite o nome 5: Fernanda
#
#Nomes cadastrados:
#
#Ana
#Carlos
#Maria
#João
#Fernanda
#
#Neste exercício, será necessário:
#
#Criar uma lista vazia
#Usar for
#Usar input()
#Usar append()
#Percorrer a lista depois do cadastro
#
#Sugestão:
#
#nomes = []
#
#Para cadastrar:
#
#nome = input("Digite um nome: ")
#nomes.append(nome)
#
#Depois, para mostrar:
#
#for nome in nomes:
#    print(nome)

def usuario_digitar_nome():
    nomes = []
    for repeticao in range(1, 6):
        nome_digitado = input(f"Digite o nome {repeticao}: ")
        nomes.append(nome_digitado)

    print("\nlista completa:")
    print(nomes)

    print("\nNomes cadastrados:")
    for nome in nomes:
        print(nome)


usuario_digitar_nome()

