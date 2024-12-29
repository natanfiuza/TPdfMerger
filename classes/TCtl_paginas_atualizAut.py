"""


Classes:
   Tctl_paginas_atualizAut
   Data Criação: 20/04/2022
   Pacote: database

"""
__author__ = "NatanFiuza - <n@taniel.com.br>"
__version__ = "0.1"

from os import stat
from classes.TDataBase import *
from classes.TPersistente import *
from math import floor
from typing import no_type_check


class TCtl_paginas_atualizAut(TPersistente):
   
    def __init__(self, id, pDataBase, tableprefix):
        """
        Classe Tctl_paginas_atualizAut
        Tem como herança a classe TPersistente

        Args:
            TPersistente (object): Classe que controla a interação com o banco de dados
        Atributos:    
           `id`, Tipo: Integer ,  Descricao:  

           `nomePagina`, Tipo: String ,  Descricao:  

           `origemDados`, Tipo: String ,  Descricao:  

           `peso`, Tipo: String ,  Descricao:  

           `status`, Tipo: String ,  Descricao: Colocar em minutos 

           `periodoAtualizacao`, Tipo: Integer ,  Descricao:  

           `tempoAtualiz`, Tipo: Integer ,  Descricao:  

           `tempoEncConexao`, Tipo: Integer ,  Descricao:  

           `atualizMan`, Tipo: String ,  Descricao:  

           `codUltAtualiz`, Tipo: Integer ,  Descricao:  

           `ultimaAtualizacao`, Tipo: datetime ,  Descricao:  

        
        """ 
        from datetime import datetime
        self.__tablePrefix = tableprefix
        self.__nomeTabela = "{}ctl_paginas_atualizAut".format(tableprefix)
        self.__database = pDataBase
        self.__totalrows = ""  # Recebe o total de registro retornados na funcao busca
        # Atributos publicos dos campos da tabela 
        self.id = 0  #  
        self.nomePagina = ""  #  
        self.origemDados = ""  #  
        self.peso = ""  #  
        self.status = "ATIVO"  #  Colocar em minutos
        self.periodoAtualizacao = 0  #  
        self.tempoAtualiz = 0  #  
        self.tempoEncConexao = 0  #  
        self.atualizMan = "n"  #  
        self.codUltAtualiz = 0  #  
        self.ultimaAtualizacao = ""  #  


        if self.__database.connected():      
            self.createTable() # Cria a tabela caso ela nao exista
			
        if TObject.isInteger(id)<0:
            import logging
            logging.warning(self.__class__.__name__ +
                ".__init__  -> Valor de id nao e um inteiro ou maior igual a zero")
                
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
	            id,nomePagina,origemDados,peso,status,periodoAtualizacao,tempoAtualiz,tempoEncConexao,atualizMan,codUltAtualiz,ultimaAtualizacao
				) VALUES (
				:id,:nomePagina,:origemDados,:peso,:status,:periodoAtualizacao,:tempoAtualiz,:tempoEncConexao,:atualizMan,:codUltAtualiz,:ultimaAtualizacao
        )""".format(nomeTabela=self.__nomeTabela )
        if int(self.id) <=0:
            self.id = (self.lastId(nomeTabela = self.__nomeTabela,database = self.__database) +1)
        sqlQuery = self.writeToFields(sql_query=sqlQuery)  
  
        return self.__database.execute(query = sqlQuery,data = {})

    def altera(self):
        """
           Altera o registro atual no banco de dados
           Returns:
           [str]: Retorna verdadeiro caso a alteracao ocorra corretamente
        """
        sqlQuery = """UPDATE {nomeTabela} set
      
           nomePagina = :nomePagina,origemDados = :origemDados,peso = :peso,status = :status,periodoAtualizacao = :periodoAtualizacao,tempoAtualiz = :tempoAtualiz,tempoEncConexao = :tempoEncConexao,atualizMan = :atualizMan,codUltAtualiz = :codUltAtualiz,ultimaAtualizacao = :ultimaAtualizacao

           where  id = :id  and uuid = :uuid """.format(nomeTabela=self.__nomeTabela)
        sqlQuery = self.writeToFields(sql_query=sqlQuery)    
        return self.__database.execute(query = sqlQuery, data={})

    def writeToFields(self,sql_query):
        """
           Escreve os valores dos campos na query 
        Args:
            `sql_query` (str): *Query do banco de dados*

        Returns:
            [str]: Retorna a query com os campos alterados

        """
        sql_query = self.paramByName(sql_query,"id",self.id)  # 
        sql_query = self.paramByName(sql_query,"nomePagina",self.nomePagina)  # 
        sql_query = self.paramByName(sql_query,"origemDados",self.origemDados)  # 
        sql_query = self.paramByName(sql_query,"peso",self.peso)  # 
        sql_query = self.paramByName(sql_query,"status",self.status)  # Colocar em minutos
        sql_query = self.paramByName(sql_query,"periodoAtualizacao",self.periodoAtualizacao)  # 
        sql_query = self.paramByName(sql_query,"tempoAtualiz",self.tempoAtualiz)  # 
        sql_query = self.paramByName(sql_query,"tempoEncConexao",self.tempoEncConexao)  # 
        sql_query = self.paramByName(sql_query,"atualizMan",self.atualizMan)  # 
        sql_query = self.paramByName(sql_query,"codUltAtualiz",self.codUltAtualiz)  # 
        sql_query = self.paramByName(sql_query,"ultimaAtualizacao",self.ultimaAtualizacao)  # 

        return sql_query

    def setValues(self, row):
        """
           Define os campos a partir de uma row passada por parametro

        Args:
            row (list): Registro de retorno de uma cursor.fetchone
        """
        if not row == None:
           self.id = row['id'] # 
           self.nomePagina = row['nomePagina'] # 
           self.origemDados = row['origemDados'] # 
           self.peso = row['peso'] # 
           self.status = row['status'] # Colocar em minutos
           self.periodoAtualizacao = row['periodoAtualizacao'] # 
           self.tempoAtualiz = row['tempoAtualiz'] # 
           self.tempoEncConexao = row['tempoEncConexao'] # 
           self.atualizMan = row['atualizMan'] # 
           self.codUltAtualiz = row['codUltAtualiz'] # 
           self.ultimaAtualizacao = row['ultimaAtualizacao'] # 
           return True
    
    def save(self):
       if TObject.isInteger(self.id) >0:
           self.altera()
       elif TObject.isInteger(self.id)==0:  
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

            sql =  "SELECT * FROM {} order by id  ".format(self.__nomeTabela)          

        else:
            sql = "SELECT * FROM {} where   {}  like {}  order by {} {} ".format(self.__nomeTabela, tipoBusca, self.getSQLValueStringLike(textoBusca), tipoBusca ,limit)
     
        self.__database.open(sql,None)        
        registros = self.__database.fetch_all()        
        self.__totalrows = len(registros)
      
        for value in registros:
            obj = TCtl_paginas_atualizAut(0,self.__database, self.__tablePrefix )
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
        CREATE TABLE IF NOT EXISTS  `ctl_paginas_atualizAut` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomePagina` varchar(100) DEFAULT NULL,
  `origemDados` varchar(40) DEFAULT NULL,
  `peso` varchar(20) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'ATIVO' COMMENT 'Colocar em minutos',
  `periodoAtualizacao` int(11) DEFAULT NULL,
  `tempoAtualiz` int(11) DEFAULT NULL,
  `tempoEncConexao` int(11) DEFAULT NULL,
  `atualizMan` char(50) DEFAULT 'n',
  `codUltAtualiz` int(11) DEFAULT NULL,
  `ultimaAtualizacao` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8 ROW_FORMAT=COMPACT
        
        """
        sqlQuery_sqlite = """
        CREATE TABLE IF NOT EXISTS  `ctl_paginas_atualizAut` (
  `id` int(11) NOT NULL ,
  `nomePagina` varchar(100) DEFAULT NULL,
  `origemDados` varchar(40) DEFAULT NULL,
  `peso` varchar(20) DEFAULT NULL,
  `status` varchar(10) DEFAULT 'ATIVO' ,
  `periodoAtualizacao` int(11) DEFAULT NULL,
  `tempoAtualiz` int(11) DEFAULT NULL,
  `tempoEncConexao` int(11) DEFAULT NULL,
  `atualizMan` char(50) DEFAULT 'n',
  `codUltAtualiz` int(11) DEFAULT NULL,
  `ultimaAtualizacao` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
)
        
        """
    
        #return self.__database.execute(sqlQuery_mysql,[])
      
