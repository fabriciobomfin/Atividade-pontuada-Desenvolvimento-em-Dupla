from models.enums.unidade_federativa import UnidadeFederativa


class Endereco:
    def __init__(self, logradouro: str, numero: int, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = logradouro
        self.numero = self._verificar_tipo_numero_da_casa(numero)
        self.complemento = complemento
        self.cep = self._verificar_tipo_cep(cep)  
        self.cidade = cidade
        self.uf = uf
    
    
    def _verificar_tipo_numero_da_casa(self, numero):
        if not isinstance(numero, int):
            raise TypeError("Digite apenas números para o número da casa.")
        if numero < 0:
            raise ValueError("Digite apenas números positivos para o número da casa.")
        return numero

    
    def _verificar_tipo_cep(self, cep):
        if not isinstance(cep, int):
            raise TypeError("Digite apenas números para o CEP.")
        if cep < 0:
            raise ValueError("Digite apenas números positivos para o CEP.")
        return cep

    def __str__(self):
        return f"{self.logradouro}, {self.numero}, {self.complemento}, {self.cep}, {self.cidade}, {self.uf.name}"
