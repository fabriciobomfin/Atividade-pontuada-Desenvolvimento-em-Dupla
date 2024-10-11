# tests/test_funcionario.py

import pytest
from abc import ABC, abstractmethod
from enum import Enum
from projeto.models.enums.unidade_federativa import UnidadeFederativa  # Ajuste o caminho conforme necessário
from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro
from projeto.models.medico import Medico

# Mock da Enum UnidadeFederativa para testes, caso necessário
class MockUnidadeFederativa(Enum):
    SP = "São Paulo"
    RJ = "Rio de Janeiro"
    MG = "Minas Gerais"
    # Adicione outros estados conforme necessário

    @property
    def nome(self):
        return self.value

@pytest.fixture
def valid_endereco():
    return Endereco(
        logradouro="Av. Teste",
        numero=456,
        complemento="Casa",
        cep="87654321",
        cidade="Rio de Janeiro",
        uf=MockUnidadeFederativa.RJ
    )

@pytest.fixture
def valid_funcionario_data(valid_endereco):
    return {
        "nome": "João Silva",
        "telefone": "11987654321",
        "email": "joao.silva@example.com",
        "endereco": valid_endereco
    }

class TestFuncionario:
    def test_funcionario_cannot_be_instantiated(self, valid_funcionario_data):
        with pytest.raises(TypeError) as excinfo:
            Funcionario(
                nome=valid_funcionario_data["nome"],
                telefone=valid_funcionario_data["telefone"],
                email=valid_funcionario_data["email"],
                endereco=valid_funcionario_data["endereco"]
            )
        assert "Can't instantiate abstract class Funcionario with abstract methods salario_final" in str(excinfo.value)

    def test_subclass_engenheiro_implements_salario_final(self, valid_funcionario_data):
        engenheiro = Engenheiro(
            nome=valid_funcionario_data["nome"],
            telefone=valid_funcionario_data["telefone"],
            email=valid_funcionario_data["email"],
            endereco=valid_funcionario_data["endereco"],
            crea="CREA12345"
        )
        assert isinstance(engenheiro, Funcionario)
        assert engenheiro.salario_final() == 6000.0  # 5000 + 1000

    def test_subclass_medico_implements_salario_final_default(self, valid_funcionario_data):
        medico = Medico(
            nome=valid_funcionario_data["nome"],
            telefone=valid_funcionario_data["telefone"],
            email=valid_funcionario_data["email"],
            endereco=valid_funcionario_data["endereco"],
            crm="CRM67890"
        )
        assert isinstance(medico, Funcionario)
        assert medico.salario_final() == 10000.0  # 8000 + 2000

    def test_subclass_medico_implements_salario_final_custom(self, valid_funcionario_data):
        medico = Medico(
            nome=valid_funcionario_data["nome"],
            telefone=valid_funcionario_data["telefone"],
            email=valid_funcionario_data["email"],
            endereco=valid_funcionario_data["endereco"],
            crm="CRM67890",
            salario_base=9000.0,
            adicional=2500.0
        )
        assert isinstance(medico, Funcionario)
        assert medico.salario_final() == 11500.0  # 9000 + 2500
