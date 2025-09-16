# tags: args, *args, funcao args, *kwargs, kwargs, **kwargs

'''
    Se utiliza quando não sabemos quantos argumentos vamos a dar a uma determinada função
    Os agumentos são passados como uma tupla.

    se utuliza * para poder usart esse tipo de função

    **kwargs - Uso de dicionarios
'''

#####   *ARGS

def soma (*sum):
    soma_total = int(0)
    for i in sum:
        soma_total = soma_total + i
    return soma_total

user_numbers = [] # Essa lista será transformada em tupla posteriormente.

user_quest = int(input("Me escreva um número para somar:\n"))
user_numbers.append(user_quest)

while True:
    user_request = int(input("Digite outro número:\n"))
    user_numbers.append(user_request)
    user_continue = input("Deseja continuar? [Sim/Não]\n").lower()
    if user_continue == "sim":
        True
    else:
        break
user_numbers = tuple(user_numbers)
soma_total = soma(*user_numbers)

print(f"A soma de seus números é {soma_total}")

#### **KWARGS

def presentation (**data):
    for key, value in data.items():
        print(f"{key} - {value}")
print("Lista de cursos:")
presentation(name = "Python", category = "Backend", dificultad = "Iniciante")
presentation(name = "Visão computacional", category = "IA", dificultad = "Avançado")
presentation(name = "Dashboards com Dash", category = "Data Science", dificultad = "Itermediario")
