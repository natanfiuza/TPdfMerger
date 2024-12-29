"""
Objeto pai de todas as classes 
Concentra varios metodos utilizados em todas as classes

Classes:
   TObject

"""
__author__ = "NatanFiuza - n@taniel.com.br"
__date__ = "14 Abril 2021"

class TObject():
    database = None

    def __init__(self):
        pass
    
    @staticmethod
    def getUUID():
        import uuid

        return str(uuid.uuid4())
    @staticmethod
    def isEmpty (myString):
        if not isinstance(myString,str):
            return False
        if myString and myString.strip():
            #myString is not None AND myString is not empty or blank
            return False
        #myString is None OR myString is empty or blank
        return True
    @staticmethod
    def strRepeat(n,string):
        word = ''
        for num in range(n):            
            word += string
        return word    

    @staticmethod
    def nowDateTime(formato = "%d/%m/%Y %H:%i:%s"):
        """[summary]

        Args:
            formato (str, optional): Recebe o formato de retorno da data. O padrao e "%d/%m/%Y %H:%i:%s".

        Returns:
            [str]: Retorna a data atual no formato determinado
        """
        from datetime import datetime
        today = datetime.now()
        return today.strftime(str(formato))  

    @staticmethod
    def isInteger(valor):

        if not isinstance(id, int):
            try:
                return int(valor)
            except:
                print('************except************')
                return -1
            
        return valor    

