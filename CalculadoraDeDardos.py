print('=-='*10)
print('  * \033[4;35mCalculadora de Dardos\033[m *')
print('=-='*10)

while True:
    # lê o nome dos jogadores
    nomes = []
    while True:
        nome = str(input('Digite seu nome: ')).strip()
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
            ponto = int(input('Digite o numero acertado: '))
            p[n].append(ponto)
            print(f'Pontuação atual: \033[1;31m{sum(p[n])}\033[m')
            print('='*(len(nomes[n]) + 13))
            if sum(p[n]) >= 50:
                break
        if sum(p[n]) >= 50:
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