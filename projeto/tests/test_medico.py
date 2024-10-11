import pytest

from projeto.models.endereco import Endereco
from projeto.models.medico import Medico
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa



@pytest.fixture

def medico_valido():
    return Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Sexo.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA","CPF","RG","Matricula",Setor.SAUDE,7000.0,"99999999")

#validando atributos

def test_id_valido(medico_valido):
    assert medico_valido.id == 18

def test_nome_valido(medico_valido):
    assert medico_valido.nome == "Nome"

def test_telefone_valido(medico_valido):
    assert medico_valido.telefone == "Telefone"

def test_email_valido(medico_valido):
    assert medico_valido.email == "Email"

def test_logradouro_valido(medico_valido):
    assert medico_valido.endereco.logradouro == "Logradouro"

def test_numero_valido(medico_valido):
    assert medico_valido.endereco.numero == "Numero"

def test_complemento_valido(medico_valido):
    assert medico_valido.endereco.complemento == "Complemento"

def test_cep_valido(medico_valido):
    assert medico_valido.endereco.cep == "CEP"

def test_cidade_valido(medico_valido):
    assert medico_valido.endereco.cidade == "Cidade"

def test_uf_valido(medico_valido):
    assert medico_valido.endereco.uf == UnidadeFederativa.BAHIA

def test_genero_valido(medico_valido):
    assert medico_valido.sexo == Genero.MASCULINO

def test_estado_civil_valido(medico_valido):
    assert medico_valido.estadoCivil == EstadoCivil.CASADO

def test_data_nascimento_valido(medico_valido):
    assert medico_valido.dataNascimento == "DD/MM/AAAA"

def test_cpf_valido(medico_valido):
    assert medico_valido.cpf == "CPF"

def test_rg_valido(medico_valido):
    assert medico_valido.rg == "RG"

def test_matricula_valido(medico_valido):
    assert medico_valido.matricula == "Matricula"

def test_setor_valido(medico_valido):
    assert medico_valido.setor == Setor.SAUDE

def test_salario_valido(medico_valido):
    assert medico_valido.salario == 7000.0

def test_crea_valido(medico_valido):
    assert medico_valido.crm == "99999999"

#testando exceções
def test_id_tipo_errado(medico_valido):
    with pytest.raises(TypeError, match = "valor inválido"):
        Medico("f", "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG", "Matricula", Setor.ENGENHARIA, 7000.0,"32575756")

def test_id_valor_negativo(medico_valido):
    with pytest.raises(ValueError, match = "valor inválido"):
        Medico(-18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG", "Matricula", Setor.ENGENHARIA, 7000.0,"32575756")

def test_nome_vazio(medico_valido):
    with pytest.raises(ValueError, match = "o nome não pode estar em branco"):
        Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG", "Matricula", Setor.ENGENHARIA, 7000.0,"32575756")

def test_salario_tipo_errado(medico_valido):
    with pytest.raises(TypeError, match = "dado incorreto"):
        Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG", "Matricula", Setor.ENGENHARIA, "7000.0","32575756")

def test_salario_negativo(medico_valido):
    with pytest.raises(ValueError, match = "salário não pode ser negativo"):
        Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG", "Matricula", Setor.ENGENHARIA, -7000.0,"32575756")

def test_cep_invalido(medico_valido):
    with pytest.raises(match = "CEP inválido"):
        Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP0", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG", "Matricula", Setor.ENGENHARIA, 7000.0,"32575756")
        
def test_rg_invalido(medico_valido):
    with pytest.raises(match = "RG inválido"):
        Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF", "RG0", "Matricula", Setor.ENGENHARIA, 7000.0,"32575756")

def test_cpf_invalido(medico_valido):
    with pytest.raises(match = "CPF inválido"):
        Medico(18, "Nome", "Telefone", "Email",
                    Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade", UnidadeFederativa.BAHIA),
                    Genero.MASCULINO,EstadoCivil.CASADO,
                    "DD/MM/AAAA", "CPF0", "RG", "Matricula", Setor.ENGENHARIA, 7000.0,"32575756")