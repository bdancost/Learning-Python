times = ('Botafogo', 'Palmeiras', 'Grêmio', 'Flamengo', 'Bragantino',
         'Fluminense', 'Paranaense', 'Fortaleza', 'Atlético Mineiro',
         'Cruzeiro', 'Internacional', 'Cuiabá', 'São Paulo', 'Corinthians',
         'Bahia', 'Goiás', 'Santos', 'Vasco', 'América -MG', 'Coritiba')
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Fortaleza está na {times.index("Fortaleza")+1}° posição')