# tests/test_engenheiro.py

import pytest
from enum import Enum
from projeto.models.enums.unidade_federativa import UnidadeFederativa  # Ajuste o caminho conforme necessário
from projeto.models.endereco import Endereco
from projeto.models.engenheiro import Engenheiro

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
def valid_engenheiro_data(valid_endereco):
    return {
        "nome": "João Silva",
        "telefone": "11987654321",
        "email": "joao.silva@example.com",
        "endereco": valid_endereco,
        "crea": "CREA12345"
    }

class TestEngenheiro:
    def test_engenheiro_initialization_valid(self, valid_engenheiro_data):
        engenheiro = Engenheiro(
            nome=valid_engenheiro_data["nome"],
            telefone=valid_engenheiro_data["telefone"],
            email=valid_engenheiro_data["email"],
            endereco=valid_engenheiro_data["endereco"],
            crea=valid_engenheiro_data["crea"]
        )
        assert engenheiro.nome == "João Silva"
        assert engenheiro.telefone == "11987654321"
        assert engenheiro.email == "joao.silva@example.com"
        assert engenheiro.endereco == valid_engenheiro_data["endereco"]
        assert engenheiro.crea == "CREA12345"
        assert engenheiro.salario_base == 5000.0
        assert engenheiro.bonus_projetos == 1000.0

    def test_engenheiro_salario_final(self, valid_engenheiro_data):
        engenheiro = Engenheiro(
            nome=valid_engenheiro_data["nome"],
            telefone=valid_engenheiro_data["telefone"],
            email=valid_engenheiro_data["email"],
            endereco=valid_engenheiro_data["endereco"],
            crea=valid_engenheiro_data["crea"]
        )
        assert engenheiro.salario_final() == 6000.0  # 5000 + 1000

    def test_engenheiro_invalid_nome_type(self, valid_engenheiro_data):
        with pytest.raises(TypeError) as excinfo:
            Engenheiro(
                nome=123,  # Tipo inválido
                telefone=valid_engenheiro_data["telefone"],
                email=valid_engenheiro_data["email"],
                endereco=valid_engenheiro_data["endereco"],
                crea=valid_engenheiro_data["crea"]
            )
        assert "O nome deve ser um texto." in str(excinfo.value)

    def test_engenheiro_empty_nome(self, valid_engenheiro_data):
        with pytest.raises(ValueError) as excinfo:
            Engenheiro(
                nome="   ",  # Nome vazio
                telefone=valid_engenheiro_data["telefone"],
                email=valid_engenheiro_data["email"],
                endereco=valid_engenheiro_data["endereco"],
                crea=valid_engenheiro_data["crea"]
            )
        assert "Nome não pode estar vazio." in str(excinfo.value)

    def test_engenheiro_invalid_telefone(self, valid_engenheiro_data):
        with pytest.raises(ValueError) as excinfo:
            Engenheiro(
                nome=valid_engenheiro_data["nome"],
                telefone="12345",  # Telefone muito curto
                email=valid_engenheiro_data["email"],
                endereco=valid_engenheiro_data["endereco"],
                crea=valid_engenheiro_data["crea"]
            )
        assert "Telefone deve conter ao menos 10 dígitos numéricos." in str(excinfo.value)

    def test_engenheiro_invalid_email(self, valid_engenheiro_data):
        with pytest.raises(ValueError) as excinfo:
            Engenheiro(
                nome=valid_engenheiro_data["nome"],
                telefone=valid_engenheiro_data["telefone"],
                email="joao.silvaexample.com",  # Email inválido
                endereco=valid_engenheiro_data["endereco"],
                crea=valid_engenheiro_data["crea"]
            )
        assert "Email inválido." in str(excinfo.value)
