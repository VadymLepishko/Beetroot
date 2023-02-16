"""
ДЗ:
1)
x = '100.9'
int(x) - error
float(x) - 100.9
str(x) - '100.9'

2) CTRL + ALT + L
print(c) - НІ
print(c) - ТАК

print(a-b) - НІ
print(a - b) - ТАК

b=9 - НІ
a = 9 - ТАК


Питання:
1) “hello world”.count(' ') - 1
2) '1234567'.find('123') -
3) 'example'.lower().upper().lower()
4) 'beetroot'.count().upper()
5) str(123).count('1')


- Збирач сміття (garbage collector) -


План:
1) Тип даних - None
2) Логічний тип даних - bool
3) Умовні конструкції  if-else  if-elif-else
4) Логічні оператори  and or not
4) Оператори членства   in   not in
5) Оператори тотожності  is   is not
6) Вкладені умовні конструкції
7) Тернарний оператор
8) assert
9) Цикл while
"""

# 1. None (NoneType) - потрібен для розуміння чи є результат
x = None

# 2. bool (boolean) - логічний тип даних
# bool()
# int -> 0 - False - остальні - True
# float -> 0.0 - False  - осальні - True
# str -> пуста строка - False - не пуста - True
# None ->
x = True
y = False
# == - дорівнює
# != - не дорівнює
# > < >= <=


# and - логічне І
# True and True -> True
# True and False -> False
# False and True -> False
# False and False -> False
if x == 10 and y == 10:
    print('ok')
else:
    print('not ok')

# or - логічне або
# True and True -> True
# True and False -> True
# False and True -> True
# False and False -> False


# not - логічне НІ
# not True - False
# not False - True

# Явне перетворення типу даних - коли ми перетворюємо
# Не явне перетворення типу даних - коли Python сам міняє тип

#  pass - пустий блок коду
# ЗАБОРОНЕНО 4 пробіли і TAB одночасно

name = 'вааавп'
if name:
    # Блок True
    pass
    # Кінець блоку True
else:
    # Блок False
    print('Помилка')
    # Кінець блок False

if not name:
    # Блок False
    print('Помилка')
    # Кінець блок False

# В випадку якщо потрібно створити зміну "or" або "and"
or_ = 10
and_ = 1434

# in - шукає чи є елемент в послідовності
x = 'hello'
y = 'o' in x  # True
k = 'o' not in x  # False

# is - перевіряє чи однакові об'єкти
# id(значення) - адреса PyObject`у
x = 10
y1 = 10
print(x is None)  # True

# 2 + 2 - 4 = None
example = None
# 0 != None
if example is None:
    print('Сталася помилка!')

# Для перевірки чи це None
# Використовуйте is None / is not None
# if example == None: - НІ
# if example is None: - ТАК
if example == None:
    print('Сталася помилка!')

# input() - відповідає за поток stdin (поток вводу даних)
# input() -> str
x = int(input('Введіть ваше ім\'я :'))
print(x + 10)

# Тернарний оператор - скорочення умовної конструкції

#   <дія_True> if <УМОВА> else <дія_False>
y = True if x == 10 else False

x = 10

if x == 10:
    y = True
else:
    y = False

# exit() - достроково завершує роботу програми
# assert -

username = 'Вася'

db_username = 'Вася1'

# if username == db_username:
#     print('Вхід')
# else:
#     print('hello')

# assert - перевіряє умову, і видає помилку якщо умова не вірна (False)
# AssertionError - ця помилка видається у випадку якщо умова assert видала False
# Якщо False - видати помилку AssertionError
# Якщо True - йде далі по коду

# n = sum(1, 2)
# n = 4
# assert n == 3, 'Ми очікували 3'

x = 1
y = 3
n = 4

count = 2

assert count == 3
