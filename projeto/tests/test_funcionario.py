from models.funcionario import Funcionario

def test_salario_final_abstrato():
    with pytest.raises(TypeError, match="Can't instantiate abstract class Funcionario"):
        Funcionario("João", "123456789", "joao@example.com", endereco_valido)
