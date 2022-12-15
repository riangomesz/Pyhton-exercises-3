# Simulador simples de compras em Python
# utilizando o método da lista

lista_de_compras = []
print("Olá você está no sacolão do Verdemar.\n E acabou de ganhar um voucher com \n descontos para escolher dez alimetos.")

for x in range(4):
    alimentos = str(input(" Selecione seus alimentos: "))
    lista_de_compras.append(alimentos)
print("Alimentos selecionados: "+str(lista_de_compras))

    
