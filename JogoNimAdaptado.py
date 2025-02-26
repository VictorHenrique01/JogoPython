import random

# Função para o modo Jogador vs Computador
def modo_computador(pedras, numero_permitido):
    return random.randint(1, min(numero_permitido, pedras))

def jogo():
    print("Insira as regras do jogo.")
    numero_inicial = int(input("Digite o número inicial de pedras: "))
    numero_permitido = int(input("Qual o máximo de pedras que o jogador pode retirar por rodada? "))
    modo = input("Escolha o modo de jogo (1 para Jogador vs Jogador, 2 para Jogador vs Computador): ")
    
    pedras = numero_inicial
    vez_jogador = 1  
    rodada = 0

    
    while pedras > 0:
        rodada += 1
        
        if modo == '1':  
            if vez_jogador == 1:
                print(f"\nRodada {rodada} para Jogador 1!")
            else:
                print(f"\nRodada {rodada} para Jogador 2!")
        
        elif modo == '2':  
            if vez_jogador == 1:
                print(f"\nRodada {rodada} para Jogador!")
            else:
                print(f"\nRodada {rodada} para Computador!")


        if vez_jogador == 1:
            retira_pedra = int(input(f"Quantas pedras deseja retirar? (Entre 1 e {numero_permitido}) "))
            
          
            if retira_pedra >= 1 and retira_pedra <= numero_permitido:
                if retira_pedra > pedras:
                    print(f"Você não pode retirar mais pedras do que o total disponível. Restam apenas {pedras} pedras.")
                    continue  
                pedras -= retira_pedra
                print(f"Restam {pedras} pedras.")
            else:
                print(f"Esse número não é permitido para retirada de pedras. Você deve retirar entre 1 e {numero_permitido} pedras.")
        
       
        elif vez_jogador == 2:
            retira_pedra = modo_computador(pedras, numero_permitido)
            print(f"O Computador retirou {retira_pedra} pedras.")
            pedras -= retira_pedra
            print(f"Restam {pedras} pedras.")

        
        if pedras == 0:
            if vez_jogador == 1:
                print("Você perdeu! Retirou a última pedra.")
            else:
                print("O Computador perdeu! Retirou a última pedra.")
            break

        
        if vez_jogador == 1:
            vez_jogador = 2
        else:
            vez_jogador = 1

jogo()
