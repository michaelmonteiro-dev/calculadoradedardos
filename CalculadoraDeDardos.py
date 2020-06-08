'''
Este projeto foi escrito por mikelovi, com a ajuda ambundante do Rick.
Tá ligado como o bagulho é
'''


from random import shuffle
nomes = []
# Tratamento de erros de entrada
def leiaPontos(msg):
    while True:
        try:
            ponto = int(input(msg))
        except (ValueError, TypeError):
            print('Entrada invalida, digite um número inteiro!')
        else:
            return ponto


def registroJogadores():
    # Registra o nome dos jogadores
    
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
    return nomes


def decisãoSN(variavel, texto):
    while variavel not in 'SN':
        print('=-='*10)
        print('\033[1;31mEntrada invalida!\033[m')
        variavel = str(input(texto)).strip().upper()
        print('=-='*10)
    return variavel


print('=-='*10)
print('  * \033[4;35mCalculadora de Dardos\033[m *')
print('=-='*10)
registroJogadores()
while True:
    quantPontos = 50
    # Pontuação maxima da partida
    r = str(input('Deseja alterar a pontuação maxima padrão (S/N)? ')).strip().upper()
    decisãoSN(r, 'Deseja alterar a pontuação maxima padrão (S/N)? ')
    if r == 'S':
        quantPontos = leiaPontos('Digite a pontuação máxima da partida: ')       
    print('=-='*10)
    # integrantes da partida
    print('        \033[4;33mParticipantes:\033[m\n')
    print('Posição atual: ', end='')
    for n in range(0, len(nomes)):
        print(nomes[n], end = ' ')
    print('\n')
    print('Essa será a ordem de jogada dos participantes: ')
    shuffle(nomes)
    for n in range(0, len(nomes)):
        print(nomes[n], end = ' ')
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
    decisãoSN(fim, 'Deseja jogar uma nova partida (S/N)? ')
    if fim == 'N':
        break
    novosJogadores = str(input('Deseja alterar os jogadores (S/N)?')).strip().upper()
    decisãoSN(novosJogadores, 'Deseja alterar os jogadores (S/N)?')
    print('=-='*10)
    if novosJogadores == 'S':
        nomes.clear()
        registroJogadores()