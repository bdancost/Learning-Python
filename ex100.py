from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores de lista: ', end='')
    for cont in range(0, 5):
        n = randint(1, 100)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = list()
sorteia(números)
somaPar(números)
