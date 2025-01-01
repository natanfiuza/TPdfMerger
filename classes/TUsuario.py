"""


Classes:
   Usuario - Table: ctl_usuario
   Data Criação: 
   Pacote: sig

"""
__author__ = "NatanFiuza - <n@taniel.com.br>"
__version__ = "0.1"

from os import stat
from classes.TDataBase import *
from classes.TPersistente import *
from math import floor
from typing import no_type_check


class TUsuario(TPersistente):

    def __init__(self, id, pDataBase, tableprefix=''):
        """
        Classe TUsuario
        Tem como herança a classe TPersistente

        Args:
            TPersistente (object): Classe que controla a interação com o banco de dados
        Atributos:    
            `id`, Tipo: Integer ,  Descricao:  

            `tipoUsuario`, Tipo: Integer ,  Descricao:  

            `identificadorPonto`, Tipo: String ,  Descricao:  

            `nomeUsuario`, Tipo: String ,  Descricao:  

            `senha`, Tipo: String ,  Descricao:  

            `idChatTelegram`, Tipo: Integer ,  Descricao:  

            `idChat_botTel_orcJB`, Tipo: Integer ,  Descricao:  

            `numCelularPrincipal`, Tipo: String ,  Descricao:  

            `email`, Tipo: String ,  Descricao:  

            `ativo`, Tipo: String ,  Descricao:  

            `idUsuarioCriador`, Tipo: Integer ,  Descricao:  

            `idPaginaInicial`, Tipo: Integer ,  Descricao:  

            `idColaborador`, Tipo: Integer ,  Descricao:  

            `AlterarOrdemPedido`, Tipo: String ,  Descricao:  

            `data_gravacao`, Tipo: datetime ,  Descricao:  

            `flagReuniaoPCP`, Tipo: Integer ,  Descricao: FLAG UTILIZADA PARA FILTRAR USU�RIOS QUE FAZEM PARA DE UMA REUNI�O DO PCP 

            `flagMotorista`, Tipo: Integer ,  Descricao: FLAG UTILIZADA PARA INFORMAR SE O USU�RIO � MOTORISTA 

            `flagMetaNotificada`, Tipo: Integer ,  Descricao:  

            `idUsuarioGestor`, Tipo: Integer ,  Descricao:  


        """
        from datetime import datetime
        self.__tablePrefix = tableprefix
        self.__nomeTabela = f"{tableprefix}ctl_usuario"
        self.__database = pDataBase
        self.__totalrows = ""  # Recebe o total de registro retornados na funcao busca
        # Atributos publicos dos campos da tabela
        self.id = 0
 

        # if self.__database.connected():
        #     self.createTable()  # Cria a tabela caso ela nao exista

        if TObject.isInteger(id) < 0:
            pass
            # import logging
            # logging.warning(self.__class__.__name__ +                            ".__init__  -> Valor de id nao e um inteiro ou maior igual a zero")

        elif TObject.isInteger(id) > 0:
            self.recupera(id=id, nomeTabela=self.__nomeTabela,
                          database=self.__database, setvalues=self.setValues)

    def insere(self):
        """
          Salva os dados no banco de dados
          Opcoes para adicionar quando for data e hora atual
            dataHora=TObject.nowDateTime("%Y-%m-%d %H:%M:%S")  
            Adicionar em sqlQuery e para o campo {dataHora}


          Returns: bool : Retorna verdadeiro se foi executado corretamente 

        """
        sqlQuery = """INSERT INTO {nomeTabela} (
	            id,tipoUsuario,identificadorPonto,nomeUsuario,senha,idChatTelegram,idChat_botTel_orcJB,numCelularPrincipal,email,ativo,idUsuarioCriador,idPaginaInicial,idColaborador,AlterarOrdemPedido,data_gravacao,flagReuniaoPCP,flagMotorista,flagMetaNotificada,idUsuarioGestor
				) VALUES (
				:id,:tipoUsuario,:identificadorPonto,:nomeUsuario,:senha,:idChatTelegram,:idChat_botTel_orcJB,:numCelularPrincipal,:email,:ativo,:idUsuarioCriador,:idPaginaInicial,:idColaborador,:AlterarOrdemPedido,:data_gravacao,:flagReuniaoPCP,:flagMotorista,:flagMetaNotificada,:idUsuarioGestor
        )""".format(nomeTabela=self.__nomeTabela)
        if int(self.id) <= 0:
            self.id = (self.lastId(nomeTabela=self.__nomeTabela,
                       database=self.__database) + 1)
        sqlQuery = self.writeToFields(sql_query=sqlQuery)

        return self.__database.execute(query=sqlQuery, data={})

    def altera(self):
        """
           Altera o registro atual no banco de dados
           Returns:
           [str]: Retorna verdadeiro caso a alteracao ocorra corretamente
        """
        sqlQuery = """UPDATE {nomeTabela} set
      
           tipoUsuario = :tipoUsuario,identificadorPonto = :identificadorPonto,nomeUsuario = :nomeUsuario,senha = :senha,idChatTelegram = :idChatTelegram,idChat_botTel_orcJB = :idChat_botTel_orcJB,numCelularPrincipal = :numCelularPrincipal,email = :email,ativo = :ativo,idUsuarioCriador = :idUsuarioCriador,idPaginaInicial = :idPaginaInicial,idColaborador = :idColaborador,AlterarOrdemPedido = :AlterarOrdemPedido,data_gravacao = :data_gravacao,flagReuniaoPCP = :flagReuniaoPCP,flagMotorista = :flagMotorista,flagMetaNotificada = :flagMetaNotificada,idUsuarioGestor = :idUsuarioGestor

           where  id = :id  """.format(nomeTabela=self.__nomeTabela)
        sqlQuery = self.writeToFields(sql_query=sqlQuery)
        return self.__database.execute(query=sqlQuery, data={})

    def writeToFields(self, sql_query):
        """
           Escreve os valores dos campos na query 
        Args:
            `sql_query` (str): *Query do banco de dados*

        Returns:
            [str]: Retorna a query com os campos alterados

        """
        sql_query = self.paramByName(sql_query, "id", self.id)  #
        sql_query = self.paramByName(sql_query, "chat_id", self.chat_id)  #
        sql_query = self.paramByName(sql_query, "email", self.email)  #
        
        self.primeiroNome = self.nome.split()[0].title() if len(
            self.nome.split()) > 1 else self.nome
        self.ultimoNome = self.nome.split(
        )[-1].title() if len(self.nome.split()) > 1 else ""
        return sql_query

    def setValues(self, row):
        """
           Define os campos a partir de uma row passada por parametro

        Args:
            row (list): Registro de retorno de uma cursor.fetchone
        """
        if not row == None:
            self.id = row['id']
            self.nomeUsuario = row['nomeUsuario']
            self.email = row['email']
            self.tipoUsuario = row['tipoUsuario']

        return True

    def save(self):
        if TObject.isInteger(self.id) > 0:
            self.altera()
        elif TObject.isInteger(self.id) == 0:
            self.insere()

    def busca(self, textoBusca="", tipoBusca="Tudo", idEmpresa=0, pg=0, rt=0, perPage=20):
        import math
        retorno = []
        if perPage <= 0:
            perPage = 20

        limit = ""
        where = ""

        if ((pg > 1) and (rt > 0)):
            np = math.ceil(rt / perPage)
            if (pg > np):  # verifica se o numero de paginas maior que o maximo
                pg = np
            ry = pg - 1
            r1 = ry * perPage
            r2 = ((pg * perPage) - 1)
            limit = " limit {} , {} ".format(r1, r2)

        sql = ""
        if (tipoBusca == "Tudo"):

            sql = "SELECT * FROM {} order by id  ".format(self.__nomeTabela)

        else:
            sql = "SELECT * FROM {} where   {}  like {}  order by {} {} ".format(
                self.__nomeTabela, tipoBusca, self.getSQLValueStringLike(textoBusca), tipoBusca, limit)

        self.__database.open(sql, None)
        registros = self.__database.fetch_all()
        self.__totalrows = len(registros)
        
        for value in registros:
            obj = TUsuario(0, self.__database, self.__tablePrefix)
            obj.setValues(value)
            retorno.append(obj)
        
        return retorno

    def rowsTotal(self):
        """Retorna o total de registros encontrados quando executada a funcao busca

        Returns:
            [integer]: [Total de registro encontrados]
        """
        return self.__totalrows

    def createTable(self):
        """
          Executa a criacao da tabela. 

        Args:
            nomeTabela (str): [description]
            database (TDataBase, optional): [description]. Defaults to TDataBase.
        """
        sqlQuery_mysql = """
       select count(*) from ctl_usuario
        
        """
        sqlQuery_sqlite = """
        CREATE TABLE IF NOT EXISTS  `usuarios` (
            `id` int(11) NOT NULL ,
            `email` varchar(255) DEFAULT NULL,
            `chat_id` varchar(255) DEFAULT NULL,
            `user_uuid` varchar(255) DEFAULT NULL,
            PRIMARY KEY (`id`),
         
          )        
        """
        if self.__database.sgdb == "sqlite":
            return self.__database.execute(sqlQuery_sqlite,data={})
        else:
            return self.__database.execute(sqlQuery_mysql,data={})
