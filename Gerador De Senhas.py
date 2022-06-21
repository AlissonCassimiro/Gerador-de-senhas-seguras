import random

#mostrando a mensagem inicial
print("-=" * 20)
print("Bem vindo ao seu gerador de senhas!")
print("-=" * 20)

#Pegando as diversas letras, numeros e sinais, e vendo quantas senhas serão geradas.
letras = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%¨&*().,?0123456789'
numeros = input('quantidade de senhas geradas: ')
numeros = int(numeros)

#definindo o tamanho da senha, e vendo a quantidade de caracteres na senha.
tamanhosenha = input('tamanho da senha: ')
tamanhosenha = int(tamanhosenha)
print('\nAqui estao suas senhas: ')

for pwd in range(numeros):
    senhas = ''
    for c in range(tamanhosenha):
        senhas += random.choice(letras)
    print(senhas)