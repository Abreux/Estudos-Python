# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

valores = []
men = mai = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {cont + 1}: ')))
    if cont == 0:
        men = mai = valores[cont]
    else:
        if valores[cont] < men:
            men = valores[cont]
        if valores[cont] > mai:
            mai = valores[cont]
print('\033[2;32m_._\033[m' *22)
print(f'Números digitados: \n',valores)
print('\033[2;32m_._\033[m' *22)
print(f'O menor número digitado foi {men}, na posição: \n', end='')
for p, v in enumerate(valores):
    if v == men:
        print(f'{p + 1}...', end='')
        print()
print('\033[2;32m_._\033[m' *22)
print(f'O maior número digitado foi {mai}, na posição: \n', end='')
for p, v in enumerate(valores):
    if v == mai:
        print(f'{p + 1}...', end='')
        print()
