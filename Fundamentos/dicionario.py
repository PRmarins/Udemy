import pprint

filmes = {
    "interstallar":{
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },

    "The Dark Knight":{
        "YerRealease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action","Crime"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmes)

print(filmes["The Dark Knight"]["genre"])