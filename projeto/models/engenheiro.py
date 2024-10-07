from models.funcionario import Funcionario
from models.endereco import Endereco

class Engenheiro(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, crea: str) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crea = crea

    def salario_final(self) -> float:
        # Implementar a lógica para calcular o salário final de um engenheiro
        return 0.0  # Substituir pela lógica real
