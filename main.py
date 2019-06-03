from builtins import print

cast = ["cleese","palin","jones","idle"]
print(cast)
print(len(cast))
print(cast[1])
cast.append("gilliam")
print(cast)
cast.pop()
print(cast)
cast.extend(["gilliam","chapman"])
print(cast)
cast.extend("bark")
cast.append(["soft","english"])
cast.remove("chapman")
cast.insert(0,"chapman")

movies = ["The Holy Grail","The Life Of Brain","The Meaning of Life"]
print(movies[1])
movies.insert(1,1975)
movies.insert(3,1979)
movies.insert(5,1983)
print(movies)

fav_movies = ["The Holy Grail","The Life Of Brain"]
print(fav_movies[0])
print(fav_movies[1])

for each_flick in fav_movies:
    print(each_flick)
