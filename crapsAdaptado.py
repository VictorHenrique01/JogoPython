#Jogo de Craps - Competição contra a Máquina
#Objetivo: Desenvolver um jogo de Craps onde o jogador compete contra a máquina.
#  O jogador e a máquina irão lançar dois 
# dados, e a regra do jogo segue as mesmas regras do Craps tradicional, 
# mas agora ambos terão que estabelecer um ponto e 
# tentar alcançá-lo antes do outro, ou tirar um 7 e perder.
#Regras:
#Primeira Jogada:
#O jogador lança dois dados, resultando em um valor entre 2 e 12.
#Se o resultado for 7 ou 11, o jogador vence automaticamente (Natural).
#Se o resultado for 2, 3 ou 12, o jogador perde automaticamente (Craps).
#Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o "Ponto" do jogador.    

#Rodadas Seguintes:
#O jogador e a máquina jogam alternadamente.
#O jogador tenta tirar o mesmo valor do seu "Ponto" para vencer.
#A máquina tenta tirar o mesmo valor do seu "Ponto" para vencer.
#Se qualquer um dos dois tirar um 7 antes de repetir o valor do seu "Ponto", perde o jogo.
#O jogo continua até que um dos jogadores (jogador ou máquina) vença ou perca.

#Objetivo do Jogo:
#O objetivo é vencer o jogo antes da máquina, estabelecendo o "Ponto" e acertando esse valor novamente
#  antes de sair um 7.
#Caso qualquer um dos dois tire 7 antes de repetir seu Ponto, perde o jogo.
#Desafio Adicional: Implemente o código de modo que as jogadas sejam alternadas entre o jogador e a máquina.
#  Exiba os resultados das jogadas e informe claramente quem venceu ou perdeu após cada rodada.

import random

def jogar_dados():
    return random.randint(1, 6), random.randint(1, 6)

def iniciar_jogo():
    dado1, dado2 = jogar_dados()
    resultado1 = dado1 + dado2
    print(f"Jogador jogou: {dado1} + {dado2} = {resultado1}")

    if resultado1 in (7, 11):
        print("Jogador venceu: Natural!")
        return
    elif resultado1 in (2, 3, 12):
        print("Jogador perdeu: Craps!")
        return
    else:
        ponto_jogador = resultado1
        print(f"Jogador estabeleceu o ponto: {ponto_jogador}")
    
    dado3, dado4 = jogar_dados()
    resultado2 = dado3 + dado4
    print(f"Máquina jogou: {dado3} + {dado4} = {resultado2}")
    
    if resultado2 in (7, 11):
        print("Máquina venceu: Natural!")
        return
    elif resultado2 in (2, 3, 12):
        print("Máquina perdeu: Craps!")
        return
    else:
        ponto_maquina = resultado2
        print(f"Máquina estabeleceu o ponto: {ponto_maquina}")
    
    while True:
        dado1, dado2 = jogar_dados()
        resultado1 = dado1 + dado2
        print(f"Jogador jogou: {dado1} + {dado2} = {resultado1}")
        
        if resultado1 == ponto_jogador:
            print("Jogador venceu ao atingir o ponto!")
            return
        elif resultado1 == 7:
            print("Jogador perdeu ao tirar um 7!")
            return
        
        # Jogada da máquina
        dado3, dado4 = jogar_dados()
        resultado2 = dado3 + dado4
        print(f"Máquina jogou: {dado3} + {dado4} = {resultado2}")
        
        if resultado2 == ponto_maquina:
            print("Máquina venceu ao atingir o ponto!")
            return
        elif resultado2 == 7:
            print("Máquina perdeu ao tirar um 7!")
            return

iniciar_jogo()

        


