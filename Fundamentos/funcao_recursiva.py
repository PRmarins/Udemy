# tags: função recursiva, funcao recursiva, funcoes, funcao, funções, função

def fatorial (num):
    info = 1
    for numbers in range (1,num+1):
        info = info *numbers
    return info

# Observe que essa função é chamada e executada dentro dela mesma.

def funcao_recursiva (num):
    if num == 1:
        return 1
    else:
        return(num * funcao_recursiva(num-1))


user_number = int(input("Escreva um número para fatorar:\n"))

print(f"O Fatorial de {user_number} é: {fatorial(user_number)}")

print(f"O fatorial de {user_number} é: {funcao_recursiva(user_number)}")
