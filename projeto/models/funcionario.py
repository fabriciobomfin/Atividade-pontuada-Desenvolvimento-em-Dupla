from abc import ABC, abstractmethod
from models.endereco import Endereco

class Funcionario(ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = self._validar_nome(nome)
        self.telefone = self._validar_telefone(telefone)
        self.email = self._validar_email(email)
        self.endereco = endereco

    def _validar_nome(self, nome):
        if not isinstance(nome, str):
            raise TypeError("O nome deve ser um texto.")
        if not nome.strip():
            raise ValueError("Nome não pode estar vazio.")
        return nome

    def _validar_telefone(self, telefone):
        if not isinstance(telefone, str):
            raise TypeError("Telefone deve ser um texto.")
        if not telefone.isdigit() or len(telefone) < 10:
            raise ValueError("Telefone deve conter ao menos 10 dígitos numéricos.")
        return telefone

    def _validar_email(self, email):
        if not isinstance(email, str):
            raise TypeError("Email deve ser um texto.")
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ValueError("Email inválido.")
        return email

    @abstractmethod
    def salario_final(self) -> float:
        pass

