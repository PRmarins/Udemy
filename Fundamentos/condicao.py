# tags: lista, condicional

# innformações sobre o filme

dict_filme = {}

while True:

    nameMovie = input("Digite o nome do filme:\n")
    yearRelease = int(input("Digite o ano de laçamento:\n"))
    ranting = float(input("Digite a nota para esse filme:\n"))
    
    dict_filme[nameMovie] = yearRelease,ranting
    
    continuar = input("Deseja continuar?\n") .strip() .upper()
    if continuar != "S":
        break

filmesQuantidade = (len(dict_filme))

verListaDeFilme = input("Deseja ver a lista de filmes?\n") .lower() .strip()

if verListaDeFilme == "s":
    for chaves in dict_filme.keys():
        print(chaves)
    
# Verificar se o filme é recomendavel

filme_user = input("Qual filme gostaria de assistir?\n")

filme_recomendation = input("Gostaria de saber se esse filme filme é recomendavel? [S/N]\n") .lower() .strip()

filme_Rating_user = dict_filme[filme_user][1]

if filme_Rating_user >= 7:
    print("Esse filme é recomendavel.")