# Projeto 1 - Desenvolvimento de Game em Python V1

# Import
import random
from os import system, name


# Função para limpar a tela a cada execução
def limpa_tela():

    # Windows
    if name == "nt":
        _ = system("cls")

    # Mac ou Linux
    else:
        _ = system("clear")


# Função


def game():

    limpa_tela()
    print("\nBem-vindo(a) ao jogo dda forca!")
    print("Adivinhe a palavra abaixo:\n")


# Lista de palvras para o jogo
palavras = ["banana", "abacate", "uva", "morango", "laranja"]

# Escolhe randomicamente uma palvra
palavra = random.choice(palavras)

# List comprehensio
letras_descobertas = ["_" for letra in palavra]

# Número de chances
chances = 6

# Lista para as letras erradas
letras_erradas = []

# Loop enquanto número de chances for maior que zero
while chances > 0:

    # print
    print(" ".join(letras_descobertas))
    print("\nChances restantes:", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    # Tentativa
    tentativa = input("\nDigite uma letra: ").lower()

    # Condicional
    if tentativa in palavra:
        index = 0
        for letra in palavra:
            if tentativa == letra:
                letras_descobertas[index] = letra
            index += 1
    else:
        chances -= 1
        letras_erradas.append(tentativa)
