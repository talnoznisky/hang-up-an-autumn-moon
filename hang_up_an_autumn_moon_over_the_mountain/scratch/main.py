from random_art.randomart import draw, drunkenwalk
...

# generate your hash digest
digest = 'l;kasdasdlk'

# generate randomart, HASHNAME must be 10 characters
art = draw(drunkenwalk(digest))
print(art)