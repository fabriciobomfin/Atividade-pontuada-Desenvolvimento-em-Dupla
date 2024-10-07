
import pytest
from models.medico import Medico
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def medico_valido():
    endereco = Endereco(
        logradouro="Rua das Flores",
        numero="200",
        complemento="Casa",
        cep="04000-000",
        cidade="Rio de Janeiro",
        uf=UnidadeFederativa.RIO_DE_JANEIRO
    )
    medico = Medico(
        nome="Maria Oliveira",
        telefone="(21) 88888-8888",
        email="maria.oliveira@hospital.com",
        endereco=endereco,
        crm="7891011-RJ"
    )
    medico.salario_base = 7000.0
    medico.adicional = 1000.0
    return medico

def test_medico_salario_final(medico_valido):
    assert medico_valido.salario_final() == 8000.0
