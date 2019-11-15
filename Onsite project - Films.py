film = {'name' : 'Redemption Shawshank', 'rating' : 87, 'year' : 1994, 'director' : 'Frank Darabont' }
print(film)
film['starring'] = 'Tim Robbins', 'Morgan Freeman'
film['budget'] = 200
print(film)
del film['budget']
print(film)
films = {}
films['DRAMA'] = film
print(films)

print('We can currently offer:')
print(list(films))

print(input('What kind of films do you like?'))
print()
print('HERE IT GOES:')
print(films['DRAMA'])

films.clear()
print(films)
print('DATABASE HAS BEEN ERASED')
