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

Задание 28: Класс Playlist (с длительностью)
python
# Создай класс "Playlist" (Плейлист):
# 1. В __init__ принимает name (название плейлиста)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут songs = [] (список песен)
# 4. Создай метод add_song(title, artist, duration), который добавляет песню в виде словаря:
#    {"title": title, "artist": artist, "duration": duration}
# 5. Создай метод remove_song(title), который удаляет песню по названию
# 6. Создай метод get_total_duration(), который возвращает общую длительность плейлиста
# 7. Создай метод show_songs(), который возвращает список песен

class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, title, artist, duration):
        self.songs.append({"title": title, "artist": artist, "duration": duration})

    def remove_song(self, title):
        for song in self.songs:
            if song["title"] == title:
                self.songs.remove(song)
                break

    def get_total_duration(self):
        if len(self.songs) == 0:
            return 0
        total = 0
        for song in self.songs:
            total = total + song["duration"]
        return total

    def show_songs(self):
        return self.songs


playlist = Playlist("Musk")

playlist.add_song("tttt", "eeee", 78)
playlist.add_song("bbbb", "nnnnn", 44)
playlist.add_song("iiii", "ooooo", 66)

playlist.remove_song("iiii")

print(playlist.get_total_duration())
Задание 29: Класс ContactBook
python
# Создай класс "ContactBook" (Книга контактов):
# 1. В __init__ принимает name (название книги)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут contacts = [] (список контактов)
# 4. Создай метод add_contact(name, phone), который добавляет контакт в виде словаря:
#    {"name": name, "phone": phone}
# 5. Создай метод remove_contact(name), который удаляет контакт по имени
# 6. Создай метод find_contact(name), который возвращает контакт по имени
# 7. Создай метод show_contacts(), который возвращает список контактов

class ContactBook:
    def __init__(self, name):
        self.name = name
        self.contacts = []

    def add_contact(self, name, phone):
        self.contacts.append({"name": name, "phone": phone})

    def remove_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                self.contacts.remove(contact)
                break

    def find_contact(self, name):
        for contact in self.contacts:
            if contact["name"] == name:
                return contact
        return None

    def show_contacts(self):
        return self.contacts


contactBook = ContactBook("book")

contactBook.add_contact("uuu", "iiioo")
contactBook.add_contact("kkkk", "sssss")
contactBook.add_contact("qqqq", "mmmm")

print(contactBook.find_contact("kkkk"))

contactBook.remove_contact("uuu")

print(contactBook.show_contacts())
Задание 30: Класс ExpenseTracker
python
# Создай класс "ExpenseTracker" (Трекер расходов):
# 1. В __init__ принимает name (название трекера)
# 2. Сохраняет name в атрибут
# 3. Создай атрибут expenses = [] (список расходов)
# 4. Создай метод add_expense(category, amount, description), который добавляет расход в виде словаря:
#    {"category": category, "amount": amount, "description": description}
# 5. Создай метод get_total(), который возвращает общую сумму всех расходов
# 6. Создай метод get_by_category(category), который возвращает все расходы по категории
# 7. Создай метод show_expenses(), который возвращает список всех расходов

class ExpenseTracker:
    def __init__(self, name):
        self.name = name
        self.expenses = []

    def add_expense(self, category, amount, description):
        self.expenses.append({"category": category, "amount": amount, "description": description})

    def get_total(self):
        if len(self.expenses) == 0:
            return 0
        total = 0
        for expense in self.expenses:
            total = total + expense["amount"]
        return total

    def get_by_category(self, category):
        result = []
        for expense in self.expenses:
            if expense["category"] == category:
                result.append(expense)
        return result

    def show_expenses(self):
        return self.expenses


expenseTracker = ExpenseTracker("Vuugg")

expenseTracker.add_expense("qqq", 434, "aaaa")
expenseTracker.add_expense("zzz", 556, "ccc")
expenseTracker.add_expense("hhh", 789, "llll")

print(expenseTracker.get_total())
print(expenseTracker.get_by_category("zzz"))
УРОК 21: НАСЛЕДОВАНИЕ
Задание 31: Vehicle → Car
python
# Создай родительский класс "Vehicle" (Транспортное средство):
# 1. В __init__ принимает brand, model, year
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Марка: {brand}, Модель: {model}, Год: {year}"
# 4. Создай метод start(), который выводит "Двигатель запущен!"

# Создай дочерний класс "Car" (Автомобиль), который наследует от Vehicle:
# 1. В __init__ принимает brand, model, year, doors (количество дверей)
# 2. Сохраняет doors в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял количество дверей:
#    "Марка: {brand}, Модель: {model}, Год: {year}, Дверей: {doors}"

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}"

    def start(self):
        print("Двигатель запущен!")


class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}, Дверей: {self.doors}"


car = Car("fsf", "fsffff", 1976, 4)
print(car.info())
Задание 32: Employee → Manager
python
# Создай родительский класс "Employee" (Сотрудник):
# 1. В __init__ принимает name, salary
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Сотрудник: {name}, Зарплата: {salary}"
# 4. Создай метод work(), который выводит "Работаю..."

# Создай дочерний класс "Manager" (Менеджер), который наследует от Employee:
# 1. В __init__ принимает name, salary, team_size (размер команды)
# 2. Сохраняет team_size в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял размер команды:
#    "Менеджер: {name}, Зарплата: {salary}, Команда: {team_size}"
# 5. Переопредели метод work(), чтобы он выводил "Управляю командой"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"

    def work(self):
        print("Работаю...")


class Manager(Employee):
    def __init__(self, name, salary, team_size):
        super().__init__(name, salary)
        self.team_size = team_size

    def info(self):
        return f"Менеджер: {self.name}, Зарплата: {self.salary}, Команда: {self.team_size}"

    def work(self):
        print("Управляю командой")


manager = Manager("dg", 455667, "tyyi")

print(manager.info())
manager.work()
Задание 33: Device → Laptop
python
# Создай родительский класс "Device" (Устройство):
# 1. В __init__ принимает brand, model
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Устройство: {brand} {model}"
# 4. Создай метод turn_on(), который выводит "Устройство включено"

# Создай дочерний класс "Laptop" (Ноутбук), который наследует от Device:
# 1. В __init__ принимает brand, model, battery (заряд батареи в %)
# 2. Сохраняет battery в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял заряд батареи:
#    "Ноутбук: {brand} {model}, Заряд: {battery}%"

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Устройство: {self.brand} {self.model}"

    def turn_on(self):
        print("Устройство включено")


class Laptop(Device):
    def __init__(self, brand, model, battery):
        super().__init__(brand, model)
        self.battery = battery

    def info(self):
        return f"Ноутбук: {self.brand} {self.model}, Заряд: {self.battery}%"


laptop = Laptop("ggh", "jjkk", 44)
print(laptop.info())
Задание 34: Shape → Rectangle
python
# Создай родительский класс "Shape" (Фигура):
# 1. В __init__ принимает name (название фигуры)
# 2. Сохраняет name в атрибут
# 3. Создай метод area(), который возвращает 0 (площадь)
# 4. Создай метод info(), который возвращает:
#    "Фигура: {name}"

# Создай дочерний класс "Rectangle" (Прямоугольник), который наследует от Shape:
# 1. В __init__ принимает name, width, height
# 2. Сохраняет width и height в атрибуты
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод area(), чтобы он возвращал площадь (width * height)
# 5. Переопредели метод info(), чтобы он возвращал:
#    "Прямоугольник: {name}, Ширина: {width}, Высота: {height}, Площадь: {area}"

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        return f"Фигура: {self.name}"


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def info(self):
        return f"Прямоугольник: {self.name}, Ширина: {self.width}, Высота: {self.height}, Площадь: {self.area()}"


rectangle = Rectangle("gg", 44, 77)
print(rectangle.info())
Задание 35: Person → Student
python
# Создай родительский класс "Person" (Человек):
# 1. В __init__ принимает name, age
# 2. Сохраняет их в атрибуты
# 3. Создай метод introduce(), который возвращает:
#    "Меня зовут {name}, мне {age} лет"
# 4. Создай метод is_adult(), который возвращает True, если возраст >= 18

# Создай дочерний класс "Student" (Студент), который наследует от Person:
# 1. В __init__ принимает name, age, student_id
# 2. Сохраняет student_id в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод introduce(), чтобы он добавлял student_id:
#    "Меня зовут {name}, мне {age} лет, ID: {student_id}"

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет"

    def is_adult(self):
        return self.age >= 18


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def introduce(self):
        return f"Меня зовут {self.name}, мне {self.age} лет, ID: {self.student_id}"


student = Student("ddd", 16, 56778)
print(student.introduce())
Задание 36: Animal → Dog
python
# Создай родительский класс "Animal" (Животное):
# 1. В __init__ принимает name, species (вид)
# 2. Сохраняет их в атрибуты
# 3. Создай метод sound(), который возвращает "Звук животного"
# 4. Создай метод info(), который возвращает:
#    "{name} — {species}"

# Создай дочерний класс "Dog" (Собака), который наследует от Animal:
# 1. В __init__ принимает name, species, breed (порода)
# 2. Сохраняет breed в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод sound(), чтобы он возвращал "Гав-гав"
# 5. Переопредели метод info(), чтобы он добавлял породу:
#    "{name} — {species}, порода: {breed}"

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def sound(self):
        return "Звук животного"

    def info(self):
        return f"{self.name} — {self.species}"


class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def sound(self):
        return "Гав-гав"

    def info(self):
        return f"{self.name} — {self.species}, порода: {self.breed}"


dog = Dog("dgd", "jj", "ty")
print(dog.sound())
print(dog.info())
Задание 37: Vehicle → Bicycle
python
# Создай родительский класс "Vehicle" (Транспортное средство):
# 1. В __init__ принимает brand, model, year
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Марка: {brand}, Модель: {model}, Год: {year}"
# 4. Создай метод move(), который выводит "Транспортное средство движется"

# Создай дочерний класс "Bicycle" (Велосипед), который наследует от Vehicle:
# 1. В __init__ принимает brand, model, year, gears (количество передач)
# 2. Сохраняет gears в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял количество передач:
#    "Велосипед: {brand} {model}, Год: {year}, Передач: {gears}"
# 5. Переопредели метод move(), чтобы он выводил "Велосипед едет"

class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        return f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}"

    def move(self):
        print("Транспортное средство движется")


class Bicycle(Vehicle):
    def __init__(self, brand, model, year, gears):
        super().__init__(brand, model, year)
        self.gears = gears

    def info(self):
        return f"Велосипед: {self.brand} {self.model}, Год: {self.year}, Передач: {self.gears}"

    def move(self):
        print("Велосипед едет")


bicycle = Bicycle("zz", "aaw34", 1987, 8)
print(bicycle.info())
bicycle.move()
Задание 38: Appliance → WashingMachine
python
# Создай родительский класс "Appliance" (Бытовой прибор):
# 1. В __init__ принимает brand, power (мощность в Вт)
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Прибор: {brand}, Мощность: {power} Вт"
# 4. Создай метод turn_on(), который выводит "Прибор включён"

# Создай дочерний класс "WashingMachine" (Стиральная машина), который наследует от Appliance:
# 1. В __init__ принимает brand, power, capacity (загрузка в кг)
# 2. Сохраняет capacity в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял загрузку:
#    "Стиральная машина: {brand}, Мощность: {power} Вт, Загрузка: {capacity} кг"
# 5. Переопредели метод turn_on(), чтобы он выводил "Стиральная машина запущена"

class Appliance:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power

    def info(self):
        return f"Прибор: {self.brand}, Мощность: {self.power} Вт"

    def turn_on(self):
        print("Прибор включён")


class WashingMachine(Appliance):
    def __init__(self, brand, power, capacity):
        super().__init__(brand, power)
        self.capacity = capacity

    def info(self):
        return f"Стиральная машина: {self.brand}, Мощность: {self.power} Вт, Загрузка: {self.capacity} кг"

    def turn_on(self):
        print("Стиральная машина запущена")


washingMachine = WashingMachine("ttt", 666, 66)
print(washingMachine.info())
washingMachine.turn_on()
Задание 39: LibraryItem → Book
python
# Создай родительский класс "LibraryItem" (Библиотечный предмет):
# 1. В __init__ принимает title, year
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Год: {year}"
# 4. Создай метод get_type(), который возвращает "Предмет"

# Создай дочерний класс "Book" (Книга), который наследует от LibraryItem:
# 1. В __init__ принимает title, year, author, pages
# 2. Сохраняет author и pages в атрибуты
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял автора и страницы:
#    "Книга: {title}, Автор: {author}, Год: {year}, Страниц: {pages}"
# 5. Переопредели метод get_type(), чтобы он возвращал "Книга"

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def info(self):
        return f"Название: {self.title}, Год: {self.year}"

    def get_type(self):
        return "Предмет"


class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages

    def info(self):
        return f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}, Страниц: {self.pages}"

    def get_type(self):
        return "Книга"


book = Book("hhhh", 1999, "llll", 409)

print(book.info())
print(book.get_type())
Задание 40: Device → Smartphone
python
# Создай родительский класс "Device" (Устройство):
# 1. В __init__ принимает brand, model
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Устройство: {brand} {model}"
# 4. Создай метод turn_on(), который выводит "Устройство включено"

# Создай дочерний класс "Smartphone" (Смартфон), который наследует от Device:
# 1. В __init__ принимает brand, model, camera (мегапиксели)
# 2. Сохраняет camera в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял камеру:
#    "Смартфон: {brand} {model}, Камера: {camera} МП"
# 5. Переопредели метод turn_on(), чтобы он выводил "Смартфон включён"

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def info(self):
        return f"Устройство: {self.brand} {self.model}"

    def turn_on(self):
        print("Устройство включено")


class Smartphone(Device):
    def __init__(self, brand, model, camera):
        super().__init__(brand, model)
        self.camera = camera

    def info(self):
        return f"Смартфон: {self.brand} {self.model}, Камера: {self.camera} МП"

    def turn_on(self):
        print("Смартфон включён")


smartphone = Smartphone("wht", "jop", 68)
print(smartphone.info())
smartphone.turn_on()
Задание 41: Media → Movie
python
# Создай родительский класс "Media" (Медиа):
# 1. В __init__ принимает title, duration (в минутах)
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Длительность: {duration} мин"
# 4. Создай метод play(), который выводит "Воспроизведение..."

# Создай дочерний класс "Movie" (Фильм), который наследует от Media:
# 1. В __init__ принимает title, duration, director, rating
# 2. Сохраняет director и rating в атрибуты
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял режиссёра и рейтинг:
#    "Фильм: {title}, Режиссёр: {director}, Рейтинг: {rating}, Длительность: {duration} мин"
# 5. Переопредели метод play(), чтобы он выводил "Фильм {title} воспроизводится..."

class Media:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def info(self):
        return f"Название: {self.title}, Длительность: {self.duration} мин"

    def play(self):
        print("Воспроизведение...")


class Movie(Media):
    def __init__(self, title, duration, director, rating):
        super().__init__(title, duration)
        self.director = director
        self.rating = rating

    def info(self):
        return f"Фильм: {self.title}, Режиссёр: {self.director}, Рейтинг: {self.rating}, Длительность: {self.duration} мин"

    def play(self):
        print(f"Фильм {self.title} воспроизводится...")


movie = Movie("ooo", 98, "mmmm", 4.9)
print(movie.info())
movie.play()
УРОК 22: ПОЛИМОРФИЗМ
Задание 42: Фигуры
python
# Создай родительский класс "Shape" (Фигура):
# 1. В __init__ принимает name
# 2. Сохраняет name в атрибут
# 3. Создай метод area(), который возвращает 0 (заглушка)
# 4. Создай метод info(), который возвращает:
#    "Фигура: {name}"

# Создай три дочерних класса:
# - Rectangle (Прямоугольник): width, height → area = width * height
# - Circle (Круг): radius → area = 3.14 * radius ** 2
# - Triangle (Треугольник): base, height → area = 0.5 * base * height

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0

    def info(self):
        return f"Фигура: {self.name}"


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Rectangle("Прямоугольник", 44, 66),
          Circle("Круг", 78),
          Triangle("Треугольник", 65, 87)]

for shape in shapes:
    print(f"{shape.info()}, Площадь: {shape.area()}")
Задание 43: Сотрудники
python
# Создай родительский класс "Employee" (Сотрудник):
# 1. В __init__ принимает name, salary
# 2. Сохраняет их в атрибуты
# 3. Создай метод work(), который возвращает "Работает"
# 4. Создай метод info(), который возвращает:
#    "Сотрудник: {name}, Зарплата: {salary}"

# Создай три дочерних класса:
# - Manager (Менеджер): work() → "Управляет командой"
# - Developer (Разработчик): work() → "Пишет код"
# - Designer (Дизайнер): work() → "Рисует макеты"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        return "Работает"

    def info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"


class Manager(Employee):
    def work(self):
        return "Управляет командой"


class Developer(Employee):
    def work(self):
        return "Пишет код"


class Designer(Employee):
    def work(self):
        return "Рисует макеты"


employees = [Manager("Анна", 100000),
             Developer("Илья", 80000),
             Designer("Мария", 70000)]

for emp in employees:
    print(f"{emp.info()}, Работа: {emp.work()}")



# Создай родительский класс "LibraryItem" (Библиотечный предмет):
# 1. В __init__ принимает title, year
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Год: {year}"
# 4. Создай метод get_type(), который возвращает "Предмет"

# Создай дочерний класс "Book" (Книга), который наследует от LibraryItem:
# 1. В __init__ принимает title, year, author, pages
# 2. Сохраняет author и pages в атрибуты
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял автора и страницы:
#    "Книга: {title}, Автор: {author}, Год: {year}, Страниц: {pages}"
# 5. Переопредели метод get_type(), чтобы он возвращал "Книга"

# Создай объект Book и вызови его методы

class LibraryItem:
    def __init__(self, title, year):
        self.title = title
        self.year = year
    def info(self):
        return f"Название: {self.title}, Год: {self.year}"
    def get_type(self):
        print("Предмет")
class Book(LibraryItem):
    def __init__(self, title, year, author, pages):
        super().__init__(title, year)
        self.author = author
        self.pages = pages
    def info(self):
        return f"Книга: {self.title}, Автор: {self.year}, Год: {self.author}, Страниц: {self.pages}"
    def get_type(self):
        print("Книга")
book = Book("hhhh", "llll", 1999, 409)

print(book.info())
book.get_type()

# Создай родительский класс "Device" (Устройство):
# 1. В __init__ принимает brand, model
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Устройство: {brand} {model}"
# 4. Создай метод turn_on(), который выводит "Устройство включено"

# Создай дочерний класс "Smartphone" (Смартфон), который наследует от Device:
# 1. В __init__ принимает brand, model, camera (мегапиксели)
# 2. Сохраняет camera в атрибут
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял камеру:
#    "Смартфон: {brand} {model}, Камера: {camera} МП"
# 5. Переопредели метод turn_on(), чтобы он выводил "Смартфон включён"

# Создай объект Smartphone и вызови его методы

class DeviceDevice:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def info(self):
        return f"Устройство: {self.brand} {self.model}"
    def turn_on(self):
        print("Устройство включено")
class Smartphone(DeviceDevice):
    def __init__(self, brand, model, camera):
        super().__init__(brand, model)
        self.camera = camera
    def info(self):
        return f"Смартфон: {self.brand} {self.model}, Камера: {self.camera} МП"
    def turn_on(self):
        print("Смартфон включён")
smartphone = Smartphone("wht", "jop", 68)
print(smartphone.info())
smartphone.turn_on()

# Создай родительский класс "Media" (Медиа):
# 1. В __init__ принимает title, duration (в минутах)
# 2. Сохраняет их в атрибуты
# 3. Создай метод info(), который возвращает:
#    "Название: {title}, Длительность: {duration} мин"
# 4. Создай метод play(), который выводит "Воспроизведение..."

# Создай дочерний класс "Movie" (Фильм), который наследует от Media:
# 1. В __init__ принимает title, duration, director, rating
# 2. Сохраняет director и rating в атрибуты
# 3. Вызывает __init__ родителя через super()
# 4. Переопредели метод info(), чтобы он добавлял режиссёра и рейтинг:
#    "Фильм: {title}, Режиссёр: {director}, Рейтинг: {rating}, Длительность: {duration} мин"
# 5. Переопредели метод play(), чтобы он выводил "Фильм {title} воспроизводится..."

# Создай объект Movie и вызови его методы

class Media:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration
    def info(self):
        return f"Название: {self.title}, Длительность: {self.duration} мин"
    def play(self):
        print("Воспроизведение...")
class Movie(Media):
    def __init__(self, title, duration, director, rating):
        super().__init__(title, duration)
        self.director = director
        self.rating = rating
    def info(self):
        return f"Фильм: {self.title}, Режиссёр: {self.director}, Рейтинг: {self.rating}, Длительность: {self.duration} мин"
    def play(self):
        print(f"Фильм {self.title} воспроизводится...")
movie = Movie("ooo", "mmmm", 4.9, 98)
print(movie.info())
movie.play()

# Создай родительский класс "Shape" (Фигура):
# 1. В __init__ принимает name
# 2. Сохраняет name в атрибут
# 3. Создай метод area(), который возвращает 0 (заглушка)
# 4. Создай метод info(), который возвращает:
#    "Фигура: {name}"

# Создай три дочерних класса:
# - Rectangle (Прямоугольник): width, height → area = width * height
# - Circle (Круг): radius → area = 3.14 * radius ** 2
# - Triangle (Треугольник): base, height → area = 0.5 * base * height

# Создай список из разных фигур, выведи их информацию и площадь через цикл

class Shape:
    def __init__(self, name):
        self.name = name
    def area(self):
        return 0
    def info(self):
        return f"Фигура: {self.name}"
class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
Shapes = [Rectangle("tt", 44, 66), Circle("jjj", 78), Triangle("bbbb", 65, 87)]
for Shape in Shapes:
    print(f"{Shape.info()}, Площадь: {Shape.area()}")
    
# Создай родительский класс "Employee" (Сотрудник):
# 1. В __init__ принимает name, salary
# 2. Сохраняет их в атрибуты
# 3. Создай метод work(), который возвращает "Работает"
# 4. Создай метод info(), который возвращает:
#    "Сотрудник: {name}, Зарплата: {salary}"

# Создай три дочерних класса:
# - Manager (Менеджер): work() → "Управляет командой"
# - Developer (Разработчик): work() → "Пишет код"
# - Designer (Дизайнер): work() → "Рисует макеты"

# Создай список из разных сотрудников, выведи их информацию и результат work() через цикл

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def work(self):
        return "Работает"
    def info(self):
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"
class Manager(Employee):
    def work(self):
        return "Управляет командой"
class Developer(Employee):
    def work(self):
        return "Пишет код"
class Designer(Employee):
    def work(self):
        return "Рисует макеты"
Employees = [Manager("qqq", 45667), Developer("zzz", 56789), Designer("bbbb", 76544)]
for Employee in Employees:
    print(f"{Employee.info()}, результат: {Employee.work()}")

# Создай класс "User" (Пользователь):
# 1. В __init__ принимает username и password
# 2. Сохраняет username как публичный атрибут
# 3. Сохраняет password как приватный атрибут (__password)
# 4. Создай метод get_username(), который возвращает имя пользователя
# 5. Создай метод check_password(password), который возвращает True, если пароль совпадает
# 6. Создай метод set_password(old_password, new_password), который:
#    - проверяет old_password
#    - если совпадает — меняет пароль на new_password
#    - если нет — выводит "Неверный старый пароль"
# 7. Создай пользователя, проверь пароль и измени его

class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password
    def get_username(self):
        return self.username
    def check_password(self, password):
        return password == self.__password
    def set_password(self, old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
            print("Пароль успешно изменён")
        else:
            print("Неверный старый пароль")
            
user = User("Tetler", "123bmuik")

# Проверяем пароль
print(user.check_password("123bmuik"))   # True
print(user.check_password("wrong"))      # False

# Меняем пароль
user.set_password("123bmuik", "uiu98")   # ✅ старый → новый

# Проверяем новый пароль
print(user.check_password("uiu98"))      # True
print(user.check_password("123bmuik"))   # False (старый уже не работает)

# Создай класс "Product" (Товар):
# 1. В __init__ принимает name, price, quantity
# 2. Сохраняет name как публичный атрибут
# 3. Сохраняет price и quantity как приватные атрибуты (__price, __quantity)
# 4. Создай метод get_price(), который возвращает цену
# 5. Создай метод get_quantity(), который возвращает количество
# 6. Создай метод set_price(new_price), который:
#    - проверяет, что new_price >= 0
#    - если да — меняет цену
#    - если нет — выводит "Цена не может быть отрицательной"
# 7. Создай метод set_quantity(new_quantity), который:
#    - проверяет, что new_quantity >= 0
#    - если да — меняет количество
#    - если нет — выводит "Количество не может быть отрицательным"
# 8. Создай метод total_cost(), который возвращает общую стоимость (price * quantity)
# 9. Создай товар, измени цену и количество, выведи общую стоимость

class Product:
    def __init__(self, name, price, quantity):
        self.name  = name
        self.__price = price
        self.__quantity = quantity
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity
    def set_price(self, new_price):
        if new_price >= 0:
            self.__price = new_price
        else:
            print("Цена не может быть отрицательной")
    def set_quantity(self, new_quantity):
        if new_quantity >= 0:
            self.__quantity = new_quantity
        else:
            print("Количество не может быть отрицательным")
    def total_cost(self):
        return self.__price * self.__quantity
product = Product("iii", 6999, 50)
product.set_price(7800)
product.set_quantity(70)
print(product.total_cost())

# Создай класс "BankAccount" (Банковский счёт):
# 1. В __init__ принимает owner и balance (по умолчанию 0)
# 2. Сохраняет owner как публичный атрибут
# 3. Сохраняет balance как приватный атрибут (__balance)
# 4. Создай метод get_balance(), который возвращает баланс
# 5. Создай метод deposit(amount), который:
#    - проверяет, что amount > 0
#    - если да — увеличивает баланс
#    - если нет — выводит "Сумма должна быть положительной"
# 6. Создай метод withdraw(amount), который:
#    - проверяет, что amount > 0 и amount <= balance
#    - если да — уменьшает баланс
#    - если нет — выводит "Недостаточно средств" или "Сумма должна быть положительной"
# 7. Создай счёт, пополни и сними деньги, выведи баланс

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("Сумма должна быть положительной")
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма должна быть положительной")
        elif amount > self.__balance:
            print("Недостаточно средств")
        else:
            self.__balance = self.__balance - amount
bankAccount = BankAccount("kio", 609876)
bankAccount.deposit(56789)
bankAccount.withdraw(3221)
print(bankAccount.get_balance())

# Создай класс "Student" (Студент):
# 1. В __init__ принимает name, grade (по умолчанию 0)
# 2. Сохраняет name как публичный атрибут
# 3. Сохраняет grade как приватный атрибут (__grade)
# 4. Создай метод get_grade(), который возвращает оценку
# 5. Создай метод set_grade(new_grade), который:
#    - проверяет, что new_grade от 0 до 100
#    - если да — меняет оценку
#    - если нет — выводит "Оценка должна быть от 0 до 100"
# 6. Создай метод improve(amount), который увеличивает grade на amount (максимум 100)
# 7. Создай метод info(), который возвращает:
#    "Студент: {name}, Оценка: {grade}"
# 8. Создай студента, измени оценку и выведи информацию

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.__grade = grade
    def get_grade(self):
        return self.__grade
    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Оценка должна быть от 0 до 100")
    def improve(self, amount):
        if self.__grade + amount <= 100:
            self.__grade = self.__grade + amount
        else:
            print("Оценка не может быть выше 100")
    def info(self):
        return f"Студент: {self.name}, Оценка: {self.__grade}"
student = Student("vhj", 65)
student.set_grade(76)
print(student.info())

# Создай класс "Book" (Книга):
# 1. В __init__ принимает title, author, pages
# 2. Сохраняет title и author как публичные атрибуты
# 3. Сохраняет pages как приватный атрибут (__pages)
# 4. Создай метод get_pages(), который возвращает количество страниц
# 5. Создай метод set_pages(new_pages), который:
#    - проверяет, что new_pages > 0
#    - если да — меняет количество страниц
#    - если нет — выводит "Страниц должно быть больше 0"
# 6. Создай метод is_long(), который возвращает True, если страниц больше 300
# 7. Создай метод info(), который возвращает:
#    "Книга: {title}, Автор: {author}, Страниц: {pages}"
# 8. Создай книгу, измени количество страниц и выведи информацию

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.__pages = pages
    def get_pages(self):
        return self.__pages
    def set_pages(self, new_pages):
        if new_pages > 0:
            self.__pages = new_pages
        else:
            print("Страниц должно быть больше 0")
    def is_long(self):
        return self.__pages > 300
    def info(self):
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.__pages}"
book = Book("tt", "mmm", 234)
book.set_pages(299)
print(book.info())

# Создай класс "Temperature" (Температура):
# 1. В __init__ принимает celsius (температура в градусах Цельсия)
# 2. Сохраняет celsius как приватный атрибут (__celsius)
# 3. Создай метод get_celsius(), который возвращает температуру
# 4. Создай метод set_celsius(new_celsius), который:
#    - проверяет, что new_celsius >= -273.15 (абсолютный ноль)
#    - если да — меняет температуру
#    - если нет — выводит "Температура не может быть ниже абсолютного нуля"
# 5. Создай метод to_fahrenheit(), который возвращает температуру в Фаренгейтах
#    Формула: fahrenheit = celsius * 9/5 + 32
# 6. Создай метод to_kelvin(), который возвращает температуру в Кельвинах
#    Формула: kelvin = celsius + 273.15
# 7. Создай метод info(), который возвращает:
#    "Температура: {celsius}°C, {fahrenheit}°F, {kelvin}K"
# 8. Создай температуру, измени её и выведи информацию

class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    def get_celsius(self):
        return self.__celsius
    def set_celsius(self, new_celsius):
        if new_celsius >= -273.15:
            self.__celsius = new_celsius
        else:
            print("Температура не может быть ниже абсолютного нуля")
    def to_fahrenheit(self):
        return self.__celsius * 9/5 + 32
    def to_kelvin(self):
        return self.__celsius + 273.15
    def info(self):
        return f"Температура: {self.__celsius}°C, {self.to_fahrenheit()}°F, {self.to_kelvin()}K"
temperature = Temperature(356)
temperature.set_celsius(56)
print(temperature.to_fahrenheit())
print(temperature.to_kelvin())
print(temperature.info())

# Создай класс "Student" (Студент):
# 1. В __init__ принимает name и grade (оценка)
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает строку:
#    "Студент: {name}, Оценка: {grade}"
# 4. Создай метод __eq__, который возвращает True, если у студентов одинаковое имя
# 5. Создай два объекта Student и сравни их через ==

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"Студент: {self.name}, Оценка: {self.grade}"
    def __eq__(self, other):
        return self.name == other.name
student = Student("yyy", 77)
student1 = Student("nnn", 88)
print(student == student1)

# Создай класс "Book" (Книга):
# 1. В __init__ принимает title, author, pages
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает:
#    "Книга: {title}, Автор: {author}, Страниц: {pages}"
# 4. Создай метод __len__, который возвращает количество страниц (pages)
# 5. Создай метод __eq__, который возвращает True, если у книг одинаковое название и автор
# 6. Создай две одинаковые книги и сравни их через ==, выведи len()

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
book = Book("hhh", "uuu", 678)
book1 = Book("hhh", "uuu", 678)
print(book == book1)
print(len(book))

# Создай класс "Rectangle" (Прямоугольник):
# 1. В __init__ принимает width и height
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает:
#    "Прямоугольник: {width}x{height}"
# 4. Создай метод __add__, который возвращает новый прямоугольник с шириной = width1 + width2 и высотой = height1 + height2
# 5. Создай метод __eq__, который возвращает True, если у прямоугольников равные площади
# 6. Создай два прямоугольника, сложи их и сравни площади

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return f"Прямоугольник: {self.width}x{self.height}"
    def area(self):
        return self.width * self.height
    def __add__(self, other):
        new_width = self.width + other.width
        new_height = self.height + other.height
        return Rectangle(new_width, new_height)
    def __eq__(self, other):
        return self.area() == other.area()
rectangle = Rectangle(45, 67)
rectangle1 = Rectangle(65, 78)
print(rectangle + rectangle1)
print(rectangle == rectangle1)

# Создай класс "Money" (Деньги):
# 1. В __init__ принимает amount (сумма) и currency (валюта, по умолчанию "USD")
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает строку:
#    "{amount} {currency}"
# 4. Создай метод __add__, который принимает другой объект Money и возвращает новый объект Money с суммой равной сумме двух других (валюту оставь как у первого)
# 5. Создай метод __eq__, который возвращает True, если суммы равны (игнорируя валюту)
# 6. Создай два объекта Money, сложи их и сравни их с третьим.

class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    def __str__(self):
        return f"{self.amount} {self.currency}"
    def __add__(self, other):
        new_amount = self.amount + other.amount
        return Money(new_amount, self.currency)
    def __eq__(self, other):
        return self.amount == other.amount
money = Money(5678, "USD")
money1 = Money(6790, "USD")
money2 = money + money1
print(money2)              # 12468 USD
print(money == money1)    # False (5678 == 6790)
print(money == Money(5678, "EUR"))   # True (суммы равны, валюта игнорируется)

# Создай класс "Vector" (Вектор):
# 1. В __init__ принимает x и y (координаты)
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает:
#    "Вектор({x}, {y})"
# 4. Создай метод __add__, который возвращает новый вектор:
#    x = self.x + other.x
#    y = self.y + other.y
# 5. Создай метод __eq__, который возвращает True, если x и y совпадают
# 6. Создай метод __len__, который возвращает длину вектора по формуле:
#    длина = (x**2 + y**2) ** 0.5
# 7. Создай два вектора, сложи их, сравни и выведи длину

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Вектор({self.x}, {self.y})"
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    def __len__(self):
        return int((self.x**2 + self.y**2) ** 0.5)
vector = Vector(65, 76)
vector1 = Vector(76, 89)
print(vector + vector1)
print(vector == vector1)
print(len(vector))
print(len(vector1))

# Создай класс "Book" (Книга):
# 1. В __init__ принимает title, author, pages
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает:
#    "Книга: {title}, Автор: {author}, Страниц: {pages}"
# 4. Создай метод __len__, который возвращает количество страниц
# 5. Создай метод __eq__, который возвращает True, если у книг одинаковое название и автор
# 6. Создай метод __add__, который возвращает новую книгу с количеством страниц = pages1 + pages2
#    Название и автор новой книги — "Сборник" и "Автор: {author1} и {author2}"
# 7. Создай три книги: первую, вторую и третью (сумму первых двух)
# 8. Выведи информацию о всех трёх книгах и сравни их

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"Книга: {self.title}, Автор: {self.author}, Страниц: {self.pages}"
    def __len__(self):
        return self.pages
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __add__(self, other):
        new_title = "Сборник"
        new_author = f"{self.author} и {other.author}"
        new_pages = self.pages + other.pages
        return Book(new_title, new_author, new_pages)
book = Book("yy", "gg", 456)
book1 = Book("aaa", "jjj", 123)
book2 = book + book1

print(book)
print(book1)
print(book2)

print(book == book1)
print(book == book2)
print(len(book2))

# Создай класс "Student" (Студент):
# 1. В __init__ принимает name, grade (оценка)
# 2. Сохраняет их в атрибуты
# 3. Создай метод __str__, который возвращает:
#    "Студент: {name}, Оценка: {grade}"
# 4. Создай метод __eq__, который возвращает True, если у студентов одинаковое имя
# 5. Создай метод __lt__, который возвращает True, если у первого студента оценка меньше, чем у второго
# 6. Создай метод __add__, который возвращает нового студента с именем "Сборный" и средней оценкой
#    (среднее арифметическое двух оценок)
# 7. Создай трёх студентов, сравни их по оценкам и сложи двух из них

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    def __str__(self):
        return f"Студент: {self.name}, Оценка: {self.grade}"
    def __eq__(self, other):
        return self.name == other.name
    def __lt__(self, other):
        return self.grade < other.grade
    def __add__(self, other):
        new_name = "Сборный"
        new_grade = (self.grade + other.grade) / 2
        return Student(new_name, new_grade)
student = Student("tyu", 56)
student1 = Student("klc", 87)
student2 = student + student1
print(student == student1)
print(student == student2)
print(student1 == student2)
print(student + student1)



