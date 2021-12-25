from hang_up_an_autumn_moon_over_the_mountain.oracle.main import Oracle

o = Oracle()
digests = o.create_digests()

for digest in digests:
    print(digest)