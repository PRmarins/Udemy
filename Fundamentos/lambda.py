# tags: lambda, funcao, função, funcao lambda, função lambda

#  São funcões rapidas e curtas

power = lambda num: num ** 2

dividir = lambda num: num/2

reverse = lambda word: word[::-1]

user_reguest = int(input("Escreva um número para saber seu quadrado:\n"))
print(f"O quadrado de {user_reguest} é {power(user_reguest)}")

user_reguest = int(input("Escreva um número para mostrar sua divisão por 2:\n"))
print(f"O numero {user_reguest} dividido por 2 é {dividir(user_reguest)}.")

user_reguest = input("Escreva uma palavra para mostrar-la ao contrario:\n")
print(f"A palavra {user_reguest} ao contrario fica:\n{reverse(user_reguest)}")