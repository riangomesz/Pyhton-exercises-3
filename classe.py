

# Função tudo que retorna valor
# Metodo é aquilo que não retorna

# Código que utiliza o método "class" em Python que também está interligado com as funções criadas por mim 

class Calculadora:
    def __init__(self):
        pass

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multi(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

    def potencia(self, valor_a, valor_b):
        return valor_a ** valor_b
    
calculadora = Calculadora()
print(calculadora.soma(10,3))
print(calculadora.subtracao(23,89))
print(calculadora.divisao(42,5))
print(calculadora.multi(56,1))
print(calculadora.potencia(7,2))
