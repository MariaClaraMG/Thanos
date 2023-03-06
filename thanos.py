import random

arvore_escondida = random.randint(0,50)

print("Bem - Vindos ao jogo do Thanos X Lanterna verde.\n")
print("Thanos está escondido em uma arvore numerada de 1 a 49, tente acha - lo\n")
print("Dificuldades: \n")
print("3 - Fácil: 15 tentativas")
print("2 - Médio: 10 tentativas")
print("1 - Dificil: 5 tentativas\n")

dificuldade = int(input("Escolha uma dificuldade: "))
tentativas = dificuldade * 5

while tentativas > 0:
    print("\nVocê possui: " + str(tentativas) + "tentativa(s)")

    escolha = int(input("\nEscolha uma árvore: "))

    if escolha == arvore_escondida:
        print("Parabéns! Você achou o Thanos.")
        break

    elif escolha < arvore_escondida:
        print("O Thanos não está na árvore selecionada. Tente uma árvore maior.")

    else:
        print("O Thanos não está na árvore selecionada. Tente uma árvore menor.")

    tentativas = tentativas - 1