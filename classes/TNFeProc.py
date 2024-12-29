"""
Registro das notas fiscais eletronicas

Classes:
   Tnfe_procs
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

class TNFeProc(TPersistente):

    def __init__(self, id, pDataBase, tableprefix):
        """
        Classe Tnfe_procs
        Tem como herança a classe TPersistente

        Args:
            TPersistente (object): Classe que controla a interação com o banco de dados
        Atributos:    
            `id`, Tipo: Integer ,  Descricao:  

            `cliente_gprint_id`, Tipo: Integer ,  Descricao: Identifica o cliente no GPrint 

            `versao`, Tipo: String ,  Descricao: Vers�o do XML, do nfeProc 

            `chNFe`, Tipo: String ,  Descricao: Chave da Nota fiscal 

            `cUF`, Tipo: String ,  Descricao: Codigo da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE. 

            `cNF`, Tipo: String ,  Descricao: Codigo num�rico que comp�e a Chave de Acesso. N�mero aleat�rio gerado pelo emitente para cada NF-e. 

            `natOp`, Tipo: String ,  Descricao: Descricao da Natureza da Operacao 

            `mod`, Tipo: String ,  Descricao: Codigo do modelo do Documento Fiscal. 55 = NF-e; 65 = NFC-e. 

            `serie`, Tipo: String ,  Descricao: S�rie do Documento Fiscal s�rie normal 0-889 Avulsa Fisco 890-899 SCAN 900-999 

            `dhEmi`, Tipo: date ,  Descricao: Data e Hora de emiss�o do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00 

            `dhSaiEnt`, Tipo: date ,  Descricao: Data e Hora da saida ou de entrada da mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD) 

            `tpNF`, Tipo:  ,  Descricao: Tipo do Documento Fiscal (0 - entrada; 1 - saida) 

            `idDest`, Tipo:  ,  Descricao: Identificador de Local de destino da operacao (1-Interna;2-Interestadual;3-Exterior) 

            `cMunFG`, Tipo: String ,  Descricao: Codigo do Munic�pio de Ocorr�ncia do Fato Gerador (utilizar a tabela do IBGE) 

            `tpImp`, Tipo:  ,  Descricao: Formato de impress�o do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletr�nica) 

            `tpEmis`, Tipo:  ,  Descricao: Forma de emiss�o da NF-e 1 - Normal; 2 - Contingencia FS 3 - Contingencia SCAN 4 - Contingencia DPEC 5 - Contingencia FSDA 6 - Contingencia SVC - AN 7 - Contingencia SVC - RS 9 - Contingencia off-line NFC-e 

            `cDV`, Tipo: String ,  Descricao: Digito Verificador da Chave de Acesso da NF-e 

            `tpAmb`, Tipo: String ,  Descricao: Identificacao do Ambiente: 1 - Producao 2 - Homologacao 

            `finNFe`, Tipo: String ,  Descricao: Finalidade da emiss�o da NF-e: 1 - NFe normal 2 - NFe complementar 3 - NFe de ajuste 4 - Devolucao/Retorno 

            `indFinal`, Tipo:  ,  Descricao: Indica operacao com consumidor final (0-N�o;1-Consumidor Final) 

            `indPres`, Tipo:  ,  Descricao: Indicador de presen�a do comprador no estabelecimento comercial no momento da oepracao (0-N�o se aplica (ex.: Nota Fiscal complementar ou de ajuste;1-Operacao presencial;2-N�o presencial, internet;3-N�o presencial, teleatendimento;4-NFC-e entrega em domic�lio;5-Operacao presencial, fora do estabelecimento;9-N�o presencial, outros) 

            `procEmi`, Tipo: String ,  Descricao: Processo de emiss�o utilizado com a seguinte codificacao: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco. 

            `verProc`, Tipo: String ,  Descricao: Vers�o do aplicativo utilizado no processo de emiss�o 

            `dhCont`, Tipo: date ,  Descricao: Informar a data e hora de entrada em Contingencia Contingencia no formato (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00. 

            `xJust`, Tipo: String ,  Descricao: Informar a Justificativa da entrada 

            `xNome`, Tipo: String ,  Descricao: Razao Social ou Nome do emitente 

            `emit_CNPJ`, Tipo: String ,  Descricao: N�mero do CNPJ do emitente 

            `emit_CPF`, Tipo: String ,  Descricao: N�mero do CPF do emitente 

            `emit_xNome`, Tipo: String ,  Descricao: Razao Social ou Nome do emitente 

            `dest_CNPJ`, Tipo: String ,  Descricao: N�mero do CNPJ do Destinat�rio 

            `dest_CPF`, Tipo: String ,  Descricao: N�mero do CPF do Destinat�rio 

            `dest_xNome`, Tipo: String ,  Descricao: Razao Social ou Nome do Destinat�rio 

            `ICMSTot_vNF`, Tipo: Float ,  Descricao: Valor Total da NF-e 

            `ICMSTot_vTotTrib`, Tipo: Float ,  Descricao: Valor estimado total de impostos federais, estaduais e municipais 

            `ICMSTot_vPIS`, Tipo: Float ,  Descricao: Valor do PIS sobre servi�os 

            `ICMSTot_vCOFINS`, Tipo: Float ,  Descricao: Valor do COFINS sobre servi�os 

            `created_at`, Tipo: timestamp ,  Descricao:  

            `updated_at`, Tipo: timestamp ,  Descricao:  
        
        """ 
        from datetime import datetime
        self.__tablePrefix = tableprefix
        self.__nomeTabela = "{}nfe_procs".format(tableprefix)
        self.__database = pDataBase
        self.__totalrows = ""  # Recebe o total de registro retornados na funcao busca
        # Atributos publicos dos campos da tabela 
        self.id = 0  #  
        self.cliente_gprint_id = 0  #  Identifica o cliente no GPrint
        self.versao = ""  #  Vers�o do XML, do nfeProc
        self.chNFe = ""  #  Chave da Nota fiscal
        self.cUF = ""  #  Codigo da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE.
        self.cNF = ""  #  Codigo num�rico que comp�e a Chave de Acesso. N�mero aleat�rio gerado pelo emitente para cada NF-e.
        self.natOp = ""  #  Descricao da Natureza da Operacao
        self.mod = ""  #  Codigo do modelo do Documento Fiscal. 55 = NF-e; 65 = NFC-e.
        self.serie = ""  #  S�rie do Documento Fiscal s�rie normal 0-889 Avulsa Fisco 890-899 SCAN 900-999
        self.dhEmi = ""  #  Data e Hora de emiss�o do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
        self.dhSaiEnt = ""  #  Data e Hora da saida ou de entrada da mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)
        self.tpNF = ""  #  Tipo do Documento Fiscal 0 - entrada; 1 - saida
        self.idDest = ""  #  Identificador de Local de destino da operacao (1-Interna;2-Interestadual;3-Exterior)
        self.cMunFG = ""  #  Codigo do Munic�pio de Ocorr�ncia do Fato Gerador (utilizar a tabela do IBGE)
        self.tpImp = ""  #  Formato de impress�o do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletr�nica)
        self.tpEmis = ""  #  Forma de emiss�o da NF-e 1 - Normal; 2 - Contingencia FS 3 - Contingencia SCAN 4 - Contingencia DPEC 5 - Contingencia FSDA 6 - Contingencia SVC - AN 7 - Contingencia SVC - RS 9 - Contingencia off-line NFC-e
        self.cDV = ""  #  Digito Verificador da Chave de Acesso da NF-e
        self.tpAmb = ""  #  Identificacao do Ambiente: 1 - Producao 2 - Homologacao
        self.finNFe = ""  #  Finalidade da emiss�o da NF-e: 1 - NFe normal 2 - NFe complementar 3 - NFe de ajuste 4 - Devolucao/Retorno
        self.indFinal = ""  #  Indica operacao com consumidor final (0-N�o;1-Consumidor Final)
        self.indPres = ""  #  Indicador de presen�a do comprador no estabelecimento comercial no momento da oepracao (0-N�o se aplica (ex.: Nota Fiscal complementar ou de ajuste;1-Operacao presencial;2-N�o presencial, internet;3-N�o presencial, teleatendimento;4-NFC-e entrega em domic�lio;5-Operacao presencial, fora do estabelecimento;9-N�o presencial, outros)
        self.procEmi = ""  #  Processo de emiss�o utilizado com a seguinte codificacao: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco.
        self.verProc = ""  #  Vers�o do aplicativo utilizado no processo de emiss�o
        self.dhCont = ""  #  Informar a data e hora de entrada em Contingencia Contingencia no formato (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.
        self.xJust = ""  #  Informar a Justificativa da entrada
        self.xNome = ""  #  Razao Social ou Nome do emitente
        self.emit_CNPJ = ""  #  N�mero do CNPJ do emitente
        self.emit_CPF = ""  #  N�mero do CPF do emitente
        self.emit_xNome = ""  #  Razao Social ou Nome do emitente
        self.dest_CNPJ = ""  #  N�mero do CNPJ do Destinat�rio
        self.dest_CPF = ""  #  N�mero do CPF do Destinat�rio
        self.dest_xNome = ""  #  Razao Social ou Nome do Destinat�rio
        self.ICMSTot_vNF = 0  #  Valor Total da NF-e
        self.ICMSTot_vTotTrib = 0.00  #  Valor estimado total de impostos federais, estaduais e municipais
        self.ICMSTot_vPIS = 0.00  #  Valor do PIS sobre servi�os
        self.ICMSTot_vCOFINS = 0.00  #  Valor do COFINS sobre servi�os
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
	            id,cliente_gprint_id,versao,chNFe,cUF,cNF,natOp,mod,serie,dhEmi,dhSaiEnt,tpNF,idDest,cMunFG,tpImp,tpEmis,cDV,tpAmb,finNFe,indFinal,indPres,procEmi,verProc,dhCont,xJust,xNome,emit_CNPJ,emit_CPF,emit_xNome,dest_CNPJ,dest_CPF,dest_xNome,ICMSTot_vNF,ICMSTot_vTotTrib,ICMSTot_vPIS,ICMSTot_vCOFINS,created_at,updated_at
				) VALUES (
				:id,:cliente_gprint_id,:versao,:chNFe,:cUF,:cNF,:natOp,:mod,:serie,:dhEmi,:dhSaiEnt,:tpNF,:idDest,:cMunFG,:tpImp,:tpEmis,:cDV,:tpAmb,:finNFe,:indFinal,:indPres,:procEmi,:verProc,:dhCont,:xJust,:xNome,:emit_CNPJ,:emit_CPF,:emit_xNome,:dest_CNPJ,:dest_CPF,:dest_xNome,:ICMSTot_vNF,:ICMSTot_vTotTrib,:ICMSTot_vPIS,:ICMSTot_vCOFINS,:created_at,:updated_at
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
            chNFe = :chNFe,
            cUF = :cUF,
            cNF = :cNF,
            natOp = :natOp,
            mod = :mod,
            serie = :serie,
            dhEmi = :dhEmi,
            dhSaiEnt = :dhSaiEnt,
            tpNF = :tpNF,
            idDest = :idDest,
            cMunFG = :cMunFG,
            tpImp = :tpImp,
            tpEmis = :tpEmis,
            cDV = :cDV,
            tpAmb = :tpAmb,
            finNFe = :finNFe,
            indFinal = :indFinal,
            indPres = :indPres,
            procEmi = :procEmi,
            verProc = :verProc,
            dhCont = :dhCont,
            xJust = :xJust,
            xNome = :xNome,
            emit_CNPJ = :emit_CNPJ,
            emit_CPF = :emit_CPF,
            emit_xNome = :emit_xNome,
            dest_CNPJ = :dest_CNPJ,
            dest_CPF = :dest_CPF,
            dest_xNome = :dest_xNome,
            ICMSTot_vNF = :ICMSTot_vNF,
            ICMSTot_vTotTrib = :ICMSTot_vTotTrib,
            ICMSTot_vPIS = :ICMSTot_vPIS,
            ICMSTot_vCOFINS = :ICMSTot_vCOFINS

            where  id = :id  """.format(nomeTabela=self.__nomeTabela)
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
        sql_query = self.paramByName(sql_query,"versao",self.versao)  # Vers�o do XML, do nfeProc
        sql_query = self.paramByName(sql_query,"chNFe",self.chNFe)  # Chave da Nota fiscal
        sql_query = self.paramByName(sql_query,"cUF",self.cUF)  # Codigo da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE.
        sql_query = self.paramByName(sql_query,"cNF",self.cNF)  # Codigo num�rico que comp�e a Chave de Acesso. N�mero aleat�rio gerado pelo emitente para cada NF-e.
        sql_query = self.paramByName(sql_query,"natOp",self.natOp)  # Descricao da Natureza da Operacao
        sql_query = self.paramByName(sql_query,"mod",self.mod)  # Codigo do modelo do Documento Fiscal. 55 = NF-e; 65 = NFC-e.
        sql_query = self.paramByName(sql_query,"serie",self.serie)  # S�rie do Documento Fiscal s�rie normal 0-889 Avulsa Fisco 890-899 SCAN 900-999
        sql_query = self.paramByName(sql_query,"dhEmi",self.dhEmi)  # Data e Hora de emiss�o do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
        sql_query = self.paramByName(sql_query,"dhSaiEnt",self.dhSaiEnt)  # Data e Hora da saida ou de entrada da mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)
        sql_query = self.paramByName(sql_query,"tpNF",self.tpNF)  # Tipo do Documento Fiscal (0 - entrada; 1 - saida)
        sql_query = self.paramByName(sql_query,"idDest",self.idDest)  # Identificador de Local de destino da operacao (1-Interna;2-Interestadual;3-Exterior)
        sql_query = self.paramByName(sql_query,"cMunFG",self.cMunFG)  # Codigo do Munic�pio de Ocorr�ncia do Fato Gerador (utilizar a tabela do IBGE)
        sql_query = self.paramByName(sql_query,"tpImp",self.tpImp)  # Formato de impress�o do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletr�nica)
        sql_query = self.paramByName(sql_query,"tpEmis",self.tpEmis)  # Forma de emiss�o da NF-e 1 - Normal; 2 - Contingencia FS 3 - Contingencia SCAN 4 - Contingencia DPEC 5 - Contingencia FSDA 6 - Contingencia SVC - AN 7 - Contingencia SVC - RS 9 - Contingencia off-line NFC-e
        sql_query = self.paramByName(sql_query,"cDV",self.cDV)  # Digito Verificador da Chave de Acesso da NF-e
        sql_query = self.paramByName(sql_query,"tpAmb",self.tpAmb)  # Identificacao do Ambiente: 1 - Producao 2 - Homologacao
        sql_query = self.paramByName(sql_query,"finNFe",self.finNFe)  # Finalidade da emiss�o da NF-e: 1 - NFe normal 2 - NFe complementar 3 - NFe de ajuste 4 - Devolucao/Retorno
        sql_query = self.paramByName(sql_query,"indFinal",self.indFinal)  # Indica operacao com consumidor final (0-N�o;1-Consumidor Final)
        sql_query = self.paramByName(sql_query,"indPres",self.indPres)  # Indicador de presen�a do comprador no estabelecimento comercial no momento da oepracao (0-N�o se aplica (ex.: Nota Fiscal complementar ou de ajuste;1-Operacao presencial;2-N�o presencial, internet;3-N�o presencial, teleatendimento;4-NFC-e entrega em domic�lio;5-Operacao presencial, fora do estabelecimento;9-N�o presencial, outros)
        sql_query = self.paramByName(sql_query,"procEmi",self.procEmi)  # Processo de emiss�o utilizado com a seguinte codificacao: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco.
        sql_query = self.paramByName(sql_query,"verProc",self.verProc)  # Vers�o do aplicativo utilizado no processo de emiss�o
        sql_query = self.paramByName(sql_query,"dhCont",self.dhCont)  # Informar a data e hora de entrada em Contingencia Contingencia no formato (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.
        sql_query = self.paramByName(sql_query,"xJust",self.xJust)  # Informar a Justificativa da entrada
        sql_query = self.paramByName(sql_query,"xNome",self.xNome)  # Razao Social ou Nome do emitente
        sql_query = self.paramByName(sql_query,"emit_CNPJ",self.emit_CNPJ)  # N�mero do CNPJ do emitente
        sql_query = self.paramByName(sql_query,"emit_CPF",self.emit_CPF)  # N�mero do CPF do emitente
        sql_query = self.paramByName(sql_query,"emit_xNome",self.emit_xNome)  # Razao Social ou Nome do emitente
        sql_query = self.paramByName(sql_query,"dest_CNPJ",self.dest_CNPJ)  # N�mero do CNPJ do Destinat�rio
        sql_query = self.paramByName(sql_query,"dest_CPF",self.dest_CPF)  # N�mero do CPF do Destinat�rio
        sql_query = self.paramByName(sql_query,"dest_xNome",self.dest_xNome)  # Razao Social ou Nome do Destinat�rio
        sql_query = self.paramByName(sql_query,"ICMSTot_vNF",self.ICMSTot_vNF)  # Valor Total da NF-e
        sql_query = self.paramByName(sql_query,"ICMSTot_vTotTrib",self.ICMSTot_vTotTrib)  # Valor estimado total de impostos federais, estaduais e municipais
        sql_query = self.paramByName(sql_query,"ICMSTot_vPIS",self.ICMSTot_vPIS)  # Valor do PIS sobre servi�os
        sql_query = self.paramByName(sql_query,"ICMSTot_vCOFINS",self.ICMSTot_vCOFINS)  # Valor do COFINS sobre servi�os
        sql_query = self.paramByName(sql_query,"created_at",self.created_at)  # 
        sql_query = self.paramByName(sql_query,"updated_at",self.updated_at)  # 

	

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
            self.versao = row['versao'] # Vers�o do XML, do nfeProc
            self.chNFe = row['chNFe'] # Chave da Nota fiscal
            self.cUF = row['cUF'] # Codigo da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE.
            self.cNF = row['cNF'] # Codigo num�rico que comp�e a Chave de Acesso. N�mero aleat�rio gerado pelo emitente para cada NF-e.
            self.natOp = row['natOp'] # Descricao da Natureza da Operacao
            self.mod = row['mod'] # Codigo do modelo do Documento Fiscal. 55 = NF-e; 65 = NFC-e.
            self.serie = row['serie'] # S�rie do Documento Fiscal s�rie normal 0-889 Avulsa Fisco 890-899 SCAN 900-999
            self.dhEmi = row['dhEmi'] # Data e Hora de emiss�o do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00
            self.dhSaiEnt = row['dhSaiEnt'] # Data e Hora da saida ou de entrada da mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)
            self.tpNF = row['tpNF'] # Tipo do Documento Fiscal (0 - entrada; 1 - saida)
            self.idDest = row['idDest'] # Identificador de Local de destino da operacao (1-Interna;2-Interestadual;3-Exterior)
            self.cMunFG = row['cMunFG'] # Codigo do Munic�pio de Ocorr�ncia do Fato Gerador (utilizar a tabela do IBGE)
            self.tpImp = row['tpImp'] # Formato de impress�o do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletr�nica)
            self.tpEmis = row['tpEmis'] # Forma de emiss�o da NF-e 1 - Normal; 2 - Contingencia FS 3 - Contingencia SCAN 4 - Contingencia DPEC 5 - Contingencia FSDA 6 - Contingencia SVC - AN 7 - Contingencia SVC - RS 9 - Contingencia off-line NFC-e
            self.cDV = row['cDV'] # Digito Verificador da Chave de Acesso da NF-e
            self.tpAmb = row['tpAmb'] # Identificacao do Ambiente: 1 - Producao 2 - Homologacao
            self.finNFe = row['finNFe'] # Finalidade da emiss�o da NF-e: 1 - NFe normal 2 - NFe complementar 3 - NFe de ajuste 4 - Devolucao/Retorno
            self.indFinal = row['indFinal'] # Indica operacao com consumidor final (0-N�o;1-Consumidor Final)
            self.indPres = row['indPres'] # Indicador de presen�a do comprador no estabelecimento comercial no momento da oepracao (0-N�o se aplica (ex.: Nota Fiscal complementar ou de ajuste;1-Operacao presencial;2-N�o presencial, internet;3-N�o presencial, teleatendimento;4-NFC-e entrega em domic�lio;5-Operacao presencial, fora do estabelecimento;9-N�o presencial, outros)
            self.procEmi = row['procEmi'] # Processo de emiss�o utilizado com a seguinte codificacao: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco.
            self.verProc = row['verProc'] # Vers�o do aplicativo utilizado no processo de emiss�o
            self.dhCont = row['dhCont'] # Informar a data e hora de entrada em Contingencia Contingencia no formato (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.
            self.xJust = row['xJust'] # Informar a Justificativa da entrada
            self.xNome = row['xNome'] # Razao Social ou Nome do emitente
            self.emit_CNPJ = row['emit_CNPJ'] # N�mero do CNPJ do emitente
            self.emit_CPF = row['emit_CPF'] # N�mero do CPF do emitente
            self.emit_xNome = row['emit_xNome'] # Razao Social ou Nome do emitente
            self.dest_CNPJ = row['dest_CNPJ'] # N�mero do CNPJ do Destinat�rio
            self.dest_CPF = row['dest_CPF'] # N�mero do CPF do Destinat�rio
            self.dest_xNome = row['dest_xNome'] # Razao Social ou Nome do Destinat�rio
            self.ICMSTot_vNF = row['ICMSTot_vNF'] # Valor Total da NF-e
            self.ICMSTot_vTotTrib = row['ICMSTot_vTotTrib'] # Valor estimado total de impostos federais, estaduais e municipais
            self.ICMSTot_vPIS = row['ICMSTot_vPIS'] # Valor do PIS sobre servi�os
            self.ICMSTot_vCOFINS = row['ICMSTot_vCOFINS'] # Valor do COFINS sobre servi�os
            self.created_at = row['created_at'] # 
            self.updated_at = row['updated_at'] # 


        
        self.primeiroNome = self.nome.split()[0].title() if len(self.nome.split()) >1  else self.nome 
        self.ultimoNome = self.nome.split()[-1].title() if len(self.nome.split()) >1  else ""
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
            obj = TNFeProc(0,self.__database, self.__tablePrefix )
            obj.setValues(value)
            retorno.append(obj)
        return retorno   
        
    def check_chave(self,chNFe = ''):            
        """
            Verifica se a chave existe no banco de dados
        Args           
            chNFe: string Chave da Nota Fiscal eletronica
        
        Returns:
            bool : Retorna verdadeiro se o registro foi encontrado
        """
        self.__database.open(
            "SELECT * FROM {} WHERE chNFe={} ".format(self.__nomeTabela,self.getSQLValueString(chNFe)), None)
            
        return True if len(self.__database.fetch_all())>0 else False 

    def check_chave_evento(self, chNFe=''):
        """
            Verifica se a chave existe no banco de dados e teve algum registro de evento
        Args:           
            chMDFe: string Chave do Manifesto Fiscal Eletronica
        
        Returns:
            bool : Retorna verdadeiro se o registro foi encontrado
        """
        self.__database.open(
            "SELECT * FROM {} WHERE chNFe={} AND evCanc='S'  ".format(self.__nomeTabela, self.getSQLValueString(chNFe)), None)
     
        return True if len(self.__database.fetch_all()) > 0 else False
    
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
        CREATE TABLE IF NOT EXISTS  `nfe_procs` (
            `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            `cliente_gprint_id` bigint(20) unsigned NOT NULL COMMENT 'Identifica o cliente no GPrint',
            `versao` varchar(191) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Vers�o do XML, do nfeProc',
            `chNFe` varchar(45) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Chave da Nota fiscal',
            `cUF` varchar(3) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Codigo da UF do emitente do Documento Fiscal. Utilizar a Tabela do IBGE.',
            `cNF` varchar(10) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT 'Codigo num�rico que comp�e a Chave de Acesso. N�mero aleat�rio gerado pelo emitente para cada NF-e.',
            `natOp` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Descricao da Natureza da Operacao',
            `mod` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Codigo do modelo do Documento Fiscal. 55 = NF-e; 65 = NFC-e.',
            `serie` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'S�rie do Documento Fiscal s�rie normal 0-889 Avulsa Fisco 890-899 SCAN 900-999',
            `dhEmi` date DEFAULT NULL COMMENT 'Data e Hora de emiss�o do Documento Fiscal (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00',
            `dhSaiEnt` date DEFAULT NULL COMMENT 'Data e Hora da saida ou de entrada da mercadoria / produto (AAAA-MM-DDTHH:mm:ssTZD)',
            `tpNF` enum('0','1') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Tipo do Documento Fiscal (0 - entrada; 1 - saida)',
            `idDest` enum('1','2','3') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Identificador de Local de destino da operacao (1-Interna;2-Interestadual;3-Exterior)',
            `cMunFG` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Codigo do Munic�pio de Ocorr�ncia do Fato Gerador (utilizar a tabela do IBGE)',
            `tpImp` enum('0','1','2','3','4','5') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Formato de impress�o do DANFE (0-sem DANFE;1-DANFe Retrato; 2-DANFe Paisagem;3-DANFe Simplificado; 4-DANFe NFC-e;5-DANFe NFC-e em mensagem eletr�nica)',
            `tpEmis` enum('1','2','3','4','5','6','7','9') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Forma de emiss�o da NF-e 1 - Normal; 2 - Contingencia FS 3 - Contingencia SCAN 4 - Contingencia DPEC 5 - Contingencia FSDA 6 - Contingencia SVC - AN 7 - Contingencia SVC - RS 9 - Contingencia off-line NFC-e',
            `cDV` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Digito Verificador da Chave de Acesso da NF-e',
            `tpAmb` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Identificacao do Ambiente: 1 - Producao 2 - Homologacao',
            `finNFe` varchar(2) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Finalidade da emiss�o da NF-e: 1 - NFe normal 2 - NFe complementar 3 - NFe de ajuste 4 - Devolucao/Retorno',
            `indFinal` enum('0','1') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Indica operacao com consumidor final (0-N�o;1-Consumidor Final)',
            `indPres` enum('0','1','2','3','4','5','9') COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Indicador de presen�a do comprador no estabelecimento comercial no momento da oepracao (0-N�o se aplica (ex.: Nota Fiscal complementar ou de ajuste;1-Operacao presencial;2-N�o presencial, internet;3-N�o presencial, teleatendimento;4-NFC-e entrega em domic�lio;5-Operacao presencial, fora do estabelecimento;9-N�o presencial, outros)',
            `procEmi` varchar(3) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Processo de emiss�o utilizado com a seguinte codificacao: 0 - emiss�o de NF-e com aplicativo do contribuinte; 1 - emiss�o de NF-e avulsa pelo Fisco; 2 - emiss�o de NF-e avulsa, pelo contribuinte com seu certificado digital, atrav�s do site do Fisco; 3- emiss�o de NF-e pelo contribuinte com aplicativo fornecido pelo Fisco.',
            `verProc` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Vers�o do aplicativo utilizado no processo de emiss�o',
            `dhCont` date DEFAULT NULL COMMENT 'Informar a data e hora de entrada em Contingencia Contingencia no formato (AAAA-MM-DDThh:mm:ssTZD) ex.: 2012-09-01T13:00:00-03:00.',
            `xJust` varchar(256) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Informar a Justificativa da entrada',
            `xNome` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Razao Social ou Nome do emitente',
            `emit_CNPJ` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'N�mero do CNPJ do emitente',
            `emit_CPF` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'N�mero do CPF do emitente',
            `emit_xNome` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Razao Social ou Nome do emitente',
            `dest_CNPJ` varchar(16) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'N�mero do CNPJ do Destinat�rio',
            `dest_CPF` varchar(14) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'N�mero do CPF do Destinat�rio',
            `dest_xNome` varchar(60) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT 'Razao Social ou Nome do Destinat�rio',
            `ICMSTot_vNF` double(8,2) NOT NULL COMMENT 'Valor Total da NF-e',
            `ICMSTot_vTotTrib` double(8,2) NOT NULL DEFAULT '0.00' COMMENT 'Valor estimado total de impostos federais, estaduais e municipais',
            `ICMSTot_vPIS` double(8,2) NOT NULL DEFAULT '0.00' COMMENT 'Valor do PIS sobre servi�os',
            `ICMSTot_vCOFINS` double(8,2) NOT NULL DEFAULT '0.00' COMMENT 'Valor do COFINS sobre servi�os',
            `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            ) ENGINE=MyISAM DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
                    
        """
        sqlQuery_sqlite = """
        CREATE TABLE IF NOT EXISTS  `nfe_procs` (
            `id` bigint(20)  NOT NULL ,
            `cliente_gprint_id` bigint(20)  NOT NULL ,
            `versao` varchar(191)  utf8mb4_unicode_ci DEFAULT NULL ,
            `chNFe` varchar(45)  utf8mb4_unicode_ci NOT NULL ,
            `cUF` varchar(3)  utf8mb4_unicode_ci NOT NULL ,
            `cNF` varchar(10)  utf8mb4_unicode_ci NOT NULL ,
            `natOp` varchar(60)  utf8mb4_unicode_ci DEFAULT NULL ,
            `mod` varchar(20)  utf8mb4_unicode_ci DEFAULT NULL ,
            `serie` varchar(100)  utf8mb4_unicode_ci DEFAULT NULL ,
            `dhEmi` date DEFAULT NULL ,
            `dhSaiEnt` date DEFAULT NULL ,
            `tpNF` enum('0','1')  utf8mb4_unicode_ci DEFAULT NULL ,
            `idDest` enum('1','2','3')  utf8mb4_unicode_ci DEFAULT NULL ,
            `cMunFG` varchar(20)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tpImp` enum('0','1','2','3','4','5')  utf8mb4_unicode_ci DEFAULT NULL ,
            `tpEmis` enum('1','2','3','4','5','6','7','9')  utf8mb4_unicode_ci DEFAULT NULL ,
            `cDV` varchar(2)  utf8mb4_unicode_ci DEFAULT NULL ,
            `tpAmb` varchar(2)  utf8mb4_unicode_ci DEFAULT NULL ,
            `finNFe` varchar(2)  utf8mb4_unicode_ci DEFAULT NULL ,
            `indFinal` enum('0','1')  utf8mb4_unicode_ci DEFAULT NULL ,
            `indPres` enum('0','1','2','3','4','5','9')  utf8mb4_unicode_ci DEFAULT NULL ,
            `procEmi` varchar(3)  utf8mb4_unicode_ci DEFAULT NULL ,
            `verProc` varchar(20)  utf8mb4_unicode_ci DEFAULT NULL ,
            `dhCont` date DEFAULT NULL ,
            `xJust` varchar(256)  utf8mb4_unicode_ci DEFAULT NULL ,
            `xNome` varchar(60)  utf8mb4_unicode_ci DEFAULT NULL ,
            `emit_CNPJ` varchar(16)  utf8mb4_unicode_ci DEFAULT NULL ,
            `emit_CPF` varchar(14)  utf8mb4_unicode_ci DEFAULT NULL ,
            `emit_xNome` varchar(60)  utf8mb4_unicode_ci DEFAULT NULL ,
            `dest_CNPJ` varchar(16)  utf8mb4_unicode_ci DEFAULT NULL ,
            `dest_CPF` varchar(14)  utf8mb4_unicode_ci DEFAULT NULL ,
            `dest_xNome` varchar(60)  utf8mb4_unicode_ci DEFAULT NULL ,
            `ICMSTot_vNF` double(8,2) NOT NULL ,
            `ICMSTot_vTotTrib` double(8,2) NOT NULL DEFAULT '0.00' ,
            `ICMSTot_vPIS` double(8,2) NOT NULL DEFAULT '0.00' ,
            `ICMSTot_vCOFINS` double(8,2) NOT NULL DEFAULT '0.00' ,
            `created_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
            `updated_at` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            PRIMARY KEY (`id`)
            )
                    
        """
        if self.__database.sgdb == "sqlite":
            return self.__database.execute(sqlQuery_sqlite,None)            
        else:     
            return self.__database.execute(sqlQuery_mysql,None)
