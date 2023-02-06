##Пользователь вводит число K - количество фруктов. Затем он вводит K фруктов в формате:
#название фрукта и его количество. Добавьте все фрукты в словарь, где название фрукта - это ключ,
#а количество - значение.
import random

N = int(input("Введите количество видов фруктов"))
fru_dict = []
frutes = []
quantity = []

for i in range(N):
    fru = str(input('Введите название фрукта'))
    qua = input('Введите количество фруктов')
    frutes.append(fru)
    quantity.append(qua)
fru_dict.append(dict(zip(frutes, quantity)))
print(fru_dict)

#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
#Создайте список friends и добавьте в него N словарей с ключами name и age.
#Найдите самого младшего из друзей и выведите его имя.

N = int(input("Введите количество друзей"))
friends = []
name = []
age = []

for i in range(N):
    n = input('Введите имя')
    a = input('Введите возраст')
    name.append(n)
    age.append(a)
    new_friends = dict(name=n, age=a)
    friends.append(new_friends)
print(friends)

for i in friends:
    for j in i.values():
        minn = min(age)
print(minn)

for some_dict in friends:
    if some_dict['age'] == minn:
        print(some_dict['name'])
        break

#Пользователь вводит число N. Затем он вводит личные данные (имя и возраст) своих N друзей.
# Создайте список friends и добавьте в него N словарей с ключами name и age.
#Выведите средний возраст всех друзей и самое длинное имя.

N = int(input("Введите количество друзей"))
for i in range(N):
    n = input('Введите имя')
    a = input('Введите возраст')
    name.append(n)
    age.append(a)
    new_friends = dict(name=n, age=a)
    friends.append(new_friends)
print(friends)
avarage_age = 0
max_name = friends[0]['name']
for some_dict in friends:
    avarage_age += int(some_dict['age'])
    if len(some_dict['name']) > len(max_name):
        max_name = some_dict['name']
avarage_age = avarage_age/N
print(avarage_age)
print(max_name)

## Программа получает на вход слово на английском языке и несколько его переводов на русском языке.
## Составьте словарь, в котором ключ - это английское слово, а значение - это список русских слов.

count = int(input())
translate_dict = {}
for _ in range(count):
    eng_rus_str = input()
    some_list = eng_rus_str.split(' - ')
    translate_dict[some_list[0]] = some_list[1].split(', ')
print(translate_dict)

## Создайте список из случайных чисел. Найдите количество различных элементов в нем.

import random

list = [random.randint(1, 10) for _ in range(10)]
some_set = set(list)
print(len(some_set))