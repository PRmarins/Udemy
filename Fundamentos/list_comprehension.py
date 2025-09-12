# tags: list, list_comprehension 

lista_filmes = ["Onde os fracos não tem vez", "Procurando o Nemo", "Interstella", "The whale", "Sherek"]

movies_with_a = [movies for movies in lista_filmes if "A" in movies.upper()]

print(movies_with_a)