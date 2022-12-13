# Função datime que importa um horário pré estabelecido no computador 

from datetime import time

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second= 30)
    print(horario)
    horario_str = horario.strftime('%H:%M:%S')
    print(type(horario_str))

if __name__ == '__main__':
    #trabalhando com time()
    trabalhando_com_time()
    
