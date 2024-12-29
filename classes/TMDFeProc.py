"""


Classes:
   TMDFeProcs
   Data Criação: 2023-01-30
   Pacote: sig

"""
__author__ = "NatanFiuza - <n@taniel.com.br>"
__version__ = "0.1"

from os import stat
from classes.TDataBase import *
from classes.TPersistente import *
from math import floor
from typing import no_type_check


class TMDFeProc(TPersistente):
   
    def __init__(self, id, pDataBase, tableprefix):
        """
        Classe Tmdfe_procs
        Tem como herança a classe TPersistente

        Args:
            TPersistente (object): Classe que controla a interação com o banco de dados
        Atributos:    
           `id`, Tipo: Integer ,  Descricao:  

           `cliente_gprint_id`, Tipo: Integer ,  Descricao: Identifica o cliente no GPrint 

           `versao`, Tipo: String ,  Descricao: Vers�o do XML, do mdfeProc 

           `chMDFe`, Tipo: String ,  Descricao: Chave da Nota fiscal 

           `uuid`, Tipo: String ,  Descricao: Identificador Unico interno do MDFe 

           `cUF`, Tipo: String ,  Descricao: Codigo da UF do emitente do Manifesto de Documentos Fiscais Eletr�nico. Utilizar a Tabela do IBGE 

           `nMDF`, Tipo: String ,  Descricao: Numero do Manifesto 

           `cMDF`, Tipo: String ,  Descricao: Codigo numerico que compoe a Chave de Acesso. 

           `cDV`, Tipo: String ,  Descricao: Digito Verificador da Chave de Acesso da NF-e 

           `tpTransp`, Tipo:  ,  Descricao: Tipo do Transportador.	1 - ETC / 2 - TAC / 3 - CTC  

           `modal`, Tipo:  ,  Descricao: Modalidade de transporte. 1 - Rodovi�rio; 2 - A�reo; 3 - Aquavi�rio; 4 - Ferrovi�rio. 

           `dhEmi`, Tipo: date ,  Descricao: Data e hora de emiss�o do Manifesto. (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00 

           `tpEmis`, Tipo:  ,  Descricao: Forma de emiss�o do Manifesto. 1 - Normal; 2 - Conting�ncia; 3-Regime Especial NFF 

           `procEmi`, Tipo: String ,  Descricao: Processo de emiss�o utilizado com a seguinte codifica��o: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco 

           `verProc`, Tipo: String ,  Descricao: Vers�o do aplicativo utilizado no processo de emiss�o 

           `UFIni`, Tipo: String ,  Descricao: Sigla da UF do Carregamento. 

           `veicTracao_placa`, Tipo: String ,  Descricao: Registra a placa do veiculo 

           `veicTracao_tara`, Tipo: Integer ,  Descricao: Tara do veiculo 

           `veicTracao_capKG`, Tipo: Integer ,  Descricao: Capacidade de carga do veiculo em KG 

           `veicTracao_capM3`, Tipo: Integer ,  Descricao: Capacidade de carga do veiculo em Metro Cubico 

           `veicTracao_condutor_xNome`, Tipo: String ,  Descricao: Nome do condutor do veiculo 

           `veicTracao_condutor_CPF`, Tipo: String ,  Descricao: CPF do condutor do veiculo 

           `veicTracao_tpRod`, Tipo:  ,  Descricao: Tipo de rodado. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros 

           `veicTracao_tpCar`, Tipo:  ,  Descricao: Tipo de Carroceria. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros 

           `veicTracao_UF`, Tipo: String ,  Descricao: UF em que veiculo esta licenciado 

           `emit_CNPJ`, Tipo: String ,  Descricao: Numero do CNPJ do emitente 

           `emit_CPF`, Tipo: String ,  Descricao: Numero do CPF do emitente 

           `emit_xNome`, Tipo: String ,  Descricao: Razao Social ou Nome do emitente 

           `tot_qCTe`, Tipo: String ,  Descricao: Quantidade total de CT-e relacionados no Manifesto 

           `tot_qNFe`, Tipo: String ,  Descricao: Quantidade total de NF-e relacionadas no Manifesto 

           `tot_qMDFe`, Tipo: String ,  Descricao: Quantidade total de MDFe relacionados no Manifesto Aquaviario 

           `tot_vCarga`, Tipo: Float ,  Descricao: Valor total da carga / mercadorias transportadas 

           `tot_cUnid`, Tipo:  ,  Descricao: Codigo da unidade de medida do Peso Bruto da Carga / Mercadorias transportadas. 01 - KG; 02 - TON 

           `created_at`, Tipo: timestamp ,  Descricao:  

           `updated_at`, Tipo: timestamp ,  Descricao:  

        
        """ 
        from datetime import datetime
        self.__tablePrefix = tableprefix
        self.__nomeTabela = "{}mdfe_procs".format(tableprefix)
        self.__database = pDataBase
        self.__totalrows = ""  # Recebe o total de registro retornados na funcao busca
        # Atributos publicos dos campos da tabela 
        self.id = 0  #  
        self.cliente_gprint_id = 0  #  Identifica o cliente no GPrint
        self.versao = ""  #  Vers�o do XML, do mdfeProc
        self.chMDFe = ""  #  Chave da Nota fiscal
        self.uuid = ""  #  Identificador Unico interno do MDFe
        self.cUF = ""  #  Codigo da UF do emitente do Manifesto de Documentos Fiscais Eletr�nico. Utilizar a Tabela do IBGE
        self.nMDF = ""  #  Numero do Manifesto
        self.cMDF = ""  #  Codigo numerico que compoe a Chave de Acesso.
        self.cDV = ""  #  Digito Verificador da Chave de Acesso da NF-e
        self.tpTransp = ""  #  Tipo do Transportador.	1 - ETC / 2 - TAC / 3 - CTC 
        self.modal = ""  #  Modalidade de transporte. 1 - Rodovi�rio; 2 - A�reo; 3 - Aquavi�rio; 4 - Ferrovi�rio.
        self.dhEmi = ""  #  Data e hora de emiss�o do Manifesto. (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
        self.tpEmis = ""  #  Forma de emiss�o do Manifesto. 1 - Normal; 2 - Conting�ncia; 3-Regime Especial NFF
        self.procEmi = ""  #  Processo de emiss�o utilizado com a seguinte codifica��o: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco
        self.verProc = ""  #  Vers�o do aplicativo utilizado no processo de emiss�o
        self.UFIni = ""  #  Sigla da UF do Carregamento.
        self.veicTracao_placa = ""  #  Registra a placa do veiculo
        self.veicTracao_tara = 0  #  Tara do veiculo
        self.veicTracao_capKG = 0  #  Capacidade de carga do veiculo em KG
        self.veicTracao_capM3 = 0  #  Capacidade de carga do veiculo em Metro Cubico
        self.veicTracao_condutor_xNome = ""  #  Nome do condutor do veiculo
        self.veicTracao_condutor_CPF = ""  #  CPF do condutor do veiculo
        self.veicTracao_tpRod = ""  #  Tipo de rodado. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros
        self.veicTracao_tpCar = ""  #  Tipo de Carroceria. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros
        self.veicTracao_UF = ""  #  UF em que veiculo esta licenciado
        self.emit_CNPJ = ""  #  Numero do CNPJ do emitente
        self.emit_CPF = ""  #  Numero do CPF do emitente
        self.emit_xNome = ""  #  Razao Social ou Nome do emitente
        self.tot_qCTe = ""  #  Quantidade total de CT-e relacionados no Manifesto
        self.tot_qNFe = ""  #  Quantidade total de NF-e relacionadas no Manifesto
        self.tot_qMDFe = ""  #  Quantidade total de MDFe relacionados no Manifesto Aquaviario
        self.tot_vCarga = 0  #  Valor total da carga / mercadorias transportadas
        self.tot_cUnid = ""  #  Codigo da unidade de medida do Peso Bruto da Carga / Mercadorias transportadas. 01 - KG; 02 - TON
        self.created_at = ""  #  
        self.updated_at = ""  #  


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
	            id,cliente_gprint_id,versao,chMDFe,uuid,cUF,nMDF,cMDF,cDV,tpTransp,modal,dhEmi,tpEmis,procEmi,verProc,UFIni,veicTracao_placa,veicTracao_tara,veicTracao_capKG,veicTracao_capM3,veicTracao_condutor_xNome,veicTracao_condutor_CPF,veicTracao_tpRod,veicTracao_tpCar,veicTracao_UF,emit_CNPJ,emit_CPF,emit_xNome,tot_qCTe,tot_qNFe,tot_qMDFe,tot_vCarga,tot_cUnid
				) VALUES (
				:id,:cliente_gprint_id,:versao,:chMDFe,:uuid,:cUF,:nMDF,:cMDF,:cDV,:tpTransp,:modal,:dhEmi,:tpEmis,:procEmi,:verProc,:UFIni,:veicTracao_placa,:veicTracao_tara,:veicTracao_capKG,:veicTracao_capM3,:veicTracao_condutor_xNome,:veicTracao_condutor_CPF,:veicTracao_tpRod,:veicTracao_tpCar,:veicTracao_UF,:emit_CNPJ,:emit_CPF,:emit_xNome,:tot_qCTe,:tot_qNFe,:tot_qMDFe,:tot_vCarga,:tot_cUnid
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

        cliente_gprint_id = :cliente_gprint_id,
        versao = :versao,
        chMDFe = :chMDFe,
        uuid = :uuid,
        cUF = :cUF,
        nMDF = :nMDF,
        cMDF = :cMDF,
        cDV = :cDV,
        tpTransp = :tpTransp,
        modal = :modal,
        dhEmi = :dhEmi,
        tpEmis = :tpEmis,
        procEmi = :procEmi,
        verProc = :verProc,
        UFIni = :UFIni,
        veicTracao_placa = :veicTracao_placa,
        veicTracao_tara = :veicTracao_tara,
        veicTracao_capKG = :veicTracao_capKG,
        veicTracao_capM3 = :veicTracao_capM3,
        veicTracao_condutor_xNome = :veicTracao_condutor_xNome,
        veicTracao_condutor_CPF = :veicTracao_condutor_CPF,
        veicTracao_tpRod = :veicTracao_tpRod,
        veicTracao_tpCar = :veicTracao_tpCar,
        veicTracao_UF = :veicTracao_UF,
        emit_CNPJ = :emit_CNPJ,
        emit_CPF = :emit_CPF,
        emit_xNome = :emit_xNome,
        tot_qCTe = :tot_qCTe,
        tot_qNFe = :tot_qNFe,
        tot_qMDFe = :tot_qMDFe,
        tot_vCarga = :tot_vCarga,
        tot_cUnid = :tot_cUnid

        where  id = :id  
        """.format(nomeTabela=self.__nomeTabela)
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
        sql_query = self.paramByName(sql_query,"cliente_gprint_id",self.cliente_gprint_id)  # Identifica o cliente no GPrint
        sql_query = self.paramByName(sql_query,"versao",self.versao)  # Vers�o do XML, do mdfeProc
        sql_query = self.paramByName(sql_query,"chMDFe",self.chMDFe)  # Chave da Nota fiscal
        sql_query = self.paramByName(sql_query,"uuid",self.uuid)  # Identificador Unico interno do MDFe
        sql_query = self.paramByName(sql_query,"cUF",self.cUF)  # Codigo da UF do emitente do Manifesto de Documentos Fiscais Eletr�nico. Utilizar a Tabela do IBGE
        sql_query = self.paramByName(sql_query,"nMDF",self.nMDF)  # Numero do Manifesto
        sql_query = self.paramByName(sql_query,"cMDF",self.cMDF)  # Codigo numerico que compoe a Chave de Acesso.
        sql_query = self.paramByName(sql_query,"cDV",self.cDV)  # Digito Verificador da Chave de Acesso da NF-e
        sql_query = self.paramByName(sql_query,"tpTransp",self.tpTransp)  # Tipo do Transportador.	1 - ETC / 2 - TAC / 3 - CTC 
        sql_query = self.paramByName(sql_query,"modal",self.modal)  # Modalidade de transporte. 1 - Rodovi�rio; 2 - A�reo; 3 - Aquavi�rio; 4 - Ferrovi�rio.
        sql_query = self.paramByName(sql_query,"dhEmi",self.dhEmi)  # Data e hora de emiss�o do Manifesto. (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
        sql_query = self.paramByName(sql_query,"tpEmis",self.tpEmis)  # Forma de emiss�o do Manifesto. 1 - Normal; 2 - Conting�ncia; 3-Regime Especial NFF
        sql_query = self.paramByName(sql_query,"procEmi",self.procEmi)  # Processo de emiss�o utilizado com a seguinte codifica��o: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco
        sql_query = self.paramByName(sql_query,"verProc",self.verProc)  # Vers�o do aplicativo utilizado no processo de emiss�o
        sql_query = self.paramByName(sql_query,"UFIni",self.UFIni)  # Sigla da UF do Carregamento.
        sql_query = self.paramByName(sql_query,"veicTracao_placa",self.veicTracao_placa)  # Registra a placa do veiculo
        sql_query = self.paramByName(sql_query,"veicTracao_tara",self.veicTracao_tara)  # Tara do veiculo
        sql_query = self.paramByName(sql_query,"veicTracao_capKG",self.veicTracao_capKG)  # Capacidade de carga do veiculo em KG
        sql_query = self.paramByName(sql_query,"veicTracao_capM3",self.veicTracao_capM3)  # Capacidade de carga do veiculo em Metro Cubico
        sql_query = self.paramByName(sql_query,"veicTracao_condutor_xNome",self.veicTracao_condutor_xNome)  # Nome do condutor do veiculo
        sql_query = self.paramByName(sql_query,"veicTracao_condutor_CPF",self.veicTracao_condutor_CPF)  # CPF do condutor do veiculo
        sql_query = self.paramByName(sql_query,"veicTracao_tpRod",self.veicTracao_tpRod)  # Tipo de rodado. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros
        sql_query = self.paramByName(sql_query,"veicTracao_tpCar",self.veicTracao_tpCar)  # Tipo de Carroceria. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros
        sql_query = self.paramByName(sql_query,"veicTracao_UF",self.veicTracao_UF)  # UF em que veiculo esta licenciado
        sql_query = self.paramByName(sql_query,"emit_CNPJ",self.emit_CNPJ)  # Numero do CNPJ do emitente
        sql_query = self.paramByName(sql_query,"emit_CPF",self.emit_CPF)  # Numero do CPF do emitente
        sql_query = self.paramByName(sql_query,"emit_xNome",self.emit_xNome)  # Razao Social ou Nome do emitente
        sql_query = self.paramByName(sql_query,"tot_qCTe",self.tot_qCTe)  # Quantidade total de CT-e relacionados no Manifesto
        sql_query = self.paramByName(sql_query,"tot_qNFe",self.tot_qNFe)  # Quantidade total de NF-e relacionadas no Manifesto
        sql_query = self.paramByName(sql_query,"tot_qMDFe",self.tot_qMDFe)  # Quantidade total de MDFe relacionados no Manifesto Aquaviario
        sql_query = self.paramByName(sql_query,"tot_vCarga",self.tot_vCarga)  # Valor total da carga / mercadorias transportadas
        sql_query = self.paramByName(sql_query,"tot_cUnid",self.tot_cUnid)  # Codigo da unidade de medida do Peso Bruto da Carga / Mercadorias transportadas. 01 - KG; 02 - TON
        

        self.primeiroNome = self.nome.split()[0].title() if len(self.nome.split()) >1  else self.nome 
        self.ultimoNome = self.nome.split()[-1].title() if len(self.nome.split()) >1  else ""
        return sql_query

    def setValues(self, row):
        """
           Define os campos a partir de uma row passada por parametro

        Args:
            row (list): Registro de retorno de uma cursor.fetchone
        """
        if not row == None:
            self.id = row['id'] # 
            self.cliente_gprint_id = row['cliente_gprint_id'] # Identifica o cliente no GPrint
            self.versao = row['versao'] # Vers�o do XML, do mdfeProc
            self.chMDFe = row['chMDFe'] # Chave da Nota fiscal
            self.uuid = row['uuid'] # Identificador Unico interno do MDFe
            self.cUF = row['cUF'] # Codigo da UF do emitente do Manifesto de Documentos Fiscais Eletr�nico. Utilizar a Tabela do IBGE
            self.nMDF = row['nMDF'] # Numero do Manifesto
            self.cMDF = row['cMDF'] # Codigo numerico que compoe a Chave de Acesso.
            self.cDV = row['cDV'] # Digito Verificador da Chave de Acesso da NF-e
            self.tpTransp = row['tpTransp'] # Tipo do Transportador.	1 - ETC / 2 - TAC / 3 - CTC 
            self.modal = row['modal'] # Modalidade de transporte. 1 - Rodovi�rio; 2 - A�reo; 3 - Aquavi�rio; 4 - Ferrovi�rio.
            self.dhEmi = row['dhEmi'] # Data e hora de emiss�o do Manifesto. (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
            self.tpEmis = row['tpEmis'] # Forma de emiss�o do Manifesto. 1 - Normal; 2 - Conting�ncia; 3-Regime Especial NFF
            self.procEmi = row['procEmi'] # Processo de emiss�o utilizado com a seguinte codifica��o: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco
            self.verProc = row['verProc'] # Vers�o do aplicativo utilizado no processo de emiss�o
            self.UFIni = row['UFIni'] # Sigla da UF do Carregamento.
            self.veicTracao_placa = row['veicTracao_placa'] # Registra a placa do veiculo
            self.veicTracao_tara = row['veicTracao_tara'] # Tara do veiculo
            self.veicTracao_capKG = row['veicTracao_capKG'] # Capacidade de carga do veiculo em KG
            self.veicTracao_capM3 = row['veicTracao_capM3'] # Capacidade de carga do veiculo em Metro Cubico
            self.veicTracao_condutor_xNome = row['veicTracao_condutor_xNome'] # Nome do condutor do veiculo
            self.veicTracao_condutor_CPF = row['veicTracao_condutor_CPF'] # CPF do condutor do veiculo
            self.veicTracao_tpRod = row['veicTracao_tpRod'] # Tipo de rodado. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros
            self.veicTracao_tpCar = row['veicTracao_tpCar'] # Tipo de Carroceria. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros
            self.veicTracao_UF = row['veicTracao_UF'] # UF em que veiculo esta licenciado
            self.emit_CNPJ = row['emit_CNPJ'] # Numero do CNPJ do emitente
            self.emit_CPF = row['emit_CPF'] # Numero do CPF do emitente
            self.emit_xNome = row['emit_xNome'] # Razao Social ou Nome do emitente
            self.tot_qCTe = row['tot_qCTe'] # Quantidade total de CT-e relacionados no Manifesto
            self.tot_qNFe = row['tot_qNFe'] # Quantidade total de NF-e relacionadas no Manifesto
            self.tot_qMDFe = row['tot_qMDFe'] # Quantidade total de MDFe relacionados no Manifesto Aquaviario
            self.tot_vCarga = row['tot_vCarga'] # Valor total da carga / mercadorias transportadas
            self.tot_cUnid = row['tot_cUnid'] # Codigo da unidade de medida do Peso Bruto da Carga / Mercadorias transportadas. 01 - KG; 02 - TON
            self.created_at = row['created_at'] # 
            self.updated_at = row['updated_at'] # 


        
        
        
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
            obj = TMDFeProc(0,self.__database, self.__tablePrefix )
            obj.setValues(value)
            retorno.append(obj)
        return retorno   

    def check_chave(self,chMDFe = ''):            
        """
            Verifica se a chave existe no banco de dados
        Args:           
            chMDFe: string Chave do Manifesto Fiscal Eletronica
        
        Returns:
            bool : Retorna verdadeiro se o registro foi encontrado
        """
        self.__database.open(
            "SELECT * FROM {} WHERE chMDFe={} ".format(self.__nomeTabela,self.getSQLValueString(chMDFe)), None)
            
        return True if len(self.__database.fetch_all())>0 else False 
        
    def check_chave_evento(self,chMDFe = ''):            
        """
            Verifica se a chave existe no banco de dados e teve algum registro de evento
        Args:           
            chMDFe: string Chave do Manifesto Fiscal Eletronica
        
        Returns:
            bool : Retorna verdadeiro se o registro foi encontrado
        """
        self.__database.open(
            "SELECT * FROM {} WHERE chMDFe={} AND (evCancMDFe='S' OR evEncMDFe='S') ".format(self.__nomeTabela,self.getSQLValueString(chMDFe)), None)
            
        return True if len(self.__database.fetch_all())>0 else False 
        
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
        CREATE TABLE IF NOT EXISTS  `mdfe_procs` (
            `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            `cliente_gprint_id` int(11) NOT NULL COMMENT 'Identifica o cliente no GPrint',
            `versao` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Vers�o do XML, do mdfeProc',
            `chMDFe` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Chave da Nota fiscal',
            `uuid` char(36) COLLATE utf8mb4_unicode_ci NOT NULL DEFAULT '' COMMENT 'Identificador Unico interno do MDFe',
            `cUF` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Codigo da UF do emitente do Manifesto de Documentos Fiscais Eletr�nico. Utilizar a Tabela do IBGE',
            `nMDF` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Numero do Manifesto',
            `cMDF` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Codigo numerico que compoe a Chave de Acesso.',
            `cDV` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Digito Verificador da Chave de Acesso da NF-e',
            `tpTransp` enum('1','2','3') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Tipo do Transportador.	1 - ETC / 2 - TAC / 3 - CTC ',
            `modal` enum('1','2','3','4') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Modalidade de transporte. 1 - Rodovi�rio; 2 - A�reo; 3 - Aquavi�rio; 4 - Ferrovi�rio.',
            `dhEmi` date DEFAULT NULL COMMENT 'Data e hora de emiss�o do Manifesto. (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00',
            `tpEmis` enum('1','2','3') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Forma de emiss�o do Manifesto. 1 - Normal; 2 - Conting�ncia; 3-Regime Especial NFF',
            `procEmi` varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Processo de emiss�o utilizado com a seguinte codifica��o: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco',
            `verProc` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Vers�o do aplicativo utilizado no processo de emiss�o',
            `UFIni` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Sigla da UF do Carregamento.',
            `veicTracao_placa` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Registra a placa do veiculo',
            `veicTracao_tara` int(11) DEFAULT NULL COMMENT 'Tara do veiculo',
            `veicTracao_capKG` int(11) DEFAULT NULL COMMENT 'Capacidade de carga do veiculo em KG',
            `veicTracao_capM3` int(11) DEFAULT NULL COMMENT 'Capacidade de carga do veiculo em Metro Cubico',
            `veicTracao_condutor_xNome` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Nome do condutor do veiculo',
            `veicTracao_condutor_CPF` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'CPF do condutor do veiculo',
            `veicTracao_tpRod` enum('01','02','03','04','05','06') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Tipo de rodado. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros',
            `veicTracao_tpCar` enum('00','01','02','03','04','05') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Tipo de Carroceria. 01 - Truck; 02 - Toco; 03 - Cavalo Mecanico; 04 - VAN; 05 - Utilitario; 06 - Outros',
            `veicTracao_UF` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'UF em que veiculo esta licenciado',
            `emit_CNPJ` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Numero do CNPJ do emitente',
            `emit_CPF` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Numero do CPF do emitente',
            `emit_xNome` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Razao Social ou Nome do emitente',
            `tot_qCTe` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Quantidade total de CT-e relacionados no Manifesto',
            `tot_qNFe` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Quantidade total de NF-e relacionadas no Manifesto',
            `tot_qMDFe` varchar(10) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Quantidade total de MDFe relacionados no Manifesto Aquaviario',
            `tot_vCarga` double(8,2) DEFAULT NULL COMMENT 'Valor total da carga / mercadorias transportadas',
            `tot_cUnid` enum('01','02') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Codigo da unidade de medida do Peso Bruto da Carga / Mercadorias transportadas. 01 - KG; 02 - TON',
            `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        
        """
        sqlQuery_sqlite = """
        CREATE TABLE IF NOT EXISTS  `mdfe_procs` (
            `id` bigint(20)  NOT NULL ,
            `cliente_gprint_id` int(11) NOT NULL ,
            `versao` varchar(191)  utf8mb4_unicode_ci DEFAULT NULL ,
            `chMDFe` varchar(45)  utf8mb4_unicode_ci NOT NULL ,
            `uuid` char(36)  utf8mb4_unicode_ci NOT NULL DEFAULT '' ,
            `cUF` varchar(3)  utf8mb4_unicode_ci NOT NULL ,
            `nMDF` varchar(10)  utf8mb4_unicode_ci NOT NULL ,
            `cMDF` varchar(10)  utf8mb4_unicode_ci NOT NULL ,
            `cDV` varchar(2)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tpTransp` enum('1','2','3')  utf8mb4_unicode_ci DEFAULT NULL ,
            `modal` enum('1','2','3','4')  utf8mb4_unicode_ci DEFAULT NULL ,
            `dhEmi` date DEFAULT NULL ,
            `tpEmis` enum('1','2','3')  utf8mb4_unicode_ci DEFAULT NULL ,
            `procEmi` varchar(3)  utf8mb4_unicode_ci DEFAULT NULL ,
            `verProc` varchar(20)  utf8mb4_unicode_ci DEFAULT NULL ,
            `UFIni` varchar(2)  utf8mb4_unicode_ci DEFAULT NULL ,
            `veicTracao_placa` varchar(10)  utf8mb4_unicode_ci DEFAULT NULL ,
            `veicTracao_tara` int(11) DEFAULT NULL ,
            `veicTracao_capKG` int(11) DEFAULT NULL ,
            `veicTracao_capM3` int(11) DEFAULT NULL ,
            `veicTracao_condutor_xNome` varchar(100)  utf8mb4_unicode_ci DEFAULT NULL ,
            `veicTracao_condutor_CPF` varchar(20)  utf8mb4_unicode_ci DEFAULT NULL ,
            `veicTracao_tpRod` enum('01','02','03','04','05','06')  utf8mb4_unicode_ci DEFAULT NULL ,
            `veicTracao_tpCar` enum('00','01','02','03','04','05')  utf8mb4_unicode_ci DEFAULT NULL ,
            `veicTracao_UF` varchar(10)  utf8mb4_unicode_ci DEFAULT NULL ,
            `emit_CNPJ` varchar(16)  utf8mb4_unicode_ci DEFAULT NULL ,
            `emit_CPF` varchar(14)  utf8mb4_unicode_ci DEFAULT NULL ,
            `emit_xNome` varchar(60)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tot_qCTe` varchar(10)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tot_qNFe` varchar(10)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tot_qMDFe` varchar(10)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tot_vCarga` double(8,2) DEFAULT NULL ,
            `tot_cUnid` enum('01','02')  utf8mb4_unicode_ci DEFAULT NULL ,
            `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            )
        
        """
        if self.__database.sgdb == "sqlite":
            return self.__database.execute(sqlQuery_sqlite,None)            
        else:     
            return self.__database.execute(sqlQuery_mysql,None)