import time

counter = 0

while True:
    num = int(input("Digite um número:\n"))

    print("Analizando...")
    time.sleep(1.5)

    print(num,"é impar" if num & 1 else "é par")

    continuar = input("Deseja continuar? [S/N]\n") .upper() .strip()
    
    counter += 1

    if counter == 5:
        print("Limite excedido")
        break

    if continuar != "S":
        break

print(counter)