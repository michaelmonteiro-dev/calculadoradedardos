from random import shuffle
# Tratamento de erros de entrada
def leiaPontos(msg):
    while True:
        try:
            ponto = int(input(msg))
        except (ValueError, TypeError):
            print('Entrada invalida, digite um número inteiro!')
        else:
            return ponto


print('=-='*10)
print('  * \033[4;35mCalculadora de Dardos\033[m *')
print('=-='*10)

while True:
    quantPontos = 50
    # Pontuação maxima da partida
    r = str(input('Deseja alterar a pontuação maxima padrão (S/N)? ')).strip().upper()
    while r not in 'SN':
        print('Entrada invalida, digite apenas "S" ou "N"')
        r = str(input('Deseja alterar a pontuação maxima padrão (S/N)? ')).strip().upper()
    if r == 'S':
        quantPontos = leiaPontos('Digite a pontuação máxima da partida: ')       
    print('=-='*10)
    # Registra o nome dos jogadores
    nomes = []
    while True:
        nome = str(input('Digite o nome do jogador: ')).strip().upper()
        nomes.append(nome)
        res = str(input('Deseja continuar (SN)? ')).strip().upper()
        print('=-='*10)
        while res not in 'SN':
            print('\033[1;31mEntrada invalida!\033[m')
            res = str(input('Deseja continuar? ')).strip().upper()
        if res == 'N':
            break

    # integrantes da partida
    print('        \033[4;33mParticipantes:\033[m')
    print('Essa será a ordem de jogada dos participantes: ')
    shuffle(nomes)
    for n in range(0, len(nomes)):
        print(nomes[n], end = ' | ')
    print('\n')

    #lista de pontuação
    p = []

    # declara o tamanho da lista
    for n in range(0, len(nomes)):
        p.append([0])

    # lê e registra a pontuação de cada jogador
    vencedor = False
    while True:
        for n in range(0, len(p)):
            print('\033[1;32mPróximo Jogador!\033[m')
            print('='*(len(nomes[n]) + 13))
            print(f'\033[1;34m{nomes[n]}\033[m é a sua vez!')
            ponto = leiaPontos('Digite o número acertado: ')
            p[n].append(ponto)
            print(f'Pontuação atual: \033[1;31m{sum(p[n])}\033[m')
            print('='*(len(nomes[n]) + 13))
            if sum(p[n]) >= quantPontos:
                break
        if sum(p[n]) >= quantPontos:
            print(f'Temos um vencedor: \033[4;32m{nomes[n]}!\033[m')
            break
    print('\n')
    print('=-='*10)    
    fim = str(input('Deseja jogar uma nova partida (S/N)? ')).strip().upper()
    print('=-='*10)
    while fim not in 'SN':
        print('=-='*10)
        print('\033[1;31mEntrada invalida!\033[m')
        fim = str(input('Deseja jogar uma nova partida (S/N)? ')).strip().upper()
        print('=-='*10)
    if fim == 'N':
        break