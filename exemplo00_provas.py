# Importa ABC e abstractmethod do módulo abc.
# Não precisa instalar, pois já fazem parte do Python.
from abc import ABC, abstractmethod


# Cria a classe Pessoa.
# Ao colocar ABC entre parênteses, Pessoa torna-se uma classe abstrata.
class Pessoa(ABC):

    # __init__ é o construtor da classe.
    # Ele é executado automaticamente quando um objeto é criado.
    def __init__(self, nome: str, telefone: str):

        # self representa o próprio objeto que está sendo criado.
        # Cria a propriedade nome e guarda o valor recebido.
        self.nome = nome

        # Cria a propriedade telefone e guarda o valor recebido.
        self.telefone = telefone

    # Método comum com retorno.
    # Ele monta e retorna os dados básicos da pessoa.
    def obter_dados_basicos(self):

        # return devolve um valor para quem chamou o método.
        return (
            f"Nome: {self.nome} - "
            f"Telefone: {self.telefone}"
        )

    # Indica que o método abaixo é abstrato.
    # Toda classe filha de Pessoa deverá criar esse método.
    @abstractmethod
    def apresentar_dados(self):

        # pass significa que não haverá código aqui.
        # A implementação será feita nas classes filhas.
        pass


# Professor é uma classe filha de Pessoa.
# Isso é herança: Professor herda de Pessoa.
class Professor(Pessoa):

    # Construtor da classe Professor.
    def __init__(self, nome: str, telefone: str, salario: float):

        # Chama o construtor da classe Pessoa.
        # Pessoa ficará responsável por guardar nome e telefone.
        super().__init__(nome, telefone)

        # Cria a propriedade salario, que pertence ao Professor.
        self.salario = salario

    # Implementação do método abstrato apresentar_dados.
    # Professor é obrigado a criar esse método por herdar de Pessoa.
    def apresentar_dados(self):

        # Chama o método obter_dados_basicos, herdado de Pessoa.
        # O valor retornado é guardado na variável dados_basicos.
        dados_basicos = self.obter_dados_basicos()

        # Mostra os dados do professor na tela.
        # Esse método não possui return, portanto é um método sem retorno explícito.
        print(
            f"{dados_basicos} - "
            f"Salário: R$ {self.salario:.2f}"
        )


# Cria a classe Curso.
class Curso:

    # Construtor da classe Curso.
    # Ele recebe o nome do curso e um objeto da classe Professor.
    def __init__(self, nome: str, professor: Professor):

        # Cria a propriedade nome do curso.
        self.nome = nome

        # Guarda um objeto Professor dentro do objeto Curso.
        # Isso é composição: um Curso tem um Professor.
        self.professor = professor

    # Método usado para apresentar os dados do curso.
    def apresentar_dados(self):

        # Mostra o nome do curso.
        print(f"Curso: {self.nome}")

        # Acessa o objeto professor que está dentro do curso.
        # Depois acessa a propriedade nome desse professor.
        print(f"Professor: {self.professor.nome}")


# Cria um objeto da classe Professor.
# Os valores são enviados para o construtor de Professor.
professor = Professor(
    "Carlos",
    "99999-9999",
    5000
)


# Cria um objeto da classe Curso.
curso = Curso(
    "Programação em Python",

    # Envia o objeto professor para dentro do objeto curso.
    professor
)


# Chama o método apresentar_dados do objeto professor.
professor.apresentar_dados()


# Chama o método apresentar_dados do objeto curso.
curso.apresentar_dados()

"""
Resumo para estudar

Orientação a objetos

É uma forma de organizar o programa usando classes e objetos. Uma classe reúne propriedades e métodos relacionados.

Classe

É um molde usado para criar objetos.

python
class Professor:
    pass

Objeto

É algo criado a partir de uma classe.

python
professor = Professor()

Construtor

É o método `__init__`. Ele é executado automaticamente quando o objeto é criado e recebe seus dados iniciais.

python
def __init__(self, nome):
    self.nome = nome

`self`

Representa o próprio objeto que está sendo criado ou utilizado.

python
self.nome = nome

O primeiro `nome`, em `self.nome`, é a propriedade do objeto.

O segundo `nome` é o valor recebido pelo construtor.

Propriedades

São os dados guardados dentro do objeto.

python
self.nome
self.telefone
self.salario

Também podem ser chamadas de atributos.

Métodos

São funções criadas dentro de uma classe. Representam ações do objeto.

python
def apresentar_dados(self):
    print(self.nome)

Método com retorno

Utiliza `return` para devolver um valor.

python
def obter_nome(self):
    return self.nome

O valor pode ser guardado em uma variável:

python
nome = professor.obter_nome()

Método sem retorno

Realiza uma ação, mas não devolve um valor explicitamente.

python
def apresentar_dados(self):
    print(self.nome)

Herança

Acontece quando uma classe filha aproveita propriedades e métodos de uma classe pai.

python
class Professor(Pessoa):

Significa:

> Professor é uma Pessoa.

`super()`

É usado para acessar métodos da classe pai.

python
super().__init__(nome, telefone)

Nesse exemplo, chama o construtor de `Pessoa` para guardar o nome e o telefone.

Abstração

Uma classe abstrata cria regras para as classes filhas.

python
class Pessoa(ABC):

    @abstractmethod
    def apresentar_dados(self):
        pass

Toda classe que herdar de `Pessoa` será obrigada a criar o método `apresentar_dados`.

python
class Professor(Pessoa):

    def apresentar_dados(self):
        print("Dados do professor")

Composição

Acontece quando um objeto possui outro objeto.

python
class Curso:
    def __init__(self, nome, professor):
        self.nome = nome
        self.professor = professor

Nesse exemplo:

> Um Curso tem um Professor.

Resumo do código

text
Pessoa
├── É uma classe abstrata
├── Possui nome e telefone
├── Possui método com retorno
└── Obriga as classes filhas a criar apresentar_dados

Professor
├── Herda de Pessoa
├── Usa super() para enviar nome e telefone para Pessoa
├── Possui salário
└── Implementa apresentar_dados

Curso
├── Possui um nome
├── Recebe um objeto Professor
└── Usa composição

Frases curtas para memorizar

text
Classe é o molde.

Objeto é algo criado com o molde.

Construtor prepara o objeto.

Propriedades guardam informações.

Métodos representam ações.

Return devolve um valor.

Herança significa "é um".

Composição significa "tem um".

Abstração cria regras para as classes filhas.


Para memorizar herança e composição, guarde principalmente esta diferença: Professor é uma Pessoa; Curso tem um Professor.
"""
