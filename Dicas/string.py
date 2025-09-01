frase = ('curso em video python')
print(frase[1:15:2])
#vai comecar a frase no primeiro caractere e seguir até o 15 e pulando de 2 em 2
print(frase[::-1])
#Escreve a frase ao inverso
print(frase.count('o',0,13))
#contar na frase quantos O tem entre o caracter 0 e o 13
print(frase.find('deo'))
#diz a partir de que caracter encontrou 'deo' na frase
print('curso'in frase)
#respode se tem ou nao 'curso'dentro da frase
print(frase.replace('python','Android'))
#substituir o python por android na frase
print(frase.upper())
#poem tudo por maiusculo
print(frase.lower())
#poem tudo em minusculo
print(frase.capitalize())
#vai por somente a primeira letra em maiusculo e todas as outras em minusculo
print(frase.title())
#poem toda primeira letra de uma palavra em maiuscula
print(frase.strip())
#remove os espaços vazios antes e depois da frase
print(frase.rstrip())
#remove os espaços vazios somente depois da frase
print(frase.lstrip())
#remove os espaços antes da frase
print(frase.split())
#Divide cada palavra em uma cadeia de caracteres nesse caso 0 seria curso,1 seria em,2 seria video e 4 seria python
print(''.join(frase))
#faz o proceso inverso do anterior
print(len(frase))
#retorna o numero de caracteres de uma string
print("""asasdoidjfsajdfqwe
asdasdasipkjasdf
sadfasdgsaera""")
#aspas triplas fazem tudo que esta entre elas ser escrito, mesmo que esteja em linhas distintas.