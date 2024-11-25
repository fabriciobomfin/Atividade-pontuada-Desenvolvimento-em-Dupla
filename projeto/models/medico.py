from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crm: str, salario_base: float = 8000.0, adicional: float = 2000.0) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm
        self.salario_base = salario_base
        self.adicional = adicional

    def salario_final(self) -> float:
        return self.salario_base + self.adicional

