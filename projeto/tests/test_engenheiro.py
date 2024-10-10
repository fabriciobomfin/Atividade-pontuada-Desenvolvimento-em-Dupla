from models.engenheiro import Engenheiro

@pytest.fixture
def engenheiro_valido(endereco_valido):
    return Engenheiro(
        nome="João",
        telefone="123456789",
        email="joao@example.com",
        endereco=endereco_valido,
        crea="12345"
    )

def test_engenheiro_valido(engenheiro_valido):
    assert engenheiro_valido.nome == "João"
    assert engenheiro_valido.telefone == "123456789"
    assert engenheiro_valido.email == "joao@example.com"
    assert engenheiro_valido.crea == "12345"
    assert engenheiro_valido.salario_final() == 0.0
