import math
print('\nDesafio 18 - Cálculos Trigonométricos.\n')
a = float(input('\nQual ângulo deseja usar?'))
sen = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('\nO ângulo de {}\ntem o seno de {:.2f}\no cosseno de {:.2f}\ne a tangente de {:.2f}!'. format(a, sen, cos, tan))