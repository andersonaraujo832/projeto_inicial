#Projeto 1 - Dese nvolvimento de Game em Python V1

#Import
import random 
from os import system, name

#Função para limpar a tela a cada execução

def limpa_tela():
	#Windows
	if name == 'nt':
	   	   _= system('cls')
	
	#Mac ou Linux
	else:
		_= system('clear')


print('Olá Vscode')
	



