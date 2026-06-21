def juego():
    inicial = int(input('Ingrese la posicion inicial: '))
    final = int(input('Ingrese la posicion final: '))
    if movimiento(inicial, final):
        print('\n', varillas[0], '\n', varillas[1], '\n', varillas[2])
    else:
        print('Movimiento invalido')

def movimiento(inicial, final):
    if varillas[inicial] and (not varillas[final] or varillas[inicial][-1] < varillas[final][-1]):
        varillas[final].append(varillas[inicial].pop())
        return True
    else:
        return False

def automatico(n, inicial, final):
    if n != varillas[inicial][-1]:
        automatico(n - 1, inicial, 3 - inicial - final)

    movimiento(inicial, final)
    print('\n', varillas[0], '\n', varillas[1], '\n', varillas[2])

    if n != 1:
        automatico(n - 1, 3 - inicial - final, final)


# desarrollo 

modo = input('jugar 1, automatico 2: ')
altura = int(input('Ingrese la altura de la torre: '))
varillas = [list(range(altura, 0, -1)), [], []]
print('\n', varillas[0], '\n', varillas[1], '\n', varillas[2])

while modo == '1':
    juego()

if modo == '2':
    automatico(altura, 0, 2)
