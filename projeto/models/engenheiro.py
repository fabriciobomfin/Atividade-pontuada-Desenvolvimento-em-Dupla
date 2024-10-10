from models.funcionario import Funcionario
from models.endereco import Endereco


class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea
        self.salario_base = 5000.0  # Exemplo de salário base
        self.bonus_projetos = 1000.0  # Exemplo de bônus

    def salario_final(self) -> float:
        return self.salario_base + self.bonus_projetos

