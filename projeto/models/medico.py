from models.funcionario import Funcionario
from models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
        self.salario_base = 0.0
        self.adicional = 0.0

    def salario_final(self) -> float:
        return self.salario_base + self.adicional
