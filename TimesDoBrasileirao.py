
lista = ('Atletico-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corintias', 'Bragantino', 'Fluminense', 'America-MG', 'Atletico-GO', 'Santos', 'Ceará-SC', 'Internacional', 'São Paulo', 'Atletico-PR', 'Cuiabá', 'Juventude', 'Gremio', 'Bahia', 'Sport Recife', 'Chapecoense')

primeiros = lista[0:5]
print(f'Os 5 primeiros são {primeiros}')

ultimos = lista[-4:]
print(f'Os ultimos 4 são {ultimos}')

ordenada = sorted(lista)
print(f'Em ordem alfabética: {ordenada}')

escolhido = lista.index('Bragantino') + 1
print(f'O Bragantino está em {escolhido}º lugar')
