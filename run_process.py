from dotenv import load_dotenv
from config import *
from functions import *
from colorama import init
from colorama import Fore, Back, Style
import subprocess
import time
import os
import sys
import configparser
import shutil
import schedule
import logging
import datetime
__version__ = "0.0.1"


if getattr(sys, 'frozen', False):
    dirbase = os.path.dirname(sys.executable)
elif __file__:
    dirbase = os.path.dirname(__file__)

init() # Iniciar colorama
load_dotenv()


git_path = os.getenv('GIT_PATH')
schedule_git_pull_minutes = os.getenv('GIT_PULL_MINUTES')
import_run_command = os.getenv('IMPORT_COMMAND')
import_run_path = os.getenv('IMPORT_PATH')
import_run_minutes = os.getenv('IMPORT_RUN_MINUTES')

logging.info(f"Start")


# Removida pois nao a necessidade de executar o update a cada minuto, fazer isso manualmente quando atualizar 
#schedule.every(int(schedule_git_pull_minutes)).minutes.do(run_git_pull,source=git_path)
schedule.every(int(import_run_minutes)).minutes.do(run_import,source=import_run_path,run_command=import_run_command)

logging.info(f"Start:  {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
print(f"Start: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

while True:
    schedule.run_pending()
    time.sleep(1)