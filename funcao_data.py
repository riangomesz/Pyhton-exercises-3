# Programa que utiliza as funções de data do calendário baseadas nas configurações atuais da CPU
# Quando executado o código ele imprime o dia o mês e o ano no console

from datetime import date

def trabalhando_com_data():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%d/%m/%Y')
    print(type(data_atual))
    print(data_atual_str)
    print(type(data_atual_str))

if __name__ == '__main__':
    #trabalhando com date()
    trabalhando_com_data()
