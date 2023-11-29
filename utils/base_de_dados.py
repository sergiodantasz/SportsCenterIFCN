from os import getenv
from pathlib import Path

from dotenv import load_dotenv
from mysql.connector import connect

DOTENV_PATH = Path(__file__).resolve().parent.parent / '.env'

load_dotenv(DOTENV_PATH, override=True)


def consultar_registros(tabela: str, cursor) -> list[tuple]:
    operacao = (
        'SELECT * '
        f'FROM {tabela};'
    )
    cursor.execute(operacao)
    busca = cursor.fetchall()
    return busca


def apagar_registros(tabela: str, cursor, conexao: connect) -> None:
    operacao = (
        'DELETE '
        f'FROM {tabela};'
    )
    cursor.execute(operacao)
    conexao.commit()


if __name__ == '__main__':
    conexao = connect(
        database=getenv('DB_NAME', 'ALTERAR'),
        user=getenv('DB_USER', 'ALTERAR'),
        password=getenv('DB_PASSWORD', 'ALTERAR'),
        host=getenv('DB_HOST', 'ALTERAR')
    )
    cursor = conexao.cursor()

    # print('-' * 50)
    # for registro in consultar_registros('sportscenterifcn_usuario', cursor):
    #     for dado in registro:
    #         print(dado)
    #     print('-' * 50)

    # apagar_registros('sportscenterifcn_usuario', cursor, conexao)

    cursor.close()
    conexao.close()
