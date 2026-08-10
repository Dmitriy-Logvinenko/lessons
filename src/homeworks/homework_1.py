# Задаём переменные начального счёта и правильных ответов:
counter = 0
counter_answer = 0
counter_percent = 0.00

True_answer_1 = "is"
True_answer_2 = "am"
True_answer_3 = "in"

# Приветствуем пользователя и просим его ввести своё имя:
print("Привет! Предлагаю проверить свои знания английского!")

user_name = input("Напиши, как тебя зовут: ")
if user_name == "":
    user_name = "Мистер Фиш"
print(f"\nПривет, {user_name}, начинаем тренировку!")

# Задаём вопросы и условия к ним:
print("Вопрос 1: My name ___ Vova.")
answer_1 = input("Введите Ваш ответ: ")

if answer_1 == "is":
    counter += 10
    counter_answer += 1
    counter_percent += 33.33
    print("Ответ верный! \nВы получаете 10 баллов!\n")
else:
    print(f"Неправильно. \nПравильный ответ: {True_answer_1}\n")

print("Вопрос 2: I ___ a coder.")
answer_2 = input("Введите Ваш ответ: ")

if answer_2 == "am":
    counter += 10
    counter_answer += 1
    counter_percent += 33.33
    print("Ответ верный! \nВы получаете 10 баллов!\n")
else:
    print(f"Неправильно. \nПравильный ответ: {True_answer_2}\n")

print("Вопрос 3: I live ___ Moscow.")
answer_3 = input("Введите Ваш ответ: ")

if answer_3 == "in":
    counter += 10
    counter_answer += 1
    counter_percent += 33.33
    print("Ответ верный! \nВы получаете 10 баллов!\n")
else:
    print(f"Неправильно. \nПравильный ответ: {True_answer_3}\n")

# Задаём условия вывода правильного окончания слов "вопрос" и "процент" ;)
if counter_answer == 0:
    question_ending = str("ов")
elif counter_answer == 1:
    question_ending = str("")
else:
    question_ending = str("а")

if counter_answer == 1:
    percent_ending = str("а")
else:
    percent_ending = str("ов")

# Создаём эстетику для 100.00 процентов B)
if counter_answer == 3:
    counter_percent = 100.00

# Выводим результаты
print(f"""Вот и всё, {user_name}!
Вы ответили на {counter_answer} вопрос{question_ending} из 3 верно.
Вы заработали {counter} Баллов.
Это {round(counter_percent, 2)} процент{percent_ending}.""")
