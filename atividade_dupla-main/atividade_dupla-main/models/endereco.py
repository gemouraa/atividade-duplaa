
class Endereco():
    def __init__(self,logradouro: str,numero: str,complemento: str,cep: str,cidade:str) -> None:
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.cidade = cidade


    def __str__(self) -> str:
        return (f"\nLogadouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCep: {self.cep}"
                f"\nCidade: {self.cidade}")

 


