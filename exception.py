# Programa que recebe e trata o erros 

class Error(Exception):
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Digite sua Nota (0-100):'))
        print(x)
        if x > 100:
            raise InputError('Nota não pode ser maior que 100' )
        elif x < 0:
            raise InputError('Nota não pode ser menor que 0')
        break
    except ValueError:
        print('Valor inválido: Deve-se digitar apenas números.')
    except InputError as ex:
        print(ex)
