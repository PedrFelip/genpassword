import random
from tkinter import *
import tkinter as tk

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%&'

def senhaaleatoria(number = 1, length = 12):
        for npws in range(number):
            password = ''
            for c in range(length):
                password += random.choice(chars)
        resultadobotao.config(text=password)
def senhamyalgoritmo():
    resultadobotao.config(text="Em Breve")

def senhapersonalizada():
    resultadobotao.config(text="Em Breve")

root = Tk()
root.title("CrypticGuard")
root.configure(background='#1F0802')  
fonte_titulo = ("Roboto", 28, 'bold')

texto_inicial = Label(root, text='Bem-vindo ao CrypticGuard...', font=fonte_titulo, fg="#3C1D52", bg="#1F0802")
texto_inicial.pack(side="top", pady=0)

botao_opcao1 = tk.Button(root, text="Aleatoria", command=senhaaleatoria, font=("Arial", 12),
                          fg="#1C646D", bg="#1C646D", activeforeground="#CEF09D", background="#1F0802",)
botao_opcao1.pack(side="top", pady=5)  # Posicionado no topo com um pequeno espaço entre os botões

botao_opcao2 = tk.Button(root, text="Recomendação", command=senhamyalgoritmo, font=("Arial", 12),
                          fg="#1C646D", bg="#1C646D", activeforeground="#CEF09D", background="#1F0802",)
botao_opcao2.pack(side="top", pady=5)  # Posicionado abaixo do botão da Opção 1

botao_opcao3 = tk.Button(root, text="Personalizada", command=senhapersonalizada,font=("Arial", 12),
                          fg="#1C646D", bg="#1C646D", activeforeground="#CEF09D", background="#1F0802",)
botao_opcao3.pack(side="top", pady=5)  # Posicionado abaixo do botão da Opção 2

# Exibir para exibir o resultado
resultadobotao = tk.Label(root, text="Aguardando Senha...", font=("Arial", 30),fg="#A0CD60" ,bg="#1F0802")
resultadobotao.pack(side="top", pady=10)  # Posicionado abaixo do botão da Opção 3


root.mainloop()