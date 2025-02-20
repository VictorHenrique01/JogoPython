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
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
dado3 = random.randint(1, 6)
dado4 = random.randint(1, 6)

ponto_maquina = 0
ponto_jogador = 0

resultado1 = dado1 + dado2
resultado2 = dado3 + dado4

if resultado1 in (7, 11) and resultado2 in (7, 11):
    print(f"Resultado: {resultado1}")
    print("Jogador venceu: Natural")
elif resultado1 in (2, 3, 12) and resultado2 in (2, 3, 12):
    print(f"Resultado: {resultado1}")
    print("Jogador perdeu: Craps")
elif resultado1 in (4, 5, 6, 8, 9, 10) and resultado2 in (4, 5, 6, 8, 9, 10):
    ponto_jogador = resultado1
    ponto_maquina = resultado2
    print(f"Ponto estabelecido para jogador: {ponto_jogador}")
    print(f"Ponto estabelecido para máquina: {ponto_maquina}")

    while True:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        dado3 = random.randint(1, 6)
        dado4 = random.randint(1, 6)
        novo_resultado1 = dado1 + dado2
        novo_resultado2 = dado3 + dado4
        print(f"Novo lançamento de dados para jogador: {dado1} + {dado2}: {novo_resultado1}")
        print(f"Novo lançamento de dados para máquina: {dado3} + {dado4}: {novo_resultado2}")
        if novo_resultado1 == ponto_jogador:
            print("Jogador venceu ao atingir o Ponto!")
        break
    

        


