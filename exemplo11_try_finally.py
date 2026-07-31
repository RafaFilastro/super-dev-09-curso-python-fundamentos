from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo


def exemplo_sem_erro():
    try:
        resultado = 10 / 2
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    finally:
        print("FINALLY: executei mesmo sem erro.")


def exemplo_com_erro():
    try:
        resultado = 10 / 0
        print("Resultado:", resultado)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")
    finally:
        print("FINALLY: executei mesmo com erro.")


def exemplo_tratar_criacao_diretorio():
    try:
        caminho_diretorio = Path("relatorios")
        caminho_diretorio.mkdir()
        print("Criado com sucesso")

    except FileExistsError:
        print("Diretório já existe")

    finally:
        mensagem = input("Digite uma mensagem para salvar no arquivo: ")

        fuso_horario = ZoneInfo("America/Sao_Paulo")
        data_hora_atual = datetime.now(fuso_horario)
        data_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        caminho_arquivo = caminho_diretorio / "relatorio-2026-07-29.txt"

        with open(
            caminho_arquivo,
            "a",
            encoding="UTF-8",
        ) as arquivo:
            arquivo.write(f"{data_formatada} - {mensagem}\n")

        print("Arquivo gerado")


if __name__ == "__main__":
    exemplo_tratar_criacao_diretorio()


if __name__ == "__main__":
    # exemplo_sem_erro()
    # exemplo_com_erro()
    exemplo_tratar_criacao_diretorio()
