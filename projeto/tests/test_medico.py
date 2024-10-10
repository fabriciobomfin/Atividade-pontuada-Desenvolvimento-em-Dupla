from models.medico import Medico

@pytest.fixture
def medico_valido(endereco_valido):
    return Medico(
        nome="Ana",
        telefone="987654321",
        email="ana@example.com",
        endereco=endereco_valido,
        crm="67890"
    )

def test_medico_valido(medico_valido):
    assert medico_valido.nome == "Ana"
    assert medico_valido.telefone == "987654321"
    assert medico_valido.email == "ana@example.com"
    assert medico_valido.crm == "67890"
    assert medico_valido.salario_final() == medico_valido.salario_base + medico_valido.adicional
