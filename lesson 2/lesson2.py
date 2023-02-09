"""
План:
1.	Що таке Python ?
2.	Середовище програмування
3.  GIT
4.  Функція print


Наш код працює за допомогою КОМПІЛЯТОРА.
- Комплілятор - читає відразу весь код

Також ще є - Інтерпретатор - читає по 1 строчці

Коли ми пишемо код ми, то повинні дотримуватися - Синтаксису - набір правил для програмування
PEP-8 - набір рекомендацій для написання правильного коду


CTRL + ALT + L - комбінація клавіш для виправлення порушень PEP-8


Коментар - це участок коду який ігнорується Пайтоном. Це ваши замітки



GIT - система контролю версій - система для збереження ваших даних на віддаленому сервері
git - команда для GIT
репозиторій - папка яка зберігає дані
master/main - головна гілка репозиторію
гілка - окрема "папка" яка працює з копією файлів. В ній ви можете редагувати файли незалежно від основних.

git init - ініціює GIT та створює .git файл який зберігає всю інформацію про ваші репозиторії/файли/гілки
git remote - список репозиторіїв
git remote add <назва_репозиторію> <шлях> - додати репозиторій до поточного проєкту
git status - поточний статус ваших файлів
git add - додати файл/папку/все до відслідковування
git commit -m "коментар" - зберігти ваші змінені файли в поточну гілку
git push <назва_репозиторію> <гілка> - залити ваші зміни в гілці до репозиторію


print - функція для виводу даних в "поток виводу даних"
Є 3 основні потоки:
1. виводу даних stdout
2. ввод даних strin
3. вивід помилок strerr
Приймає безліч параметрів через кому - всі ці дані виведе на екран.
Також приймає основні іменовані параметри:
- sep - говорить функції який роздільник використовувати. За замовчуванням це символ пробілу
- end - вставляє вказаний текст в кінець виведеного тексту. За замовчуванням це \n - символ переходу на нову строку


help - читати документацію

Змінна - ім'я яке зберігає якусь інформацію
"""
