cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'desoito',
        'dezenove', 'vinte')

while True:
        núm = int(input('Digite um número entre 0 e 20: '))
        if 0 <= núm <= 20:
                break
        print('Tente novamente. ', end='')
print(f'Você digitou o número {cont[núm]}')