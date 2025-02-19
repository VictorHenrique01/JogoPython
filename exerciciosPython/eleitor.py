#Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0
votos = [1, 2, 3]
eleitores = int(input("Digite o número total de eleitores: "))
for i in range(eleitores):
    voto = int(input(f" Eleitor {i + 1}, Digite o número do candidato que deseja votar: "))
    if not voto in votos:
        print("Números de candidatos disponíveis para voto são: 1, 2 ou 3. Tente novamente")
    elif voto == 1:
        candidato1 += 1
    elif voto == 2:
        candidato2 += 1
    elif voto == 3:
        candidato3 += 1

print("Quantidade de votos para candidato 1:", candidato1)
print("Quantidade de votos para candidato 2:", candidato2)
print("Quantidade de votos para candidato 3:", candidato3)

