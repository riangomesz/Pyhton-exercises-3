def word_counter(list_words):
    counter = []
    for x in list_words:
        qtde = len(x)
        counter.append(qtde)
    return counter
if __name__ == '__main__':
    list = ['dog','cat','bird','wolf']
    print(word_counter(list))
    
