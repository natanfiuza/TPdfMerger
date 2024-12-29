"""
    Funcoes e controles para objetos persistentes
"""
__autor__ = "NatanFiuza - n@taniel.com.br"
__date__    = "21 Abril 2021"

from classes.TObject import TObject
from classes.TDataBase import TDataBase


class TPersistente(TObject):


    def getSQLValueString(self,valor):
        """Adiciona o escape \ em caracteres nao alfanumericos
           
        Args:
            valor (str, optional): string para adicionar o escape '\' em caracteres nao alfa numericos. Defaults to "".

        Returns:
            string: Retorna a string convertida
        """
     
        if isinstance(valor, str):
            import re
            return "'"+re.escape(valor)+"'"
     
        if isinstance(valor, int):
            import re
            return "'"+re.escape(str(valor)) +"'"

        if isinstance(valor, float):
            import re
            return "'"+re.escape(str(valor)) +"'"

        return ''    

    def getSQLValueStringLike(self,valor):
        """
         Adiciona o escape \\ em caracteres nao alfanumericos
           
        Args:
            valor (str, optional): string para adicionar o escape '\\' em caracteres nao alfa numericos. Defaults to "".

        Returns:
            string: Retorna a string convertida
        """
     
        if isinstance(valor, str):
            import re

            return "'%"+re.escape(valor)+"%'"
     
        if isinstance(valor, int):
            import re
            valor = str(valor)
            return "'%"+re.escape(valor)+"%'"

        if isinstance(valor, float):
            import re
            valor = str(valor)
            return "'%"+re.escape(valor)+"%'"
  
    def recupera(self, id, nomeTabela , setvalues, database = TDataBase):
        """Recupera os valores de um registro usando id como busca

            id (integer): Identificador do registro
        Args:
            nomeTabela (string): Nome da tabela
            setvalues (func): Função do objeto que chama este funcao para popular os campos
            database (TDataBase, optional): Objeto TDataBase com a conexao do banco de dados. Defaults to TDataBase.

        Returns:
            bool : Retorna verdadeiro se a funcao passada em setvalues for executada corretamente
        """
        database.open(
            "SELECT * FROM {} WHERE id={} ".format(nomeTabela,self.getSQLValueString(id)), None)
    
        
        return setvalues(database.fetch_one())

    def lastId(self,nomeTabela, database = TDataBase):
        """
            Recupera o ultimo valor do registro id

        Args:
            nomeTabela (str): [description]
            database (TDataBase, optional): [description]. Defaults to TDataBase.
        
        Returns: 
             int : O valor do ultimo id  
        """    
        database.open(query = "SELECT max(id) as lastid FROM {nomeTabela}".format(nomeTabela = nomeTabela),param = {})
        row = database.fetch_one()
        return row['lastid']

    def exclui(self,id,nomeTabela,database = TDataBase):
        """
          Exclui o registro atual pelo id 

        Args:
            nomeTabela (str): [description]
            database (TDataBase, optional): [description]. Defaults to TDataBase.
        """
        return database.execute("DELETE FROM {nomeTabela} WHERE id='{id}' ".format(nomeTabela = nomeTabela,id = id))
    

    def paramByName(self,sql_query,pCampo,valor):
        """
           Renomeia os valores :<campo> para o valor do campo entre '' 


        Args:
            sql_query (str): SQL Query usada para as substituicoes  
            pCampo (str): Nome do campo 
            valor (str): Valor que sera substituido pelo nome do campo
        """
        erro = 0
        separador = " "
        prefixo = ":"

        if sql_query.find( prefixo + pCampo + " ") > 0:
            separador = " "
        
        if sql_query.find( prefixo + pCampo + ",") > 0:
            separador = ","
                   
        if sql_query.find( prefixo + pCampo + ")") > 0:
            separador = ")"
        
        if sql_query.find( prefixo +  pCampo + chr(13)) > 0:
            separador = chr(13)
            
        
        if sql_query.find( prefixo +  pCampo + chr(10)) > 0:
            separador = chr(10)
         
        
        if sql_query.find( prefixo +  pCampo + chr(9)) > 0:
            separador = chr(9)
           
        valor = str(valor)        
        return sql_query.replace(":"+pCampo + separador, self.getSQLValueString(valor)+separador )

    def listtoCSV(self,listobj,filename = "default.csv"):
        """
            Gera um csv de um objeto

        Args:
            listobj (list): [description]
            filename (str, optional): Nome do arquivo. Defaults to "default.csv".
        """
        if filename == "default":
            filename = "{}.csv".format(self.__class__.__name__)
        dd = {}
        fieldnames = []
        fn = listobj[0]
        for k in fn.__dict__:
                if isinstance(fn.__dict__[k],(float, int, str)):
                    if not "{}__".format(fn.__class__.__name__) in k:
                        fieldnames.append(k)
        import csv

        with open(filename, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
        
            for value in listobj:          
                for k in value.__dict__:
                    if isinstance(value.__dict__[k],(float, int, str)):
                        if not "{}__".format(value.__class__.__name__) in k:
                            dd[k] = value.__dict__[k]
                writer.writerow(dd) 

    def toJson(self):
        """Retorna o objeto no formato json

        Returns:
            [string]: Retorna uma string no formato json
        """
        import json
        dd = {}
        v1 = {}
        for k in self.__dict__:
            if isinstance(self.__dict__[k],(float, int, str)):
                if not "{}__".format(self.__class__.__name__) in k:
                    dd[k] = self.__dict__[k] 
        v1[self.__class__.__name__] = dd
        return json.dumps(v1)
    
    def toXML(self):
        """Retorna uma string no formato XML

        Returns:
            [string]: Retorna um XML do objeto
        """
        from xml.dom.minidom import parseString
        from dicttoxml import dicttoxml    # Atencao: Isntalar o modulo dicttoxml 
        dd = {}
        for k in self.__dict__:
            if isinstance(self.__dict__[k],(float, int, str)):
                if not "{}__".format(self.__class__.__name__) in k:
                    dd[k] = self.__dict__[k]    
        dom = parseString(dicttoxml(dd, custom_root=self.__class__.__name__))  
        return dom.toprettyxml()

    def toStr(self):              
        """Retorna uma string do objeto

        Returns:
            [string]: Retorna uma string com as propriedades do objeto
        """
        ident = "   "
        retorno = "{}:\n".format(self.__class__.__name__)
        for k in self.__dict__:
            if isinstance(self.__dict__[k],(float, int, str)):
                if not "{}__".format(self.__class__.__name__) in k:
                    retorno = "{}{}{}=\"{}\"\n".format(retorno,ident,k,self.__dict__[k]) 
        return retorno                       