import pytest
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    return Endereco(
        logradouro="Rua Principal",
        numero=123,
        complemento="Apto 101",
        cep=12345678,
        cidade="Cidade Exemplo",
        uf=UnidadeFederativa.SP
    )

def test_endereco_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua Principal"
    assert endereco_valido.numero == 123
    assert endereco_valido.complemento == "Apto 101"
    assert endereco_valido.cep == 12345678
    assert endereco_valido.cidade == "Cidade Exemplo"
    assert endereco_valido.uf == UnidadeFederativa.SP

def test_numero_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="Digite apenas números positivos para o número da casa."):
        Endereco("Rua Principal", -123, "Apto 101", 12345678, "Cidade Exemplo", UnidadeFederativa.SP)

def test_numero_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="Digite apenas números para o número da casa."):
        Endereco("Rua Principal", "123", "Apto 101", 12345678, "Cidade Exemplo", UnidadeFederativa.SP)

def test_cep_negativo_retorna_mensagem_erro():
    with pytest.raises(ValueError, match="Digite apenas números positivos para o CEP."):
        Endereco("Rua Principal", 123, "Apto 101", -12345678, "Cidade Exemplo", UnidadeFederativa.SP)

def test_cep_tipo_invalido_retorna_mensagem_erro():
    with pytest.raises(TypeError, match="Digite apenas números para o CEP."):
        Endereco("Rua Principal", 123, "Apto 101", "12345678", "Cidade Exemplo", UnidadeFederativa.SP)
