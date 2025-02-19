##Jogo de Craps: Crie um programa que simule um jogo de Craps. O jogo funciona da seguinte maneira:
#O jogador lança dois dados, resultando em um valor entre 2 e 12. Na primeira jogada:

#Se o resultado for 7 ou 11, o jogador vence automaticamente (chamado de natural).
#Se o resultado for 2, 3 ou 12, o jogador perde imediatamente (chamado
#de craps).
#Se o resultado for 4, 5, 6, 8, 9 ou 10, esse valor se torna o Ponto do jogador.

#Caso um Ponto tenha sido estabelecido, o jogador continua lançando os dados:

#Se tirar o mesmo valor do Ponto, ele vence.
#Se tirar um 7 antes de repetir o Ponto, ele perde.
#Implemente a lógica para simular esse jogo e exiba o resultado de cada jogada.

import random
dado1 = random.randint(1, 6)
dado2 = random.randint(1, 6)
pontos = 0
resultado = dado1 + dado2

if resultado in (7, 11):
    print(f"Resultado: {resultado}")
    print("Jogador venceu: Natural")
elif resultado in (2, 3, 12):
    print(f"Resultado: {resultado}")
    print("Jogador perdeu: Craps")
elif resultado in (4, 5, 6, 8, 9, 10):
    pontos = resultado
    print(f"Ponto estabelecido: {pontos}")

    while True:
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        novo_resultado = dado1 + dado2
        print(f"Novo lançamento {dado1} + {dado2}: {novo_resultado}")

        if novo_resultado == pontos:
            print("Jogador venceu ao atingir o Ponto!")
            break
        elif novo_resultado == 7:
            print("Jogador perdeu ao tirar 7!")
            break
    