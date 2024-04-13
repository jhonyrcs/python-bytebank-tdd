from codigo.bytebank import Funcionario
import pytest

class TestClass:
    def test_quando_idade_recebe_21_05_1980_deve_retornar_44(self):
        #Given(Contexto)
        entrada = '21/05/1980'
        esperado = 44

        pantera_negra = Funcionario('TChalla', entrada, 10000)
        
        #When(Ação)
        resultado = pantera_negra.idade()

        #Then(Desfecho)
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Tony_Stark_deve_retornar_apenas_Start(self):
        #Given(Contexto)
        entrada = 'Tony Stark'
        esperado = 'Stark'

        homem_de_ferro = Funcionario(entrada, '29/05/1970', 10000)
        
        #When(Ação)
        resultado = homem_de_ferro.sobrenome()

        #Then(Desfecho)
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        #Given(Contexto)
        entrada_salario = 100000
        entrada_nome = 'Steve Rogers'
        esperado = 90000

        capitao_america = Funcionario(entrada_nome, '04/07/1918', entrada_salario)        
        capitao_america.decrescimo_salario()
        
        #When(Ação)
        resultado = capitao_america.salario
        
        #Then(Desfecho)
        assert resultado == esperado

    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_10000_deve_retornar_1000(self):
        #Given(Contexto)
        entrada = 10000
        esperado = 1000

        viuva_negra = Funcionario('Natasha Romanoff', '22/11/1984', entrada)
        
        #When(Ação)
        resultado = viuva_negra.calcular_bonus()

        #Then(Desfecho)
        assert resultado == esperado
    
    @pytest.mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        #Given(Contexto)
        with pytest.raises(Exception):
            entrada = 100000000

            thor = Funcionario('Thor Odinson', '05/06/0515', entrada)

            #When(Ação)
            resultado = thor.calcular_bonus()

            #Then(Desfecho)
            assert resultado

    # def test_retorno_str(self):
    #     #Given(Contexto)
    #     nome, data_nascimento, salario = 'Bruce Banner', '01/05/1969', 10000
    #     esperado = 'Funcionario(Bruce Banner, 01/05/1969, 10000)'

    #     hulk = Funcionario(nome, data_nascimento, salario)
        
    #     #When(Ação)
    #     resultado = hulk.__str__()

    #     #Then(Desfecho)
    #     assert resultado == esperado