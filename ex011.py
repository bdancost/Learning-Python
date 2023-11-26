larg = float(input('Largura de parede: '))
alt = float(input('Altura de parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.2f}m²'.format(larg, alt, área))
tinta = área / 4
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))
