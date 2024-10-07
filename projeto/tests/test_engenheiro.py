
import pytest
from models.engenheiro import Engenheiro
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def engenheiro_valido():
    endereco = Endereco(
        logradouro="Av. Paulista",
        numero="1000",
        complemento="Apt. 101",
        cep="01311-200",
        cidade="São Paulo",
        uf=UnidadeFederativa.SÃO_PAULO
    )
    engenheiro = Engenheiro(
        nome="João da Silva",
        telefone="(11) 99999-9999",
        email="joao.silva@empresa.com",
        endereco=endereco,
        crea="123456-SP"
    )
    engenheiro.salario_base = 5000.0
    engenheiro.bonus = 500.0
    return engenheiro

def test_eng_plano_final(engenheiro_valido):
    assert engenheiro_valido.salario_final() == 5500.0
