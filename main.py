from codigo.bytebank import Funcionario

# homem_de_ferro = Funcionario('Tony Stark', '29/05/1970', 15000)
# print(homem_de_ferro.idade())

def teste_idade():
    pantera_negra = Funcionario('TChalla', '21/05/1980', 10000)
    print(f'Teste = {pantera_negra.idade()}')

teste_idade()