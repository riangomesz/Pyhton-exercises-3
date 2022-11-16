# Programa que recebe uma frase e uma palavra escrita pelo o usuário 
# Após isso ele retorna ao usuário se a palavra está na frase ou não está na frase


text = input()
word = input()

def search(text,word):
    if word in text:
       return "Word found"
    else:
       return "Word not found"


print(search(text, word))
