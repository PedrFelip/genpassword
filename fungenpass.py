import random
# Caracteres para a senha
chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&'

print ("Bem vindo ao criador de senha!!")
#Entrada de dados para Criação da senha
number = int(input('Digite o número de senhas a serem geradas: '))
length = int(input('Digite o comprimento da senha desejada: '))

#função que eu estava usado de teste para aplicar na interface
def senhaaleatoria(number, length):
        for npws in range(number):
            password = ''
            for c in range(length):
                password += random.choice(chars)
            print (password)

senhaaleatoria(number, length)