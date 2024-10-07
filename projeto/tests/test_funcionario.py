
import pytest
from models.funcionario import Funcionario

def test_funcionario_abstract():
    with pytest.raises(TypeError):
        Funcionario(
            nome="Nome",
            telefone="123456789",
            email="email@example.com",
            endereco=None  
        )
