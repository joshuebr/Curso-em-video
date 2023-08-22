print('\ndesafio 83 - validando expressões numéricas!'.title())
exp = str(input('\ndigite a expressão: '.title()))
lista = []
for par in exp:
    if par == '(':
        lista.append('(')
    elif par == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('\nsua expressão está válida!'.upper())
else:
    print('\nsua expressão está errada!'.upper())

