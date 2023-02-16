# Цикл - дія  яка повторюється за певною умовою

# 1. for
# 2. while

# while - цикл працює поки умова правдива (True)
# зациклення - цикл працює бескінечно
# while True - вічний цикл

# break - достроково завершує роботу циклу
# continue - достроково переходить на початок циклу

# Тіло циклу - код який знах. в циклі
# Ітерація - 1 прохід по тілу циклу
"""
n = 10

while True:
    x = input('Введіть X:')

    if x == 'X':
        break

x = input('Введіть X:')
# x = 3
# 3 != X - False - X = X - X != X - True - end
while x != 'X':
    x = input('Введіть X:')

"""

# 3 спроби. > 10
password = input('Enter password')
count = 1

while len(password) < 10 and count < 3:
    password = input('Enter password')

    if len(password) == 5:
        continue

    count += 1  # Інкремент - збільшення змінної

    assert count < 3

else:
    print('Все ок')
