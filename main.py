'''
Jogo do Adivinhe o Número
2024.07.30
Beatriz Costa
'''
# Objetivo: Desenvolver um jogo, onde o usuário deverá tentar adivinhar um número secreto sorteado pelo PC

# Módulos e Bibliotecas
from random import randint # Biblioteca do jogo

# Variáveis
msg = '' # Variável para msgs
numeroSecreto = 0 # Usado para sorteio do número secreto

# CONSTANTES
CAR = '*' # Caractere usado para desenhar a estrutura do jogo
TDT = 40 # Tamanho da Tela a ser desenhada
MAR = 2 # Margem de dois caracteres
INI = 1 # Inicio dos sorteios do numero vai de 1
FIM = 100 # ate o 100
TVS = 3 # Numero de tentarivas

# Listas
listaMsgs = [] # Variável para lista de msgs

# Funções
# Função para mostrar uma linha de Caracteres
def mostraLinha(): # Mostra as linhas 
  print(CAR*TDT) # Mostra o tamanho da tela "vezes" qual caractere será usado para desenhar a tela

# Função para mostrar um texto centralizado entre um número de Caracteres
def msgCentro(msg): # Mensagem do centeo
  print(f'{CAR} {msg:^{TDT-MAR-MAR}} {CAR}') # Mostra todo o comando da tela quando começamos o jogo

# Função para mostrar um cabeçalho com texto entre linhas
def cabecalho(listaMsgs): # Função do cabeçalho 
  mostraLinha() # Aparece as linhas 
  for msg in listaMsgs: # Outra função (das linhas para mostrar as mensagens )
    msgCentro(msg) # Mensagem do centro
  mostraLinha() # Mostra as linhas do jogo

# Função para Sortear o número secreto
def sorteiaNum(): # Sorteia o numero secreto
  numeroSecreto = randint(INI,FIM) # o Numero secreto será (inteiro) de 1 ate 100
  return numeroSecreto #Volta ao número secreto

# Função para pegar a resposta e testar se é um número
def pegaResposta(): # Pega a sua resposta 
  resposta = input(f'{CAR} Sua resposta: ') # Aparecera a mensagem "Sua resposta "
  while not resposta.isdigit(): # Esse comando será para verificar e dizer que está errado quando é colocado qualquer letra inves de um número 
    listaMsgs = ['Resposta Inválida!', 'Tente um Número'] # Essa mensagem aparecera e dira para você tentar um número 
    cabecalho(listaMsgs) # Cabeçalho com as mensagens 
    resposta = input(f'{CAR} Sua resposta:') # Novamente aparecera para colocar a sua resposta 
  resposta = int(resposta) # Irá aparecer isso se você colocar a reposta 
  return resposta # Retorna a resposta 
  
# Função para dar a Dica
def dica(numeroSecreto, resposta): # Se seu numero nao for o numero secreto, esse comando lhe dara a dica de se o NS for maior ou menor
  if numeroSecreto < resposta: # Comando que testa se o NS é menor que a resposta 
    cabecalho('Tente um Número MENOR!') # Mensagem que aparecera o NS for menor
  else: # Comando se o número for maior
    cabecalho('Tente um Número MAIOR!') # Mensagem que aparecera se o NS for maior
    
# Função para Startar o jogo
def startGame(): # Começará o jogo
  TVS = 3 # O jogo tem 3 temtativas 
  numeroSecreto = sorteiaNum() # Temos a variável NS que receber a função de sortear um número 
  listaMsgs = ['JOGO DO ADIVINHE O NÚMERO', 'Powered by Beatriz Costa'] # Mensagem que irá aparecer ao iniciarmos o jogo 
  cabecalho(listaMsgs) # Cabeçalho com as mensagens 
  playGame(TVS, numeroSecreto) # Pada jogar, com as tentativas e o NS

def playGame(TVS, numeroSecreto): # Função para iniciar o jogo,com as tentativas e o NS
  for tentativas in range (TVS): # Código das tentativas 
    resposta = pegaResposta() # Pega a sua resposta 
    testeAcerto = resposta == numeroSecreto # Verifica seu acerto,com a resposta e o número secreto 
    if testeAcerto: # Se você acerta aparecera 
      listaMsgs = ['OLOKO BICHO!!!', 'ACERTOU MEMO!!!,' 'PARABÉNS YOU WIN!'] # Essa mensagem!
      cabecalho(listaMsgs) # Cabeçalho com as mensagens 
      break # Ou se você errar
    elif tentativas != 2: # Terá apenas mais duas tentativas 
      listaMsgs = ['SE É RUIM D+', 'NÃO É ASSIM CRIATURA!'] # Essa mensagem irá aparecer
      cabecalho(listaMsgs) # Cabeçalho com as mensagens 
      dica(numeroSecreto, resposta) # O comando da dica verefica o número secreto com a resposta 
    else: # Comando se você errar(de novo)
      cabecalho('MelDels Que Feio!!!') # Se você errar novamente, essa mensagem aparecerá 
  else: # Comando quando você perde o jogo
     listaMsgs = ['FIM DE JOGO', 'O NUM SECRETO ERA', numeroSecreto, 'PARABÉNS YOU LOSE!'] # Mensagem que aparecerá se você perder o jogo,e mostra qual era o número secreto
     cabecalho(listaMsgs) # Cabeçalho com as mensagens 
     listaMsgs = ['Deseja Jogar Novamente?', '[0 - NÃO]', '[1 - SIM'] # Mensagem que aparecerá peeguntando se você deseja jogar novamente ou não 
     cabecalho(listaMsgs) # Cabeçalho com as mensagens 
     resposta = pegaResposta() # Pega qual for a sua resposta (0 - NAO ou 1 - SIM)
     if resposta == 1: # Uma resposta apenas 
      startGame() # Continua o jogo 
     else: # Comando quando o jogo termina
      listaMsgs = ['FOI BOM JOGAR COM VOCÊ!', 'ATÉ A PRÓXIMA'] # Mensagem aparece se você deseja não jogar novamente 
      cabecalho(listaMsgs) # Cabeçalho com as mensagens

  
# Programa Principal
startGame() # Comando para iniciar o jogo