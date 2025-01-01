from dotenv import load_dotenv
import decorator
import html
import datetime
#import logging
import shutil
import sys
from config import *
from functions import *
from zipfile import ZipFile
from colorama import init
from colorama import Fore, Back, Style

import subprocess
import time
import os

## Biblioteca para tratar pdf
import PyPDF2


if getattr(sys, 'frozen', False):
    dirbase = os.path.dirname(sys.executable)
elif __file__:
    dirbase = os.path.dirname(__file__)


# from classes.TUsuario import TUsuario
# from classes.TNFeProc import TNFeProc
# from classes.TMDFeProc import TMDFeProc

#from bs4 import BeautifulSoup
#from bs4.element import Tag

__version__ = "0.0.2"

init()  # Iniciar colorama

load_dotenv()

# Banco de dados
database_port = os.getenv('DB_PORT')
database_host = os.getenv('DB_HOST')
database_user = os.getenv('DB_USER')
database_database = os.getenv('DB_DATABASE')
database_password = os.getenv('DB_PASSWORD')

# Parametros adicionais
#URL_API = os.getenv('URL_API_UPLOAD')



#logging.info(f"Start")


# database = TDataBase(host=database_host,
#                         user=database_user,
#                         password=database_password,
#                         sgdb='mysql',
#                         mydatabase=database_database)

# nfeproc = TNFeProc(id=0, pDataBase=database, tableprefix="")



def merge_pdfs(paths, output):
    """
    Mescla vários arquivos PDF em um único arquivo.

    Args:
        paths: Uma lista de caminhos para os arquivos PDF a serem mesclados.
        output: O caminho para o arquivo PDF de saída.
    """
    merger = PyPDF2.PdfMerger()

    for path in paths:
        with open(path, 'rb') as f:
            merger.append(f)

    with open(output, 'wb') as f:
        merger.write(f)

if __name__ == '__main__':
    if len(sys.argv) < 4:
        print("\n\nUso: python merge_pdf.py <arquivo1.pdf> <arquivo2.pdf> ... -output=<arquivo_saida.pdf>\n\n")
        sys.exit(1)

    paths = []
    output = None
    for arg in sys.argv[1:]:
        if arg.startswith('-output='):
            output = arg[8:]
        else:
            paths.append(arg)

    if not output:
        print("\n\nErro: O argumento -output é obrigatório.\n\n")
        sys.exit(1)

    merge_pdfs(paths, output)
    print(f"\n\nArquivos PDF mesclados com sucesso em {output}\n\n")




print(Style.RESET_ALL)

#logging.info(f"Finished")
