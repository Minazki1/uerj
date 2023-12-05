import random
partidas = 0
tentativas = 0
print('Saudações usuário!')
nome = input('Qual o seu nome?: ')
while 1 == 1:

    print('\nDê uma olhada no nosso menu:')
    print('1.Embarcar em uma Nova Missão;')
    print('2.Explorar o último desafio;')
    print('3.Abandonar a Convenção(Sair).')
    escolha = int(input('O que você deseja fazer?: '))
    while escolha < 1 or escolha > 3:
        print('\nOpção indisponível')
        escolha = int(input('Escolha uma das opções: '))
    if escolha == 1:
        tentativas = 0
        partidas += 1
        num = random.choice(range(1, 101))
        print('\nNessa missão você necessitará enviar um transmissão com um número entre o intervalo de 1 a 100')
        num_player = int(input('Qual número deseja enviar?: '))
        tentativas += 1
        if num == num_player:
            print('\nVocê transmitiu o número correto!')
            print(f'Número de tentativas: {tentativas}')
        while num != num_player:
            if num_player > num:
                print('\nO número transmitido está em uma órbita mais elevada que o desejado')
                num_player = int(input('Escolha outro número com uma órbita menor: '))
                tentativas += 1
            if num_player < num:
                print('\nO número transmitido está em uma galáxia distante em relação ao número secreto')
                num_player = int(input('Escolha outro número com uma órbita maior: '))
                tentativas += 1
            if num_player == num:
                print('Você transmitiu o número correto!')
                print(f'Número de tentativas: {tentativas}')
    if escolha == 2:
        if partidas > 0:
            print('\nRegistros do último desafio:')
            print(f'Nome do jogador: {nome}')
            print(f'Número de tentativas: {tentativas}')
        else:
            print('\nNão há registros de jogos anteriores')

    if escolha == 3:
        print(f'\nO universo esperará ansiosamente para sua próxima missão.')
        exit()
