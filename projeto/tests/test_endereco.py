
import pytest
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    return Endereco(
        logradouro="Rua das Flores",
        numero="123",
        complemento="Apt. 101",
        cep="01234-567",
        cidade="São Paulo",
        uf=UnidadeFederativa.SÃO_PAULO
    )

def test_endereco_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua das Flores"
    assert endereco_valido.numero == "123"
    assert endereco_valido.complemento == "Apt. 101"
    assert endereco_valido.cep == "01234-567"
    assert endereco_valido.cidade == "São Paulo"
    assert endereco_valido.uf == UnidadeFederativa.SÃO_PAULO

def test_endereco_cep_invalido():
    with pytest.raises(ValueError, match="CEP inválido."):
        Endereco(
            logradouro="Rua Sem Nome",
            numero="456",
            complemento="",
            cep="ABCDE",  
            cidade="Cidade",
            uf=UnidadeFederativa.BAHIA
        )

def test_endereco_logradouro_vazio():
    with pytest.raises(ValueError, match="O logradouro não pode estar vazio."):
        Endereco(
            logradouro="",  
            numero="123",
            complemento="",
            cep="12345678",
            cidade="Cidade",
            uf=UnidadeFederativa.BAHIA
        )
