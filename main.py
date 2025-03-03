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


__version__ = "0.0.3"

init()  # Iniciar colorama

load_dotenv()


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
    if len(sys.argv) < 2:
        print(f"\nPdfMerger v{__version__}")
        print("\nUso: PdfMerger [<file1.pdf> <file2.pdf> ... || -inputlist=<arquivo_lista.txt>] -output=<arquivo_saida.pdf>\n\n")
        sys.exit(1)

    paths = []
    output = None
    inputlist_file = None
    for arg in sys.argv[1:]:
        if arg.startswith('-output='):
            output = arg[8:]
        elif arg.startswith('-inputlist='):   
            inputlist_file = arg[11:] 
        else:
            paths.append(arg)
    
    if inputlist_file:
        paths = ler_arquivo_para_lista(inputlist_file)

    if not output:
        print("\n\nErro: O argumento -output é obrigatório.\n\n")
        sys.exit(1)

    merge_pdfs(paths, output)
    print(f"\n\nArquivos PDF mesclados com sucesso em {output}\n\n")




print(Style.RESET_ALL)

#logging.info(f"Finished")
