#Jogo de Craps - Competição contra a Máquina
#Objetivo: Desenvolver um jogo de Craps onde o jogador compete contra a máquina. O jogador e a máquina irão lançar dois #dados, e a regra do jogo segue as mesmas regras do Craps tradicional, mas agora ambos terão que estabelecer um ponto e 
# tentar alcançá-lo antes do outro, ou tirar um 7 e perder.
#Regras:
#Primeira Jogada:
#O jogador lança dois dados, resultando em um valor entre 2 e 12.
#Se o resultado for 7 ou 11, o jogador vence automaticamente (Natural).
#Se o resultado for 2, 3 ou 12, o jogador perde automaticamente (Craps).
#Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o "Ponto" do jogador.
    
#A máquina também lança dois dados com a mesma regra:
#Se o resultado for 7 ou 11, a máquina vence automaticamente.
#Se o resultado for 2, 3 ou 12, a máquina perde automaticamente.
#Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o "Ponto" da máquina.
    
#Rodadas Seguintes:
#O jogador e a máquina jogam alternadamente.
#O jogador tenta tirar o mesmo valor do seu "Ponto" para vencer.
#A máquina tenta tirar o mesmo valor do seu "Ponto" para vencer.
#Se qualquer um dos dois tirar um 7 antes de repetir o valor do seu "Ponto", perde o jogo.
#O jogo continua até que um dos jogadores (jogador ou máquina) vença ou perca.

#Objetivo do Jogo:
#O objetivo é vencer o jogo antes da máquina, estabelecendo o "Ponto" e acertando esse valor novamente antes de sair um 7.
#Caso qualquer um dos dois tire 7 antes de repetir seu Ponto, perde o jogo.
#Desafio Adicional: Implemente o código de modo que as jogadas sejam alternadas entre o jogador e a máquina. Exiba os resultados das jogadas e informe claramente quem venceu ou perdeu após cada rodada.