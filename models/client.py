from utils.helper import date_string,string_date
from datetime import date
class Cliente:
    id=1
    def __init__(self:object,nome:str,email:str,cpf:str,data_nascimento:str):
        self.__codigo=Cliente.id
        self.__nome=nome
        self.__dataNascimento=string_date(data_nascimento)
        self.__email=email
        self.__cpf=cpf
        self.__dataCadastro=date.today()
        Cliente.id+=1
    @property
    def codigo(self):
        return self.__codigo
    @property
    def nome(self):
        return self.__nome
    @property
    def dataNascimento(self):
        return string_date(self.__dataNascimento)
    @property
    def email(self):
        return self.__email
    @property
    def cpf(self):
        return self.__cpf
    @property
    def dataCadastro(self):
        return date_string(self.__dataCadastro)

