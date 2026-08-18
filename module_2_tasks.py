УРОК 19: ОСНОВЫ КЛАССОВ
Задание 1: Класс Student
python
# Создай класс "Student" (Студент):
# 1. В __init__ принимает name и age
# 2. Сохраняет их в атрибуты
# 3. Создай метод introduce(), который выводит:
#    "Меня зовут {name}, мне {age} лет"

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет"


student1 = Student("Petrov", 20)
student2 = Student("Ivanov", 22)

print(student1.introduce())
print(student2.introduce())
Задание 2: Класс Book
python
# Создай класс "Book" (Книга):
# 1. В __init__ принимает title, author, pages
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Автор: {author}, Страниц: {pages}"

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"


book1 = Book("Tetler", "Top", 69)
book2 = Book("Spartak", "Champion", 4444)

print(book1.info())
print(book2.info())
Задание 3: Класс Car
python
# Создай класс "Car" (Машина):
# 1. В __init__ принимает brand, model, year
# 2. Сохраняет их в атрибуты
# 3. Создай метод start_engine(), который выводит "Двигатель запущен!"
# 4. Создай метод stop_engine(), который выводит "Двигатель остановлен"
# 5. Создай метод info(), который возвращает:
#    "Марка: {brand}, Модель: {model}, Год: {year}"

class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start_engine(self):
        print("Двигатель запущен!")

    def stop_engine(self):
        print("Двигатель остановлен")

    def info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}"


car1 = Car("Bobo", "Tutu", 1987)
car2 = Car("Ewe", "fipo", 1876)

car1.start_engine()
car2.start_engine()
print(car1.info())
print(car2.info())
Задание 4: Класс User
python
# Создай класс "User" (Пользователь):
# 1. В __init__ принимает username и email
# 2. Сохраняет их в атрибуты
# 3. Создай метод login(), который выводит:
#    "Пользователь {username} вошёл в систему"
# 4. Создай метод logout(), который выводит:
#    "Пользователь {username} вышел из системы"

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        return f"Пользователь {self.username} вошёл в систему"

    def logout(self):
        return f"Пользователь {self.username} вышел из системы"


user1 = User("Tetler", "lfgj@ksf.ru")
user2 = User("eteg", "httu@fgg.ru")

print(user1.login())
print(user1.logout())
print(user2.login())
print(user2.logout())
Задание 5: Класс Product
python
# Создай класс "Product" (Товар):
# 1. В __init__ принимает name, price, quantity
# 2. Сохраняет их в атрибуты
# 3. Создай метод total_cost(), который возвращает общую стоимость (price * quantity)
# 4. Создай метод sell(amount), который:
#    - уменьшает quantity на amount
#    - если amount больше quantity, выводит "Недостаточно товара"

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self):
        return self.price * self.quantity

    def sell(self, amount):
        if amount <= self.quantity:
            self.quantity = self.quantity - amount
        else:
            print("Недостаточно товара")

    def info(self):
        return f"Товар: {self.name}, Цена: {self.price}, Количество: {self.quantity}"


product = Product("Apple", 534, 32)

print(product.total_cost())
product.sell(2)
print(product.info())
Задание 6: Класс BankAccount
python
# Создай класс "BankAccount" (Банковский счёт):
# 1. В __init__ принимает owner и balance
# 2. Сохраняет их в атрибуты
# 3. Создай метод deposit(amount), который увеличивает balance на amount
# 4. Создай метод withdraw(amount), который:
#    - уменьшает balance на amount
#    - если amount больше balance, выводит "Недостаточно средств"
# 5. Создай метод info(), который возвращает:
#    "Владелец: {owner}, Баланс: {balance}"

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Недостаточно средств")

    def info(self):
        return f"Владелец: {self.owner}, Баланс: {self.balance}"


bankAccount = BankAccount("Tetler", 1800000)

bankAccount.deposit(300000)
bankAccount.withdraw(100000)
print(bankAccount.info())
Задание 7: Класс Library
python
# Создай класс "Library" (Библиотека):
# 1. В __init__ принимает name (название библиотеки)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут books = [] (пустой список книг)
# 4. Создай метод add_book(book), который добавляет книгу в список books
# 5. Создай метод show_books(), который выводит все книги в библиотеке

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def show_books(self):
        return f"{self.books}"


library = Library("Библиотека")

library.add_book("Tdgd")
library.add_book("fdhrtfjfg")
library.add_book("iiiiiiiigggg")

print(library.show_books())
Задание 8: Класс Playlist
python
# Создай класс "Playlist" (Плейлист):
# 1. В __init__ принимает name (название плейлиста)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут songs = [] (пустой список песен)
# 4. Создай метод add_song(song), который добавляет песню в список songs
# 5. Создай метод show_songs(), который возвращает список всех песен

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def show_songs(self):
        return f"{self.songs}"


playlist = Playlist("Music")

playlist.add_song("gg")
playlist.add_song("w35wt")
playlist.add_song("ert43yrh")

print(playlist.show_songs())
Задание 9: Класс Student (с улучшением оценки)
python
# Создай класс "Student" (Студент):
# 1. В __init__ принимает name и grade (оценка)
# 2. Сохраняет их в атрибуты
# 3. Создай метод improve(amount), который увеличивает grade на amount (максимум 100)
# 4. Создай метод info(), который возвращает:
#    "Студент: {name}, Оценка: {grade}"

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def improve(self, amount):
        if self.grade + amount <= 100:
            self.grade = self.grade + amount
        else:
            print("Оценка не может быть выше 100")

    def info(self):
        return f"Студент: {self.name}, Оценка: {self.grade}"


student = Student("Tetler", 35)

student.improve(12)
student.improve(21)
print(student.info())
Задание 10: Класс Counter
python
# Создай класс "Counter" (Счётчик):
# 1. В __init__ принимает start (начальное значение)
# 2. Сохраняет его в атрибут value
# 3. Создай метод increment(), который увеличивает value на 1
# 4. Создай метод decrement(), который уменьшает value на 1
# 5. Создай метод reset(), который устанавливает value в 0
# 6. Создай метод current(), который возвращает текущее значение

class Counter:
    def __init__(self, start):
        self.value = start

    def increment(self):
        self.value = self.value + 1

    def decrement(self):
        self.value = self.value - 1

    def reset(self):
        self.value = 0

    def current(self):
        return self.value


counter = Counter(10)

print(counter.current())
counter.increment()
counter.increment()
counter.increment()
counter.decrement()
print(counter.current())
counter.reset()
print(counter.current())
Задание 11: Класс Temperature
python
# Создай класс "Temperature" (Температура):
# 1. В __init__ принимает celsius (температура в градусах Цельсия)
# 2. Сохраняет его в атрибут celsius
# 3. Создай метод to_fahrenheit(), который возвращает температуру в Фаренгейтах
#    Формула: fahrenheit = celsius * 9/5 + 32
# 4. Создай метод to_kelvin(), который возвращает температуру в Кельвинах
#    Формула: kelvin = celsius + 273.15
# 5. Создай метод set_celsius(value), который изменяет celsius на value

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return self.celsius * 9/5 + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def set_celsius(self, value):
        self.celsius = value


temperature = Temperature(41)

print(f"По Цельсию: {temperature.celsius}")
print(f"По Фаренгейту: {temperature.to_fahrenheit()}")
print(f"По Кельвину: {temperature.to_kelvin()}")

temperature.set_celsius(5)

print(f"По Цельсию после изменения: {temperature.celsius}")
print(f"По Фаренгейту: {temperature.to_fahrenheit()}")
print(f"По Кельвину: {temperature.to_kelvin()}")
Задание 12: Класс Rectangle
python
# Создай класс "Rectangle" (Прямоугольник):
# 1. В __init__ принимает width и height
# 2. Сохраняет их в атрибуты
# 3. Создай метод area(), который возвращает площадь (width * height)
# 4. Создай метод perimeter(), который возвращает периметр (2 * (width + height))
# 5. Создай метод is_square(), который возвращает True, если ширина равна высоте

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def set_size(self, width, height):
        self.width = width
        self.height = height


rectangle = Rectangle(34, 56)

print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.is_square())

rectangle.set_size(44, 65)

print(rectangle.area())
print(rectangle.perimeter())
print(rectangle.is_square())
Задание 13: Класс Circle
python
# Создай класс "Circle" (Круг):
# 1. В __init__ принимает radius
# 2. Сохраняет его в атрибут
# 3. Создай метод area(), который возвращает площадь круга (3.14 * radius²)
# 4. Создай метод circumference(), который возвращает длину окружности (2 * 3.14 * radius)
# 5. Создай метод set_radius(value), который изменяет радиус

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * 3.14

    def circumference(self):
        return 2 * 3.14 * self.radius

    def set_radius(self, value):
        self.radius = value


circle = Circle(300)

circle.set_radius(400)
print(circle.area())
print(circle.circumference())
Задание 14: Класс Book (с is_long)
python
# Создай класс "Book" (Книга):
# 1. В __init__ принимает title, author, pages
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Автор: {author}, Страниц: {pages}"
# 4. Создай метод is_long(), который возвращает True, если страниц больше 300
# 5. Создай метод set_pages(value), который изменяет количество страниц

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"Название: {self.title}, Автор: {self.author}, Страниц: {self.pages}"

    def is_long(self):
        return self.pages > 300

    def set_pages(self, value):
        self.pages = value


book = Book("Poh", "Zah", 248)

book.set_pages(312)
print(book.info())
Задание 15: Класс Song
python
# Создай класс "Song" (Песня):
# 1. В __init__ принимает title, artist, duration (в секундах)
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Исполнитель: {artist}, Длительность: {duration} сек"
# 4. Создай метод is_long(), который возвращает True, если длительность больше 240 секунд
# 5. Создай метод set_duration(value), который изменяет длительность

class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def info(self):
        return f"Название: {self.title}, Исполнитель: {self.artist}, Длительность: {self.duration} сек"

    def is_long(self):
        return self.duration > 240

    def set_duration(self, value):
        self.duration = value


song = Song("Puzo", "Bobr", 223)

song.set_duration(156)
print(song.info())
Задание 16: Класс TV
python
# Создай класс "TV" (Телевизор):
# 1. В __init__ принимает brand и channel (по умолчанию 1)
# 2. Сохраняет их в атрибуты
# 3. Создай метод turn_on(), который выводит "Телевизор включён"
# 4. Создай метод turn_off(), который выводит "Телевизор выключен"
# 5. Создай метод change_channel(new_channel), который изменяет канал
#    Если new_channel от 1 до 100 — меняет канал
#    Если нет — выводит "Канал не существует"

class TV:
    def __init__(self, brand, channel=1):
        self.brand = brand
        self.channel = channel

    def turn_on(self):
        return "Телевизор включён"

    def turn_off(self):
        return "Телевизор выключен"

    def change_channel(self, new_channel):
        if new_channel >= 1 and new_channel <= 100:
            self.channel = new_channel
        else:
            print("Канал не существует")

    def info(self):
        return f"Телевизор: {self.brand}, Канал: {self.channel}"


tv = TV("Tetler", 33)

print(tv.turn_on())
tv.change_channel(44)
print(tv.info())

tv.change_channel(150)
print(tv.info())
Задание 17: Класс BankAccount (повтор)
python
# Создай класс "BankAccount" (Банковский счёт):
# 1. В __init__ принимает owner и balance (по умолчанию 0)
# 2. Сохраняет их в атрибуты
# 3. Создай метод deposit(amount), который увеличивает balance на amount
# 4. Создай метод withdraw(amount), который:
#    - уменьшает balance на amount
#    - если amount больше balance, выводит "Недостаточно средств"
# 5. Создай метод show_balance(), который возвращает текущий баланс

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("Недостаточно средств")
        else:
            self.balance = self.balance - amount

    def show_balance(self):
        return self.balance


bankAccount = BankAccount("Tetler", 1500000)

bankAccount.deposit(300000)
bankAccount.withdraw(150000)
print(bankAccount.show_balance())
Задание 18: Класс Student (с add_grade и remove_grade)
python
# Создай класс "Student" (Студент):
# 1. В __init__ принимает name, grade (по умолчанию 0)
# 2. Сохраняет их в атрибуты
# 3. Создай метод add_grade(amount), который увеличивает grade на amount (максимум 100)
# 4. Создай метод remove_grade(amount), который уменьшает grade на amount (минимум 0)
# 5. Создай метод info(), который возвращает:
#    "Студент: {name}, Оценка: {grade}"

class Student:
    def __init__(self, name, grade=0):
        self.name = name
        self.grade = grade

    def add_grade(self, amount):
        if self.grade + amount <= 100:
            self.grade = self.grade + amount
        else:
            print("Оценка не может быть выше 100")

    def remove_grade(self, amount):
        if self.grade - amount >= 0:
            self.grade = self.grade - amount
        else:
            print("Оценка не может быть ниже 0")

    def info(self):
        return f"Студент: {self.name}, Оценка: {self.grade}"


student = Student("Tetler", 55)

student.add_grade(18)
student.remove_grade(5)
print(student.info())
Задание 19: Класс Laptop
python
# Создай класс "Laptop" (Ноутбук):
# 1. В __init__ принимает brand, model, battery (заряд батареи в %, по умолчанию 100)
# 2. Сохраняет их в атрибуты
# 3. Создай метод use(amount), который уменьшает battery на amount (минимум 0)
# 4. Создай метод charge(amount), который увеличивает battery на amount (максимум 100)
# 5. Создай метод info(), который возвращает:
#    "Ноутбук: {brand} {model}, Заряд: {battery}%"

class Laptop:
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery

    def use(self, amount):
        if self.battery - amount >= 0:
            self.battery = self.battery - amount
        else:
            print("Заряд батареи не может быть меньше 0")

    def charge(self, amount):
        if self.battery + amount <= 100:
            self.battery = self.battery + amount
        else:
            print("Заряд батареи не может быть больше 100")

    def info(self):
        return f"Ноутбук: {self.brand} {self.model}, Заряд: {self.battery}%"


laptop = Laptop("Omen", "rx210", 75)

laptop.use(40)
laptop.charge(35)
print(laptop.info())
Задание 20: Класс BookShelf
python
# Создай класс "BookShelf" (Книжная полка):
# 1. В __init__ принимает name (название полки)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут books = [] (пустой список книг)
# 4. Создай метод add_book(book), который добавляет книгу в список
# 5. Создай метод remove_book(book), который удаляет книгу из списка
# 6. Создай метод show_books(), который возвращает список книг

class BookShelf:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def show_books(self):
        return self.books


bookShelf = BookShelf("Polka")

bookShelf.add_book("Lena")
bookShelf.add_book("Pizena")
bookShelf.add_book("Sisi")
bookShelf.remove_book("Pizena")

print(bookShelf.show_books())
Задание 21: Класс ToDoList
python
# Создай класс "ToDoList" (Список задач):
# 1. В __init__ создай атрибут tasks = [] (пустой список)
# 2. Создай метод add_task(task), который добавляет задачу в список
# 3. Создай метод remove_task(task), который удаляет задачу из списка
# 4. Создай метод show_tasks(), который возвращает список задач
# 5. Создай метод mark_done(task), который удаляет задачу (как выполненную)

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def show_tasks(self):
        return self.tasks

    def mark_done(self, task):
        self.tasks.remove(task)


toDoList = ToDoList()

toDoList.add_task("gf")
toDoList.add_task("fgg")
toDoList.add_task("rfj")
toDoList.remove_task("fgg")

print(toDoList.show_tasks())
Задание 22: Класс Calculator
python
# Создай класс "Calculator" (Калькулятор):
# 1. В __init__ создай атрибут history = [] (история вычислений)
# 2. Создай метод add(a, b), который возвращает a + b и добавляет запись в историю
# 3. Создай метод subtract(a, b), который возвращает a - b и добавляет запись в историю
# 4. Создай метод multiply(a, b), который возвращает a * b и добавляет запись в историю
# 5. Создай метод divide(a, b), который возвращает a / b и добавляет запись в историю
# 6. Создай метод show_history(), который возвращает историю вычислений

class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append(f"{a} - {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

    def divide(self, a, b):
        result = a / b
        self.history.append(f"{a} / {b} = {result}")
        return result

    def show_history(self):
        return self.history


calculator = Calculator()

calculator.add(9, 5)
calculator.subtract(5, 7)
calculator.multiply(5, 3)
calculator.divide(2, 2)

print(calculator.show_history())
Задание 23: Класс TemperatureTracker
python
# Создай класс "TemperatureTracker" (Трекер температуры):
# 1. В __init__ создай атрибут readings = [] (список показаний)
# 2. Создай метод add_reading(temp), который добавляет температуру в список
# 3. Создай метод get_average(), который возвращает среднюю температуру
# 4. Создай метод get_max(), который возвращает максимальную температуру
# 5. Создай метод get_min(), который возвращает минимальную температуру
# 6. Создай метод show_readings(), который возвращает список всех показаний

class TemperatureTracker:
    def __init__(self):
        self.readings = []

    def add_reading(self, temp):
        self.readings.append(temp)

    def get_average(self):
        if len(self.readings) == 0:
            return 0
        return sum(self.readings) / len(self.readings)

    def get_max(self):
        if len(self.readings) == 0:
            return None
        return max(self.readings)

    def get_min(self):
        if len(self.readings) == 0:
            return None
        return min(self.readings)

    def show_readings(self):
        return self.readings


tracker = TemperatureTracker()

tracker.add_reading(10)
tracker.add_reading(20)
tracker.add_reading(30)
tracker.add_reading(40)
tracker.add_reading(50)

print(tracker.show_readings())
print(tracker.get_average())
print(tracker.get_max())
print(tracker.get_min())
Задание 24: Класс ScoreTracker
python
# Создай класс "ScoreTracker" (Трекер очков):
# 1. В __init__ создай атрибут scores = [] (пустой список)
# 2. Создай метод add_score(score), который добавляет очки в список
# 3. Создай метод get_average(), который возвращает средний балл (или 0, если список пустой)
# 4. Создай метод get_max(), который возвращает максимальный балл (или None, если список пустой)
# 5. Создай метод get_min(), который возвращает минимальный балл (или None, если список пустой)
# 6. Создай метод show_scores(), который возвращает список всех очков

class ScoreTracker:
    def __init__(self):
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_average(self):
        if len(self.scores) == 0:
            return 0
        return sum(self.scores) / len(self.scores)

    def get_max(self):
        if len(self.scores) == 0:
            return None
        return max(self.scores)

    def get_min(self):
        if len(self.scores) == 0:
            return None
        return min(self.scores)

    def show_scores(self):
        return self.scores


scoreTracker = ScoreTracker()
scoreTracker.add_score(43)
scoreTracker.add_score(23)
scoreTracker.add_score(67)
scoreTracker.add_score(87)

print(scoreTracker.get_average())
print(scoreTracker.get_max())
print(scoreTracker.get_min())
print(scoreTracker.show_scores())
Задание 25: Класс ShoppingCart
python
# Создай класс "ShoppingCart" (Корзина покупок):
# 1. В __init__ создай атрибут items = [] (список товаров)
# 2. Создай метод add_item(item, price), который добавляет товар и его цену в корзину
# 3. Создай метод get_total(), который возвращает общую стоимость всех товаров
# 4. Создай метод show_items(), который возвращает список товаров

class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        self.items.append({"name": item, "price": price})

    def get_total(self):
        total = 0
        for item in self.items:
            total = total + item["price"]
        return total

    def show_items(self):
        return self.items


shoppingCart = ShoppingCart()

shoppingCart.add_item("fdg", 44)
shoppingCart.add_item("fdggg", 66)
shoppingCart.add_item("dyfegf", 778)

print(shoppingCart.show_items())
print(shoppingCart.get_total())
Задание 26: Класс StudentGroup
python
# Создай класс "StudentGroup" (Группа студентов):
# 1. В __init__ принимает group_name (название группы)
# 2. Сохраняет group_name в атрибут
# 3. Создай атрибут students = [] (список студентов)
# 4. Создай метод add_student(name, grade), который добавляет студента в виде словаря:
#    {"name": name, "grade": grade}
# 5. Создай метод get_average_grade(), который возвращает среднюю оценку по группе
# 6. Создай метод show_students(), который возвращает список студентов

class StudentGroup:
    def __init__(self, group_name):
        self.group_name = group_name
        self.students = []

    def add_student(self, name, grade):
        self.students.append({"name": name, "grade": grade})

    def get_average_grade(self):
        if len(self.students) == 0:
            return 0
        total = 0
        for student in self.students:
            total = total + student["grade"]
        return total / len(self.students)

    def show_students(self):
        return self.students


studentGroup = StudentGroup("Группа Python")

studentGroup.add_student("zzzz", 44)
studentGroup.add_student("cccc", 55)
studentGroup.add_student("bbbb", 88)

print(studentGroup.show_students())
print(studentGroup.get_average_grade())
Задание 27: Класс Library (с удалением)
python
# Создай класс "Library" (Библиотека):
# 1. В __init__ принимает name (название библиотеки)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут books = [] (список книг)
# 4. Создай метод add_book(title, author), который добавляет книгу в виде словаря:
#    {"title": title, "author": author}
# 5. Создай метод remove_book(title), который удаляет книгу по названию
# 6. Создай метод show_books(), который возвращает список книг

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, title, author):
        self.books.append({"title": title, "author": author})

    def remove_book(self, title):
        for book in self.books:
            if book["title"] == title:
                self.books.remove(book)
                break

    def show_books(self):
        return self.books


library = Library("Библиотека")

library.add_book("sdgsgs", "tyr")
library.add_book("hgfjhkjl", "hggjg")
library.add_book("iiiiii", "er")

library.remove_book("hgfjhkjl")

print(library.show_books())
