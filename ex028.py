from random import randint
from time import sleep

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# n4 = float(input('Digite a quarta nota: '))
# m = (n1 + n2 + n3 + n4)/4
# print ('A sua média foi {:.1f}'.format(m))
# print ('Parabéns' if m >= 6 else 'Estude mais')

computador = randint(0, 5) # Faz o computador "Pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))


