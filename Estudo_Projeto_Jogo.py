#Projeto 1 - Dese nvolvimento de Game em Python V1

#Import
import random 
from os import system, name

#Função para limpar a tela a cada execução
def limpa_tela():
 
    # Windows
    if name == 'nt':
        _ = system('cls')
 
    # Mac ou Linux
    else:
        _ = system('clear')
        


#Função 

def game():
    
	limpa_tela()     
	print("\nBem-vindo(a) ao jogo dda forca!")
	print("Adivinhe a palavra abaixo:\n")

# Lista de palvras para o jogo
palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']

# Escolhe randomicamente uma palvra
palvra = random.choice(palavras)

# List comprehensio
letras_descobertas = ['_' for letra in palvra]

# Número de chances
chances = 6

# Lista para as letras erradas
letras_erradas = []

#teste de update no github!!!
print("teste de github")




