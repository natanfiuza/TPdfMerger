"""
    Arquivo de configuração do aplicativo

"""
import logging
logging.Logger.propagate = False
logging.basicConfig(filename='file_logging.log', level=logging.NOTSET,format='%(levelname)s|%(asctime)s|%(message)s', datefmt='%Y-%m-%d %H:%M:%S ')
logging.basicConfig(level=logging.WARNING)

from classes.TObject import TObject
#from classes.TDataBase import TDataBase