#Descrição do Jogo do Nim
#O jogo do Nim é um jogo matemático simples para dois jogadores. Ele é jogado com um número inicial de objetos (por #exemplo, 21 pedras), e os jogadores se revezam removendo um número limitado de objetos por turno. O objetivo pode variar, mas normalmente, o jogador que pegar o último objeto perde.
#Regra
#* O jogo começa com um número N de pedras (exemplo: 21).
#* Cada jogador pode retirar entre 1 e M pedras por turno (exemplo: entre 1 e 3 pedras).
#* O jogador que retirar a última pedra perde o jogo.
#O jogo pode ter dois modos:
#* Jogador vs. Jogador
#* Jogador vs. Computador (com estratégia)
#Dicas:
#Estrutura do jogo: Definição do número de pedras e da quantidade permitida por jogada.
#Loop de turnos: Alternância entre os jogadores, verificando as regras.
#Modo contra o computador: Implementar um algoritmo básico para o computador jogar. Se quiser desafiar os alunos, peça #para implementarem uma estratégia vencedora usando a lógica matemática do Nim.
#Exibição clara do jogo: O código deve mostrar quantas pedras restam e qual foi a jogada do adversário.

numero_inicial = int(input("Digite o número inicial de pedras: "))
numero_permitido = int(input("Qual o máximo de pedras que o jogador pode retirar por rodada? "))
pedras = numero_inicial
while pedras > 1:
    # alterar rodada entre jogadores
    retira_pedra = int(input("Quantas pedras deseja retirar? "))
    if retira_pedra >= 1 and retira_pedra <= numero_permitido:
        pedras -= retira_pedra
    else:
        print("Esse número não é permitido para retirada de pedras.")


        
    
        
        