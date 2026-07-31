#--------------------------------------------------
#EXERCÍCIO 01 - Mensagens simples
#Função: exercicio_01_mensagens()
#--------------------------------------------------
#Crie uma função que mostre na tela algumas mensagens simples.
#
#A função deve apresentar:
#
#- Uma mensagem de boas-vindas
#- Uma mensagem dizendo que o aluno está aprendendo Python
#- Uma mensagem dizendo que Python é usado para criar programas
#
#Exemplo de saída:
#
#Bem-vindo ao Python!
#Estou aprendendo a programar.
#Python pode ser usado para criar vários tipos de programas.
#
#Neste exercício, use apenas print().
#Não use variáveis e não use input().

def mensagem():
    print("Bem-vindo ao python!")
    print("Estou aprendendo a programar")
    print("Python pode ser usado para criar varios tipos de programas")


#mensagem()

#--------------------------------------------------
#EXERCÍCIO 02 - Variáveis sem input
#Função: exercicio_02_variaveis()
#--------------------------------------------------
#Crie uma função que tenha três variáveis:
#
#- nome
#- idade
#- cidade
#
#Depois, mostre os dados na tela usando print().
#
#Exemplo de saída:
#
#Nome: Ana
#Idade: 15
#Cidade: Blumenau
#
#Neste exercício, os valores devem ser escritos diretamente no código.
#Não use input() ainda.

def variaveis():
    nome: str = "Ana"
    idade: int = 34
    cidade: str = "Blumenau"

    print(nome, "tem", idade, "anos, e mora em", cidade)

#variaveis()

#--------------------------------------------------
#EXERCÍCIO 03 - Input de texto
#Função: exercicio_03_input_nome()
#--------------------------------------------------
#Crie uma função que peça o nome do usuário usando input().
#
#Depois, mostre uma mensagem de boas-vindas usando o nome digitado.
#
#Exemplo:
#
#Digite seu nome: Carlos
#
#Saída esperada:
#
#Olá, Carlos! Seja bem-vindo ao sistema.
#
#Neste exercício, o valor digitado será tratado como texto.
#Não precisa converter o valor.

def pedir_dados():
    nome: str = input("Digite o primeiro nome: ")
    sobrenome: str = input("Digite o seu sobrenome: ")

    nome_completo: str = nome + " " + sobrenome + "!"

    print("Olá,", nome_completo, "Seja bem-vindo ao sistema")


#pedir_dados()

#--------------------------------------------------
#EXERCÍCIO 04 - Input com dados pessoais
#Função: exercicio_04_dados_pessoais()
#--------------------------------------------------
#Crie uma função que peça as seguintes informações ao usuário:
#
#- nome
#- bairro
#- cidade
#
#Depois, mostre uma frase completa usando esses dados.
#
#Exemplo:
#
#Digite seu nome: Maria
#Digite seu bairro: Centro
#Digite sua cidade: Blumenau
#
#Saída esperada:
#
#Maria mora no bairro Centro, na cidade de Blumenau.
#
#Neste exercício, todos os dados são textos.
#Não precisa usar int() ou float().

def pedir_dados_v2():
    nome: str = input("Digite o seu nome: ")
    sobrenome: str = input("Digite seu sobrenome: ")
    cidade: str = input("Digite a cidade que você mora: ")
    bairro: str = input("Digite o bairro que você mora: ")

    nome_completo: str = nome + " " + sobrenome

    print(nome_completo, "mora no bairro", bairro,  "que fica localizado na cidade de", cidade)


#pedir_dados_v2()

#--------------------------------------------------
#EXERCÍCIO 05 - Conversão de idade para int
#Função: exercicio_05_idade_int()
#--------------------------------------------------
#Crie uma função que peça a idade do usuário usando input().
#
#Depois, converta a idade para número inteiro usando int().
#
#Por fim, mostre a idade digitada.
#
#Exemplo:
#
#Digite sua idade: 16
#
#Saída esperada:
#
#Você tem 16 anos.
#
#Lembrete:
#O input() sempre retorna texto.
#Para transformar em número inteiro, use int().

def idade():
    idade: int = int(input("Digite a sua idade: "))

    print("Você tem", idade, "anos.")


#idade()

#--------------------------------------------------
#EXERCÍCIO 06 - Calculando idade no próximo ano
#Função: exercicio_06_idade_proximo_ano()
#--------------------------------------------------
#Crie uma função que peça o nome e a idade do usuário.
#
#A idade deve ser convertida para int.
#
#Depois, calcule qual será a idade da pessoa no próximo ano.
#
#Exemplo:
#
#Digite seu nome: João
#Digite sua idade: 15
#
#Saída esperada:
#
#João, no próximo ano você terá 16 anos.
#
#Neste exercício, será necessário:
#
#- Usar input() para ler o nome
#- Usar input() para ler a idade
#- Converter a idade usando int()
#- Somar 1 na idade

def calculo_idade():
    nome: str = input("Digite seu nome: ")
    idade: int = int(input("Digite o ano que você nasceu: "))

    idade_ano_que_vem: int = idade + 1

    print(nome, "no próximo ano você terá", idade_ano_que_vem, "anos.")


#calculo_idade()

#--------------------------------------------------
#EXERCÍCIO 07 - Dobro de um número inteiro
#Função: exercicio_07_dobro_numero()
#--------------------------------------------------
#Crie uma função que peça um número inteiro ao usuário.
#
#Depois, converta o valor para int.
#
#Em seguida, calcule e mostre o dobro desse número.
#
#Exemplo:
#
#Digite um número inteiro: 8
#
#Saída esperada:
#
#O dobro de 8 é 16.
#
#Neste exercício, será necessário converter o valor digitado antes de fazer o cálculo.

def dobro_numero():
    numero: int = int(input("Digite um número: "))
    numero_dobro: int = numero * 2

    print("O dobro de", numero, "é", numero_dobro)


#dobro_numero()

#--------------------------------------------------
#EXERCÍCIO 08 - Verificar maioridade
#Função: exercicio_08_maioridade()
#--------------------------------------------------
#Crie uma função que peça a idade do usuário.
#
#A idade deve ser convertida para int.
#
#Depois, use if para verificar se a pessoa é maior de idade.
#
#Regra:
#
#- Se a idade for maior ou igual a 18, mostre:
#  Você é maior de idade.
#
#- Caso contrário, mostre:
#  Você é menor de idade.
#
#Exemplo:
#
#Digite sua idade: 20
#
#Saída esperada:
#
#Você é maior de idade.

def maioridade():
    idade: int = int(input("Digite a sua idade: "))

    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade")

#maioridade()

#--------------------------------------------------
#EXERCÍCIO 09 - Verificar número positivo
#Função: exercicio_09_numero_positivo()
#--------------------------------------------------
#Crie uma função que peça um número inteiro ao usuário.
#
#O número deve ser convertido para int.
#
#Depois, use if para verificar se o número é positivo.
#
#Regra:
#
#- Se o número for maior que 0, mostre:
#  O número é positivo.
#
#- Caso contrário, mostre:
#  O número não é positivo.
#
#Exemplo:
#
#Digite um número: 5
#
#Saída esperada:
#
#O número é positivo.

def numero_positivo():
    numero: int = int(input("Digite um número: "))

    if numero >= 0:
        print("O numero é positivo")
    else:
        print("O número é negativo")

#numero_positivo()

#--------------------------------------------------
#EXERCÍCIO 10 - Verificar se pode entrar no evento
#Função: exercicio_10_entrada_evento()
#--------------------------------------------------
#Crie uma função que peça o nome e a idade de uma pessoa.
#
#A idade deve ser convertida para int.
#
#Depois, use if para verificar se a pessoa pode entrar em um evento.
#
#Regra:
#
#- Se a idade for maior ou igual a 16, mostre:
#  Nome da pessoa, você pode entrar no evento.
#
#- Caso contrário, mostre:
#  Nome da pessoa, você não pode entrar no evento.
#
#Exemplo:
#
#Digite seu nome: Ana
#Digite sua idade: 15
#
#Saída esperada:
#
#Ana, você não pode entrar no evento.

def entrada_evento():
    nome: str = input("Digite o seu nome: ")
    idade: int = int(input("Digite a sua idade: "))

    if idade >= 16:
        print(nome, "pode entrar no evento.")
    else:
        print(nome, "você não pode entrar no evento.")


#entrada_evento()

#--------------------------------------------------
#EXERCÍCIO 11 - Verificar nota do aluno
#Função: exercicio_11_verificar_nota()
#--------------------------------------------------
#Crie uma função que peça a nota de um aluno.
#
#A nota deve ser convertida para float.
#
#Depois, use if para verificar se o aluno foi aprovado.
#
#Regra:
#
#- Se a nota for maior ou igual a 7, mostre:
#  Aluno aprovado.
#
#- Caso contrário, mostre:
#  Aluno reprovado.
#
#Exemplo:
#
#Digite a nota do aluno: 8.5
#
#Saída esperada:
#
#Aluno aprovado.

def verificar_nota():
    nota: float = float(input("Digite a sua nota: "))

    if nota >= 7:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")


#verificar_nota()

#--------------------------------------------------
#EXERCÍCIO 12 - Verificar saldo para compra
#Função: exercicio_12_verificar_saldo()
#--------------------------------------------------
#Crie uma função que peça:
#
#- saldo disponível
#- valor da compra
#
#Os dois valores devem ser convertidos para float.
#
#Depois, use if para verificar se a pessoa pode realizar a compra.
#
#Regra:
#
#- Se o saldo for maior ou igual ao valor da compra, mostre:
#  Compra aprovada.
#
#- Caso contrário, mostre:
#  Saldo insuficiente.
#
#Exemplo:
#
#Digite seu saldo: 100
#Digite o valor da compra: 75.50
#
#Saída esperada:
#
#Compra aprovada.

def verificar_saldo():
    saldo_disponivel: float = float(input("Digite o saldo disponivel: "))
    valor_compra: float = float(input("Digite o valor da compra: "))

    if saldo_disponivel >= valor_compra:
        print("Compra aprovada!")
    else:
        print("Compra negada!")


#verificar_saldo()

#--------------------------------------------------
#EXERCÍCIO 13 - Aprovação com nota e frequência
#Função: exercicio_13_aprovacao_nota_frequencia()
#--------------------------------------------------
#Crie uma função que peça:
#
#- nota do aluno
#- frequência do aluno
#
#A nota deve ser convertida para float.
#A frequência deve ser convertida para int.
#
#Depois, use if com and para verificar se o aluno foi aprovado.
#
#Regra:
#
#- Se a nota for maior ou igual a 7 e a frequência for maior ou igual a 75, mostre:
#  Aluno aprovado.
#
#- Caso contrário, mostre:
#  Aluno reprovado.
#
#Exemplo:
#
#Digite a nota: 8
#Digite a frequência: 80
#
#Saída esperada:
#
#Aluno aprovado.
#
#Neste exercício, use o operador and.

def nota_frequencia():
    nota_aluno: float = float(input("Digite a nota: "))
    frequencia: int = int(input("Digite a frequencia: "))

    if nota_aluno >= 7 and frequencia >= 75:
        print("Aluno aprovado")
    else:
        print("Aluno reprovado")


#nota_frequencia()

#--------------------------------------------------
#EXERCÍCIO 14 - Entrada gratuita
#Função: exercicio_14_entrada_gratuita()
#--------------------------------------------------
#Crie uma função que peça a idade da pessoa.
#
#A idade deve ser convertida para int.
#
#Depois, use if com or para verificar se a pessoa tem entrada gratuita.
#
#Regra:
#
#- Se a idade for menor que 6 ou maior ou igual a 60, mostre:
#  Entrada gratuita.
#
#- Caso contrário, mostre:
#  Entrada paga.
#
#Exemplo:
#
#Digite sua idade: 65
#
#Saída esperada:
#
#Entrada gratuita.
#
#Neste exercício, use o operador or.

def entrada_gratuita():
    idade: int = int(input("Digite a sua idade: "))

    if idade <= 6 or idade >= 60:
        print("Entrada gratuita")
    else:
        print("Entrada paga")


#entrada_gratuita()

#--------------------------------------------------
#EXERCÍCIO 15 - Login simples
#Função: exercicio_15_login_simples()
#--------------------------------------------------
#Crie uma função que peça:
#
#- usuário
#- senha
#
#Depois, use if com and para verificar se o login está correto.
#
#Regra:
#
#- Se o usuário for igual a "admin" e a senha for igual a "1234", mostre:
#  Login realizado com sucesso.
#
#- Caso contrário, mostre:
#  Usuário ou senha incorretos.
#
#Exemplo:
#
#Digite o usuário: admin
#Digite a senha: 1234
#
#Saída esperada:
#
#Login realizado com sucesso.
#
#Neste exercício, use o operador and.

def login_simples():
    usuario: str = input("Digite o usuario: ")
    senha: int = int(input("Digite a senha: "))

    if usuario == "admin" and senha == 1234:
        print("Login realizado com sucesso!")
    else:
        print("Usúario ou senha incorretos")


#login_simples()

#--------------------------------------------------
#EXERCÍCIO 16 - Mostrar uma mensagem várias vezes
#Função: exercicio_16_mensagem_varias_vezes()
#--------------------------------------------------
#Crie uma função que mostre a mensagem "Estou aprendendo Python" cinco vezes usando while.
#
#Saída esperada:
#
#Estou aprendendo Python
#Estou aprendendo Python
#Estou aprendendo Python
#Estou aprendendo Python
#Estou aprendendo Python
#
#Neste exercício, será necessário:
#
#- Criar uma variável contador começando em 1
#- Usar while
#- Mostrar a mensagem na tela
#- Somar 1 no contador a cada repetição
#
#Atenção:
#Não use for neste exercício.
#Use apenas while.

def mensagem_varias_vezes():

    i = 0
    while i < 5:
        print("Estou aprendendo Python")
        i = i + 1


#mensagem_varias_vezes()

#--------------------------------------------------
#EXERCÍCIO 17 - Mostrar números pares até 20
#Função: exercicio_17_numeros_pares()
#--------------------------------------------------
#Crie uma função que mostre os números pares de 2 até 20 usando while.
#
#A saída esperada deve ser:
#
#2
#4
#6
#8
#10
#12
#14
#16
#18
#20
#
#Neste exercício, será necessário:
#
#- Criar uma variável numero começando em 2
#- Usar while
#- Mostrar o valor da variável numero
#- Somar 2 na variável a cada repetição
#
#Atenção:
#Não use for neste exercício.
#Use apenas while.

def numeros_pares():
    i = 0
    while i < 22:
        print(i)
        i = i + 2


#numeros_pares()

#--------------------------------------------------
#EXERCÍCIO 18 - Repetir mensagem
#Função: exercicio_18_repetir_mensagem()
#--------------------------------------------------
#Crie uma função que peça uma mensagem e uma quantidade de vezes.
#
#Depois, mostre a mensagem na tela repetindo a quantidade informada.
#
#Exemplo:
#
#Digite uma mensagem: Olá
#Digite a quantidade de vezes: 3
#
#Saída esperada:
#
#Olá
#Olá
#Olá
#
#Neste exercício, será necessário:
#
#- Usar input() para ler a mensagem
#- Usar input() para ler a quantidade
#- Converter a quantidade para int()
#- Usar while para repetir a mensagem

def repetir_mensagem():
    mensagem: str = input("Digite uma mensagem: ")
    quantidade: int = int(input("Digite a quantidade de vezes que será repetida: "))

    i: int = 0
    while i < quantidade:
            print(mensagem)
            i = i + 1


#repetir_mensagem()

#--------------------------------------------------
#EXERCÍCIO 19 - Somar números de 1 até N
#Função: exercicio_19_somar_1_ate_n()
#--------------------------------------------------
#Crie uma função que peça um número inteiro ao usuário.
#
#Depois, calcule a soma de todos os números de 1 até o número informado.
#
#Exemplo:
#
#Digite um número: 5
#
#Cálculo:
#
#1 + 2 + 3 + 4 + 5 = 15
#
#Saída esperada:
#
#A soma é 15.
#
#Neste exercício, será necessário:
#
#- Usar input()
#- Converter o valor para int()
#- Criar uma variável contador
#- Criar uma variável soma
#- Usar while para repetir a soma

def somar():
    numero: int = int(input("Digite um número: "))
    contador: int = 1
    soma: int = 0

    while contador <= numero:
        soma = soma + contador
        contador = contador + 1
    print("A soma é", soma)


#somar()

#--------------------------------------------------
#EXERCÍCIO 20 - Pedir senha até acertar
#Função: exercicio_20_senha_while()
#--------------------------------------------------
#Crie uma função que peça uma senha ao usuário.
#
#Enquanto a senha digitada for diferente de "1234", o programa deve pedir a senha novamente.
#
#Quando a senha estiver correta, mostre a mensagem:
#
#Acesso permitido.
#
#Exemplo:
#
#Digite a senha: 0000
#Senha incorreta. Tente novamente.
#
#Digite a senha: 1111
#Senha incorreta. Tente novamente.
#
#Digite a senha: 1234
#Acesso permitido.
#
#Neste exercício, será necessário:
#
#- Usar input()
#- Usar while
#- Comparar a senha digitada com "1234"
#- Repetir enquanto a senha estiver incorreta

def senha_while():
    senha: str = input("Digite uma senha")

    while senha != "1234":
        print("Senha incorreta. Tente novamente.")
        senha = input("Digite a senha: ")

    print("Acesso permitido")

#senha_while()

#--------------------------------------------------
#EXERCÍCIO 21 - Menu simples com while
#Função: exercicio_21_menu_simples()
#--------------------------------------------------
#Crie uma função que mostre um menu simples para o usuário.
#
#O menu deve aparecer enquanto o usuário não escolher a opção 0.
#
#Menu:
#
#1 - Mostrar mensagem de boas-vindas
#2 - Mostrar mensagem sobre Python
#0 - Sair
#
#Regras:
#
#- Se o usuário digitar 1, mostre:
#  Bem-vindo!
#
#- Se o usuário digitar 2, mostre:
#  Python é uma linguagem de programação.
#
#- Se o usuário digitar 0, mostre:
#  Programa encerrado.
#
#- Se o usuário digitar qualquer outro número, mostre:
#  Opção inválida.
#
#Neste exercício, será necessário:
#
#- Usar while
#- Usar input()
#- Converter a opção para int()
#- Usar if, elif e else dentro do while

def menu_simples():
    opcao: int = -1

    while opcao != 0:
        print("\n1 - Mostrar mensagem de boas-vindas")
        print("2 - Mostrar mensagem sobre Python")
        print("0 - Sair")

        opcao = int(input("Digite uma opção: "))

        if opcao == 1:
            print("Bem-vindo!")
        elif opcao == 2:
            print("Python é uma linguagem de programação.")
        elif opcao == 0:
            print("Programa encerrado.")
        else:
            print("opção invalida.")


#menu_simples()

#--------------------------------------------------
#EXERCÍCIO 22 - Tabuada com while
#Função: exercicio_22_tabuada_while()
#--------------------------------------------------
#Crie uma função que peça um número inteiro ao usuário.
#
#Depois, mostre a tabuada desse número de 1 até 10 usando while.
#
#Exemplo:
#
#Digite um número: 5
#
#Saída esperada:
#
#5 x 1 = 5
#5 x 2 = 10
#5 x 3 = 15
#5 x 4 = 20
#5 x 5 = 25
#5 x 6 = 30
#5 x 7 = 35
#5 x 8 = 40
#5 x 9 = 45
#5 x 10 = 50

def tabuada_while():
    numero: int = int(input("Digite um número"))
    contador: int = 1

    while contador <= 10:
        resultado: int = numero * contador

        print(numero, "x", contador, "=", resultado)

        contador = contador + 1

#tabuada_while()

#--------------------------------------------------
#EXERCÍCIO 23 - Somar números até digitar zero
#Função: exercicio_23_somar_ate_zero()
#--------------------------------------------------
#Crie uma função que peça números inteiros ao usuário.
#
#O programa deve continuar pedindo números enquanto o usuário não digitar 0.
#
#Quando o usuário digitar 0, o programa deve mostrar a soma de todos os números digitados.
#
#Exemplo:
#
#Digite um número: 5
#Digite um número: 3
#Digite um número: 2
#Digite um número: 0
#
#Saída esperada:
#
#A soma dos números digitados é 10.

def somar_ate_zero():
    soma: int = 0
    numero: int = int(input("Digite um número: "))

    while numero != 0:
        soma = soma + numero
        numero = int(input("Digite um numero: "))
    print("A soma dos números digitados é", soma)


#somar_ate_zero()

#--------------------------------------------------
#EXERCÍCIO 24 - Contar números positivos
#Função: exercicio_24_contar_positivos()
#--------------------------------------------------
#Crie uma função que peça números inteiros ao usuário.
#
#O programa deve continuar pedindo números enquanto o usuário não digitar 0.
#
#Ao final, mostre quantos números positivos foram digitados.
#
#Exemplo:
#
#Digite um número: 5
#Digite um número: -2
#Digite um número: 8
#Digite um número: 0
#
#Saída esperada:
#
#Quantidade de números positivos: 2

def contar_positivos():
    quantidade_positivos: int = 0
    numero: int = int(input("Digite um número: "))

    while numero != 0:
        if numero > 0:
            quantidade_positivos = quantidade_positivos + 1

        numero = int(input("Digite um número: "))

    print("Quantidade de números positivos:", quantidade_positivos)


#contar_positivos()

#--------------------------------------------------
#EXERCÍCIO 26 - Média de notas com while
#Função: exercicio_26_media_notas_while()
#--------------------------------------------------
#Crie uma função que peça 4 notas de um aluno usando while.
#
#Depois, calcule e mostre a média das notas.
#
#Exemplo:
#
#Digite a nota: 8
#Digite a nota: 7
#Digite a nota: 9
#Digite a nota: 6
#
#Saída esperada:
#
#A média do aluno é 7.5.
#
#Neste exercício, será necessário:
#
#- Criar um contador
#- Criar uma variável soma
#- Repetir até digitar 4 notas
#- Calcular a média no final

def media_notas():
    i: int = 0
    soma: float = 0

    while i < 4:
        nota: float = float(input("Digite a nota: "))
        soma = soma + nota
        i = i + 1

    media: float = soma / 4

    print("A média do aluno é", media)


#media_notas()

#--------------------------------------------------
#EXERCÍCIO 27 - Senha com limite de tentativas
#Função: exercicio_27_senha_tentativas()
#--------------------------------------------------
#Crie uma função que peça uma senha ao usuário.
#
#A senha correta é "1234".
#
#O usuário terá no máximo 3 tentativas para acertar.
#
#Regras:
#
#- Se acertar a senha, mostre:
#  Acesso permitido.
#
#- Se errar as 3 tentativas, mostre:
#  Acesso bloqueado.
#
#Exemplo:
#
#Digite a senha: 1111
#Senha incorreta.
#
#Digite a senha: 2222
#Senha incorreta.
#
#Digite a senha: 3333
#Senha incorreta.
#
#Acesso bloqueado.
#
#Neste exercício, será necessário usar while com contador de tentativas.

def senha_tentativas():
    tentativas: int = 0
    senha_correta: str = "1234"

    while tentativas < 3:
        senha_digitada: str = input("Digite a senha: ")

        if senha_digitada == senha_correta:
            print("Acesso liberado!")
            return
        print("Senha incorreta.")
        tentativas = tentativas + 1
    print("Acesso bloqueado.")

senha_tentativas()

#--------------------------------------------------
#EXERCÍCIO 28 - Validar idade
#Função: exercicio_28_validar_idade()
#--------------------------------------------------
#Crie uma função que peça a idade do usuário.
#
#A idade deve estar entre 0 e 120.
#
#Enquanto o usuário digitar uma idade inválida, o programa deve pedir novamente.
#
#Quando a idade for válida, mostre a mensagem:
#
#Idade cadastrada com sucesso.
#
#Exemplo:
#
#Digite sua idade: -5
#Idade inválida. Digite novamente.
#
#Digite sua idade: 150
#Idade inválida. Digite novamente.
#
#Digite sua idade: 16
#Idade cadastrada com sucesso.

def validar_idade():
    idade: int = int(input("Digite sua idade: "))

    while idade < 0 or idade > 120:
        print("Idade inválida. Digite novamente.")
        idade = int(input("Digite sua idade: "))

    print("Idade cadastrada com sucesso.")

validar_idade()

#--------------------------------------------------
#EXERCÍCIO 29 - Adivinhar número secreto
#Função: exercicio_29_adivinhar_numero()
#--------------------------------------------------
#Crie uma função com um número secreto definido no código.
#
#Exemplo:
#
#numero_secreto = 7
#
#Depois, peça para o usuário tentar adivinhar o número.
#
#Enquanto o usuário não acertar, continue pedindo um novo número.
#
#Regras:
#
#- Se o número digitado for maior que o número secreto, mostre:
#  O número secreto é menor.
#
#- Se o número digitado for menor que o número secreto, mostre:
#  O número secreto é maior.
#
#- Quando acertar, mostre:
#  Parabéns, você acertou!
#
#Exemplo:
#
#Digite um número: 5
#O número secreto é maior.
#
#Digite um número: 9
#O número secreto é menor.
#
#Digite um número: 7
#Parabéns, você acertou!

def adivinhar_numero():
    numero_secreto: int = 7
    numero_digitado: int = int(input("Digite um número: "))

    while numero_digitado != numero_secreto:

        if numero_digitado > numero_secreto:
            print("O número secreto é menor.")

        else:
            print("O número secreto é maior.")

        numero_digitado = int(input("Digite um número: "))

    print("Parabéns, você acertou!")


adivinhar_numero()

#--------------------------------------------------
#EXERCÍCIO 30 - Menu de operações
#Função: exercicio_30_menu_operacoes()
#--------------------------------------------------
#Crie uma função que mostre um menu até o usuário escolher a opção 0.
#
#Menu:
#
#1 - Somar dois números
#2 - Subtrair dois números
#3 - Multiplicar dois números
#0 - Sair
#
#Regras:
#
#- Se escolher 1, peça dois números e mostre a soma.
#- Se escolher 2, peça dois números e mostre a subtração.
#- Se escolher 3, peça dois números e mostre a multiplicação.
#- Se escolher 0, mostre:
#  Programa encerrado.
#
#- Se escolher qualquer outra opção, mostre:
#  Opção inválida.
#
#Neste exercício, será necessário:
#
#- Usar while para manter o menu funcionando
#- Usar input() para escolher a opção
#- Usar if, elif e else para verificar a opção escolhida
#- Usar int() ou float() para converter os números
#"""

def menu_operacoes():
    opcao: int = -1

    while opcao != 0:
        print("\n1 - Somar dois números")
        print("2 - Subtrair dois números")
        print("3 - Multiplicar dois números")
        print("0 - Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            numero_1: float = float(input("Digite o primeiro número: "))
            numero_2: float = float(input("Digite o segundo número: "))

            resultado: float = numero_1 + numero_2

            print("Resultado da soma:", resultado)

        elif opcao == 2:
            numero_1: float = float(input("Digite o primeiro número: "))
            numero_2: float = float(input("Digite o segundo número: "))

            resultado: float = numero_1 - numero_2

            print("Resultado da subtração:", resultado)

        elif opcao == 3:
            numero_1: float = float(input("Digite o primeiro número: "))
            numero_2: float = float(input("Digite o segundo número: "))

            resultado: float = numero_1 * numero_2

            print("Resultado da multiplicação:", resultado)

        elif opcao == 0:
            print("Programa encerrado.")

        else:
            print("Opção inválida.")


menu_operacoes()
