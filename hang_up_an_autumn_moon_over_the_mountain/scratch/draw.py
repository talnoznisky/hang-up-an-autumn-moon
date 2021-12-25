import hang_up_an_autumn_moon_over_the_mountain.oracle.random_art.randomart as ra
from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle

o = Oracle()
digests = [ra.drunkenwalk(s['substring'].encode()) for s in o.cards]

art = ra.draw(digests)

print(art)
