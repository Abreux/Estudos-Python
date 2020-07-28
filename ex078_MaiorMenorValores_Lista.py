# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
valores = []
maior = menor = 0

for p in range(0, 5):
    valores.append(int(input(f'Digite um valor na posição {p + 1}: ')))
print(valores)

if p == 0:
    menor = maior = valores[0]
else:
    if valores[p] < menor:
        menor = valores[p]
    if valores[p] > maior:
        maior = valores[p]

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')




