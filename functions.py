"""
Varias funcos proprias
Criado: 2021-04-22

"""
# import cv2

from classes.TObject import TObject
from classes.TDataBase import TDataBase
from classes.TPersistente import TPersistente
from classes.TUsuario import TUsuario

from colorama import init
from colorama import Fore, Back, Style
import os
from os import walk
import json
import time
import glob
import codecs
#import logging
import shutil
import datetime
import subprocess
import requests
import uuid
from subprocess import Popen, PIPE

logo = """
 _   _       _               ___                          
( ) ( )     ( )_            (  _ \             
|  \| |  _ _|  _)  _ _  ___ | | ) |  __  _   _
|     |/ _  ) |  / _  )  _  \ | | )/ __ \ ) ( )  
| | \ | (_| | |_( (_| | ( ) | |_) |  ___/ \_/ | 
(_) (_)\__ _)\__)\__ _)_) (_)____/ \____)\___/


"""                                                               



def print_logo():
    print(logo) 


def externalIP():
    return requests.get('http://ipinfo.io/ip')


def open_json_file(filename= ""):
    """
    
    Open a JSON file and returns it.
    
    @param `filename`: Name of the JSON file
    @return  File handle
    """
    try:
        #os.path.join(json_config_dir, item)
        json_file = open(filename, "r")
        json_object = json.load(json_file)
        json_file.close()

    except FileNotFoundError as error:
        msg_error = f"File {filename} not found."
        #logging.error(msg_error)
        print("\x1b[43m\x1b[31m"+msg_error+" \x1b[0m")
        return ""
    except json.decoder.JSONDecodeError as error:
        msg_error = f"File {filename}: error in json decoder"
        #logging.error(msg_error)
        print("\x1b[43m\x1b[31m"+msg_error+" \x1b[0m")
        return ""
    return json_object


def save_json_file(filename="", json_object=[]):
    """
    
    Save a JSON file.
    
    @param `filename`: Name of the JSON file
    @param `json_object`: Object to save
    @return True if successful, False otherwise
    
    """
    try:    
        json_file = open(filename, "w+")
        json.dump(json_object, json_file)
        json_file.close()
    except:
        msg_error = f"Error on save file: {filename}."
        #logging.error(msg_error)
        print(msg_error)        
        return False

    return True


def check_dir(path, file_type="*.*"):
    """
    Check whether the "path" folder exists.
    If it exists list the files with the specified file_type
    @param `path`: path to check
    @param `file_type`: file type to filter (e.g., "*.txt", "document.*", "*.*")
    @return: list of files existing, otherwise empty list
    """
    if not os.path.exists(path):
        os.makedirs(path)
    return glob.glob(os.path.join(path, file_type))



def change_os_path_sep(path = ""):
    """
    
    Change \ or / to the default OS path separator in a given path.
    
    @param `path`: The path to change
    @return  Path changed, else False
    """
    path = path.replace('\\',os.path.sep)
    path = path.replace('/',os.path.sep)
    return path



def run_git_pull(source = ""):
     
    print(f"Run GIT PULL at {str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
    source = source.replace('\\','/')
    os.chdir(source)
    os.system("git pull")

def run_import(source = "", run_command=""):
     
    print(f"Run Import NFe at {str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
    #logging.info("Run Import NFe")
    source = source.replace('\\','/')
    os.chdir(source)
    os.system(run_command)

def get_value_tag(tag_name='',str=''):
    """
    Retorna um valor de substring retirado de uma tag xml
    """
    if tag_name=='':
        return False
    if str=='':
        return False
    
    return str[str.find(f"<{tag_name}>")+len(f"<{tag_name}>"):str.find(f"</{tag_name}>")]

def tag_exist(tag_name='',str=''):
    """
    Verifica se um TAG XML existe em uma string
    A funcçao verifica se </tag_name> existe em str
    """
    if tag_name=='':
        return False
    if str=='':
        return False
    
    return True if str.find(f"</{tag_name}>")>=0 else False

    
def ler_arquivo_para_lista(caminho_arquivo):
    """
    Lê um arquivo de texto e retorna uma lista onde cada linha do arquivo é um item.

    Args:
        caminho_arquivo: Uma string representando o caminho (path) completo para o arquivo de texto.

    Returns:
        Uma lista de strings, onde cada elemento é uma linha do arquivo.
        Retorna uma lista vazia se o arquivo não existir ou ocorrer um erro.
    """
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:  # 'r' para leitura, encoding='utf-8' para lidar com acentos e caracteres especiais
            linhas = arquivo.readlines()
        
        #Remover caracteres de nova linha (\n) do final de cada linha
        linhas_limpas = [linha.strip() for linha in linhas] #List comprehension
        return linhas_limpas


    except FileNotFoundError:
        print(f"Erro: Arquivo '{caminho_arquivo}' não encontrado.")
        return []  # Retorna uma lista vazia em caso de arquivo não encontrado
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return []  # Retorna uma lista vazia em caso de outros erros

def corrigir_caminho(caminho):
    """
    Corrige um caminho de arquivo (path) em string que usa barras invertidas duplas (\\\\)
    e o converte para um formato utilizável em Python, de três maneiras diferentes.

    Args:
        caminho: Uma string representando o caminho com barras invertidas duplas.

    Returns:
        Uma tupla com três strings:
            1. O caminho com barras invertidas simples ('\\').
            2. O caminho com barras normais ('/').
            3. O caminho utilizando os.path.normpath() para obter a representação
               canônica (a forma mais "correta" e portátil) do caminho.
        Retorna (None, None, None) se a entrada não for uma string.
    """
    if not isinstance(caminho, str):
        print("Erro: A entrada deve ser uma string.")
        return None, None, None

    # 1. Substituir \\ por \ (barras invertidas simples)
    caminho_barras_simples = caminho.replace("\\\\", "\\")

    # 2. Substituir \\ por / (barras normais)
    caminho_barras_normais = caminho.replace("\\\\", "/")

    # 3. Usar os.path.normpath() (MELHOR OPÇÃO)
    caminho_normalizado = os.path.normpath(caminho)

    return caminho_barras_simples, caminho_barras_normais, caminho_normalizado
