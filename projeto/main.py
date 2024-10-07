import os
from models.engenheiro import Engenheiro
from models.medico import Medico
from models.endereco import Endereco
from models.enums.unidade_federativa import UnidadeFederativa
from models.enums.sexo import Sexo


# Limpar a tela do console
os.system("cls" if os.name == "nt" else "clear")

def main():
    # Cadastro do Médico
    print("Cadastro do Médico:")
    crm = input("CRM: ")
    sexo = Sexo[input("Sexo (FEMININO, MASCULINO, FLUIDO): ").strip().upper()]
    data_nascimento = input("Data de Nascimento (DD/MM/AAAA): ")
    
    endereco = Endereco(
        logradouro=input("Logradouro: "),
        numero=int(input("Número: ")),
        complemento=input("Complemento: "),
        cep=input("CEP: "),
        cidade=input("Cidade: "),
        uf=obter_unidade_federativa(input("Unidade Federativa (ex: SP ou São Paulo): "))
    )

    
   
def obter_unidade_federativa(uf_str):
    
    uf_str = uf_str.strip().upper()
    try:
        return UnidadeFederativa[uf_str]
    except KeyError:
        print("Unidade Federativa inválida. Por favor, insira a sigla ou o nome corretamente.")
        return obter_unidade_federativa(input("Unidade Federativa (ex: SP ou São Paulo): "))

if __name__ == "__main__":
    main()
