# Exemplo de padrão de projeto Factory
from abc import ABC, abstractmethod
from typing import List


# Classe abstrata que define o contrato para os clientes
class Cliente(ABC):

    @abstractmethod
    def print_information(self) -> str:
        raise NotImplementedError()


# Classe abstrata que define o contrato para as fábricas
class Factory(ABC):
    def factory_method(self) -> Cliente:
        raise NotImplementedError()


# Fábrica concreta que cria clientes físicos    
class ClienteFisicoFactory(Factory):
    def factory_method(self, cpf, data_nascimento, sexo) -> Cliente:
        return ClienteFisico(cpf, data_nascimento, sexo)


# Fábrica concreta que cria clientes jurídicos
class ClienteJuridicoFactory(Factory):
    def factory_method(self, cnpj, tipo_empresa, data_criacao) -> Cliente:
        return ClienteJuridico( cnpj, tipo_empresa, data_criacao)


# Classe concreta que implementa o cliente físico
class ClienteFisico(Cliente):

    # Construtor
    def __init__(self, cpf, data_nascimento, sexo) -> None:
        self.cpf = cpf
        self.data_nascimento = data_nascimento
        self.sexo = sexo
    
    # Método que imprime as informações do cliente
    def print_information(self) -> None:
        print("Tipo de cliente: Fisico")
        print(f"CPF: {self.cpf}")
        print(f"Data de nascimento: {self.data_nascimento}")
        print(f"Sexo: {self.sexo}")


# Classe concreta que implementa o cliente jurídico
class ClienteJuridico(Cliente):

    # Construtor
    def __init__(self, cnpj, data_criacao, tipo_empresa) -> None:
        self.cnpj = cnpj
        self.data_criacao = data_criacao
        self.tipo_empresa = tipo_empresa
    
    # Método que imprime as informações do cliente
    def print_information(self) -> None:
        print("Tipo de cliente: Juridico")
        print(f"CNPJ: {self.cnpj}")
        print(f"Data de criação: {self.data_criacao}")
        print(f"Tipo de empresa: {self.tipo_empresa}")


# Classe principal
class Main():
    def main(self):
        cliente_fisico = ClienteFisicoFactory().factory_method("123.456.789-10", "01/01/2000", "M")
        cliente_fisico.print_information()
        print("\n")
        cliente_juridico = ClienteJuridicoFactory().factory_method("12.124.452/0001-67", "01/01/1953", "LTDA")
        cliente_juridico.print_information()


if __name__ == "__main__":

    main = Main()
    main.main()