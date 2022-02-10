s1 = input('Введите строку 1: ')
s2 = input('Введите строку 2: ')

answer1 = bool(s1 == s2)
answer2 = bool(s1 in s2)
answer3 = bool(s2 in s1)

print(f'Вы ввели строку {s1} и {s2}')
print(f'Их длина соответственно {len(s1)} и {len(s2)}')
print(f'Первый символ первой строки: {s1[0]}')
print(f'Последний символ последней строки: {s2[-1]}')
print(f'{s1} равен {s2}? {answer1}')
print(f'{s1} содержится ли в {s2}? {answer2}')
print(f'А наоборот? {answer3}')
