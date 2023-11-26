real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 4.87
pesoarg = real / 0.019
euro = real / 5.34
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))
print('Com R${:.2f} você pode comprar ${:.2f}'.format(real, pesoarg))
print('Com R${:.2f} você pode comprar €${:.2f}'.format(real, euro))
