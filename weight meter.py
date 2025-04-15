lista = []
pessoas = []
maior = menor = 0
while True:
    lista.append(str(input('nome: ')))
    lista.append(int(input('peso: ')))
    if len(pessoas) == 0:
        maior = menor = lista[1]
    else:
        if lista[1] > maior:
            maior = lista[1]
        if lista[1] < menor:
            menor = lista[1]
    pessoas.append(lista[:])
    lista.clear()
    c = str(input('deseja continuar? [S/N] '))

    if c in 'Nn':
        break


print(f'foram cadastrados {len(pessoas)} pessoas até o momento')
print(f'o maior peso registrado foi {maior}. peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'{i[0]}...',end='')
print()
print(f'o menor peso registrado foi {menor}. peso de ',end='')
for i in pessoas:
    if i[1] == menor:
        print(f'{i[0]}...',end='')
