"""
    Controla a conexao com o banco de dados
    Utlizando o mysql.connector
"""
__autor__ = "NatanFiuza - n@taniel.com.br"
__date__    = "13 Abril 2021"

from classes.TObject import *

import mysql.connector
import sqlite3
import logging

class TDataBase(TObject):
    
    lastrowid = 0
    rowcount = 0

    def __init__(self, host, user, password,sgdb, mydatabase):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__mydatabase = mydatabase
        self.__conectado = False
        self.__sgdb = sgdb
        if self.__sgdb == "mysql":
            try:
                self.__mydb = mysql.connector.connect(
                    host=self.__host,
                    user=self.__user,
                    password=self.__password,
                    database=self.__mydatabase				
                )
    
            except Exception as err:
                logging.error("Erro nao identificado: {}".format(err))
                print("Erro nao identificado: {}".format(err))
            else:
                logging.info("Conectado ao banco de dado: host={0},db={1}".format(self.__host,self.__mydatabase))
                self.__conectado = True
                self.__mycursor = self.__mydb.cursor(dictionary=True)

        elif self.__sgdb == "sqlite":
            try:
                self.__mydb = sqlite3.connect(self.mydatabase)
                self.__mydb.row_factory = self.__dict_factory
                self.__conectado = True
                self.__mycursor = self.__mydb.cursor()
            except sqlite3.OperationalError as err:
                logging.error("SGDB: {}, Erro sqlite3.OperationalError: {}".format(self.__sgdb,err))
                print("SGDB: {} ,Erro sqlite3.OperationalError: {}".format(self.__sgdb,err))  
            except Exception as err:
                logging.error("SGDB: {}, Erro nao identificado: {}".format(self.__sgdb,err))
                print("SGDB: {} ,Erro nao identificado: {}".format(self.__sgdb,err))    
   
    @property
    def mydatabase(self):
        return self.__mydatabase

    @property
    def sgdb(self):
        return self.__sgdb
    
    @mydatabase.setter
    def mydatabase(self,value):
        self.__mydatabase = value

    def execute(self,query,data,multi=False):
        """
        Executa comandos SQL no banco de dados

        Args:
            query (string): Os comandos SQL
            data (list): Lista com os campos para serem usados na query
            multi (bool): Determina se tem mais de um comando SQL, separados por ; 
        """
        if self.__sgdb == "mysql":
            try:            
                self.__mycursor.execute(query,data) 
                self.lastrowid = self.__mycursor.lastrowid    
                self.rowcount = self.__mycursor.rowcount
                self.commit()
            except Exception as err:
                logging.error("\\{TDataBase.execute\\} Erro não identificado: {}".format(err))
                print("Erro nao identificado: {}".format(err))
            else:
                return True

        if self.__sgdb == "sqlite":
            try:
                self.__mycursor.execute(query, data)
                self.lastrowid = self.__mycursor.lastrowid
                self.rowcount = self.__mycursor.rowcount
                self.commit()
            except sqlite3.OperationalError as err:
                logging.error(
                    "SGDB: {}, Erro sqlite3.OperationalError: {}".format(self.__sgdb, err))
                print("SGDB: {} ,Erro sqlite3.OperationalError: {}".format(
                    self.__sgdb, err))
            except Exception as err:
                logging.error("TDataBase.execute SGDB: {}, Erro não identificado: {}".format(
                    self.__sgdb, err))
                print("TDataBase.execute SGDB: {}, Erro nao identificado: {}".format(
                    self.__sgdb, err))
            else:
                return True
            
    def open(self,query,param):
        """
          Executa uma query do tipo SELECT 

        Args:
            query (string): [description]
            param (list): [description]
        """
        if self.__sgdb == "mysql":
            self.__mycursor.execute(query,param)     
            self.rowcount = self.__mycursor.rowcount
        if self.__sgdb == "sqlite":
            try:
                self.__mycursor.execute(query)
                self.rowcount = self.__mycursor.rowcount
            except Exception as err:
                logging.error(
                    "TDataBase.open Erro não identificado: {}".format(err))
                print("Query:\n {}".format(query))

            except sqlite3.OperationalError as err:
                logging.error(
                    "TDataBase.open OperationalError: {}".format(err))
                print("Query:\n {}".format(query))

            else:
                return True
    
    def fetch_all(self):
        return self.__mycursor.fetchall()

    def fetch_one(self):
        return self.__mycursor.fetchone()    

    def __dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def commit(self):
        """
           Executa o commit na conexao
        """
        self.__mydb.commit()

    def connected(self):
        return self.__conectado