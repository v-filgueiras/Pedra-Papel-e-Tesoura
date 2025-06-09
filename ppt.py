import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
placar = {'Usuário': 0, 'Máquina': 0}

def escolha_maquina():
    return random.randint(0, 2)

def determinar_vencedor(usuario, maquina):
    if usuario == maquina:
        return 'Empate'
    elif (usuario - maquina) % 3 == 1:
        return 'Usuário'
    else:
        return 'Máquina'

while True:
    try:
        escolha_usuario = int(input('Escolha uma opção: 0 - Pedra | 1 - Papel | 2 - Tesoura\n'))

        if escolha_usuario not in [0, 1, 2]:
            print('Escolha inválida. Tente novamente.')
            continue

        escolha_computador = escolha_maquina()

        print(f'Usuário escolheu: {opcoes[escolha_usuario]}')
        print(f'Máquina escolheu: {opcoes[escolha_computador]}')

        resultado = determinar_vencedor(escolha_usuario, escolha_computador)

        if resultado == 'Empate':
            print('Empate!')
        else:
            placar[resultado] += 1
            print(f'{resultado} venceu esta rodada!')

        print(f'Placar: Usuário {placar["Usuário"]} x {placar["Máquina"]}')
        print('-' * 40)

    except ValueError:
        print('Entrada inválida. Digite apenas 0, 1 ou 2.\n')
