# Приветствуем пользователя
print("""Привет! Это викторина по английскому языку.
Тебе нужно заполнить пропущенные слова.\n""")

# Вопросы и ответы
questions = [
    "My name ___ Vova.",
    "I ___ a coder.",
    "I live ___ Moscow.",
    "She ___ from London.",
    "We ___ learning Python.",
]

answers = ["is", "am", "in", "is", "are"]

# Какая викторина без вариантов ответа
options = ["1. is", "2. am", "3. in", "4. are"]

# Счётчики
correct = 0
score = 0
attempts = 0
counter_questions = 0

# Спрашиваем имя
print("Как тебя зовут?")

user_name = input("Введи своё имя: ")
if user_name == "":
    user_name = "Мистер Фиш"

# Выводим начало
print(f"""\nПриятно познакомится, {user_name}!\n
Начинаем викторину.
Всего {len(questions)} вопросов.
Напиши "stop", чтобы выйти.\n""")

# Основной цикл: Выводит вопросы и проверяет ответы
# И внутренний цикл: Проверяет на наличие пустой строки
for question in range(len(questions)):
    counter_questions += 1

    while True:
        print(f"Вопрос {question + 1}. {questions[question]}")
        for option in options:
            print(option)

        user_answer = input("Введи ответ, который считаешь верным: ")

        # Цикл проверки ответа
        if user_answer:
            if user_answer == answers[question]:
                correct += 1
                score += 10
                attempts += 1
                print("Верно!\n")
            else:
                attempts += 1
                print(f"Неверно. Правильный ответ: {answers[question]}\n")
            break
        else:
            attempts += 1
            print("Ты ничего не ввёл, попробуй ещё раз.\n")

    # Обработка завершения при вводе "stop"
    if user_answer == "stop":
        print("Хорошо. Закончим викторину на этом вопросе.\n")
        break

# Считаем проценты
percent = (correct / len(questions)) * 100 if attempts > 0 else 0

# Выводим итоги
print(f"Вот и всё, {user_name}!")
print("На этом викторина закончилась.\n")
print(f"""Подведём итоги:
- Пройдено вопросов {counter_questions} из {len(questions)}.
- Ты совершил попыток: {attempts}.
- Правильных ответов: {correct}.
- Ты получаешь {score} Баллов.
- Твой процент успеха = {round(percent, 2)}%""")
