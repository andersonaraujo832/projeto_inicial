# Hangman Game (Jogo da Forca)
# Programação Orientada a Objetos

import random

# Tabuleiro
board = [
    """

>>>>>>>>>> Hangman <<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========""",
    """

+---+
|   |
O   |
    |
    |
    |
=========""",
    """

+---+
|   |
O   |
|   |
    |
    |
=========""",
    """

+---+
|   |
O   |
/|   |
     |
     |
=========""",
    """

+---+
|   |
O   |
/|\  |
     |
     |
=========""",
    """

+---+
|   |
O   |
/|\  |
/    |
     |
=========""",
    """

+---+
|   |
O   |
/|\  |
/ \  |
     |
=========""",
]


# Classe Hangman
class Hangman:
    def __init__(self, word):
        self.word = word  # Palavra secreta
        self.guessed_letters = []  # Letras já tentadas
        self.wrong_attempts = 0  # Número de erros

    # Mostrar o estado atual do jogo
    def display_hangman(self):
        print(board[self.wrong_attempts])
        hidden_word = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                hidden_word += letter
            else:
                hidden_word += "_"
        print("Palavra:", " ".join(hidden_word))
        print("Letras já usadas:", " ".join(self.guessed_letters))
        print("\n")

    # Jogador tenta uma letra
    def guess(self, letter):
        if letter not in self.guessed_letters:
            self.guessed_letters.append(letter)
            if letter not in self.word:
                self.wrong_attempts += 1
                print(f"A letra '{letter}' não está na palavra.")
        else:
            print(f"Você já tentou a letra '{letter}'.")

    # Verifica se o jogo terminou (erros esgotados)
    def game_over(self):
        return self.wrong_attempts >= len(board) - 1

    # Verifica se o jogador venceu
    def is_winner(self):
        return all(letter in self.guessed_letters for letter in self.word)


# Função principal
def main():
    # Lista de palavras
    word_list = ["python", "dados", "alura", "engenharia", "streamlit", "forca"]
    secret_word = random.choice(word_list)

    game = Hangman(secret_word)

    print("Bem-vindo ao jogo da Forca!")
    while not game.game_over() and not game.is_winner():
        game.display_hangman()
        guess = input("Digite uma letra: ").lower()
        game.guess(guess)

    # Resultado final
    if game.is_winner():
        print("Parabéns! Você venceu! A palavra era:", secret_word)
    else:
        game.display_hangman()
        print("Game over! A palavra era:", secret_word)


# Executa o jogo
if __name__ == "__main__":
    main()
