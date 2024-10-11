# tests/test_endereco.py

import pytest
from enum import Enum
from projeto.models.enums.unidade_federativa import UnidadeFederativa  # Ajuste o caminho conforme necessário
from projeto.models.endereco import Endereco

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
        logradouro="Rua Exemplo",
        numero=123,
        complemento="Apto 45",
        cep="12345678",
        cidade="São Paulo",
        uf=MockUnidadeFederativa.SP
    )

class TestEndereco:
    def test_endereco_initialization_valid(self, valid_endereco):
        endereco = valid_endereco
        assert endereco.logradouro == "Rua Exemplo"
        assert endereco.numero == 123
        assert endereco.complemento == "Apto 45"
        assert endereco.cep == "12345678"
        assert endereco.cidade == "São Paulo"
        assert endereco.uf == MockUnidadeFederativa.SP

    def test_endereco_invalid_numero_type(self):
        with pytest.raises(TypeError) as excinfo:
            Endereco(
                logradouro="Rua Exemplo",
                numero="123",  # Tipo inválido
                complemento="Apto 45",
                cep="12345678",
                cidade="São Paulo",
                uf=MockUnidadeFederativa.SP
            )
        assert "Digite apenas números para o número da casa." in str(excinfo.value)

    def test_endereco_negative_numero(self):
        with pytest.raises(ValueError) as excinfo:
            Endereco(
                logradouro="Rua Exemplo",
                numero=-10,  # Número negativo
                complemento="Apto 45",
                cep="12345678",
                cidade="São Paulo",
                uf=MockUnidadeFederativa.SP
            )
        assert "Digite apenas números positivos para o número da casa." in str(excinfo.value)

    def test_endereco_invalid_cep_type(self):
        with pytest.raises(TypeError) as excinfo:
            Endereco(
                logradouro="Rua Exemplo",
                numero=123,
                complemento="Apto 45",
                cep=12345678,  # Tipo inválido
                cidade="São Paulo",
                uf=MockUnidadeFederativa.SP
            )
        assert "CEP deve ser informado como string." in str(excinfo.value)

    def test_endereco_invalid_cep_length(self):
        with pytest.raises(ValueError) as excinfo:
            Endereco(
                logradouro="Rua Exemplo",
                numero=123,
                complemento="Apto 45",
                cep="1234567",  # 7 dígitos
                cidade="São Paulo",
                uf=MockUnidadeFederativa.SP
            )
        assert "Digite um CEP válido com 8 dígitos numéricos." in str(excinfo.value)

    def test_endereco_invalid_cep_non_digit(self):
        with pytest.raises(ValueError) as excinfo:
            Endereco(
                logradouro="Rua Exemplo",
                numero=123,
                complemento="Apto 45",
                cep="1234ABCD",  # Caracteres não numéricos
                cidade="São Paulo",
                uf=MockUnidadeFederativa.SP
            )
        assert "Digite um CEP válido com 8 dígitos numéricos." in str(excinfo.value)

    def test_endereco_str_method(self, valid_endereco):
        endereco_str = str(valid_endereco)
        expected_str = "Rua Exemplo, 123, Apto 45, 12345678, São Paulo, São Paulo"
        assert endereco_str == expected_str
