a, b, c = int(input()), int(input()), int(input())
exp1 = (a**2 + b**2)/(3*b - 4)
exp2 = (4 * c**5) / 6
integer = exp1 // exp2
remainder = exp1 % exp2
print(f'Целая часть: {integer}', f'Остаток от деления: {remainder}', end='\n')
