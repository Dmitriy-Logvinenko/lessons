# Словарь легкого уровня:
words_easy = {
    "Family": "Семья",
    "Hand": "Рука",
    "People": "Люди",
    "Evening": "Вечер",
    "Minute": "Минута",
}

# Словарь среднего уровня:
words_medium = {
    "Believe": "Верить",
    "Feel": "Чувствовать",
    "Make": "Делать",
    "Open": "Открывать",
    "Think": "Думать",
}

# Словарь сложного уровня:
words_hard = {
    "Rural": "Деревенский",
    "Fortune": "Удача",
    "Exercise": "Упражнение",
    "Suggest": "Предлагать",
    "Except": "Кроме",
}

# Словарь рангов:
levels = {
    0: "Нулевой.",
    1: "Так себе.",
    2: "Можно лучше.",
    3: "Норм.",
    4: "Хорошо.",
    5: "Отлично!",
}


# Функция выбора словаря:
def choose_difficulty():
    """
    Предлагает выбрать уровень сложности.
    Возвращает словарь выбранного уровня сложности.
    """

    user_input = input()

    # Проверка:
    if user_input.lower() == "легкий":
        print("Ты выбрал легкий уровень сложности.")
        words = words_easy
    elif user_input.lower() == "средний":
        print("Ты выбрал средний уровень сложности.")
        words = words_medium
    elif user_input.lower() == "сложный":
        print("Ты выбрал сложный уровень сложности.")
        words = words_hard
    else:
        print("Выбран средний уровень сложности.")
        words = words_medium
    return words


# Функция вопросов и ответов:
def play_game(words):
    """
    Задаёт слова и проверяет перевод.
    Возвращает словарь верности ответов пользователя.
    """

    answers = {}
    number_question = 0

    # Цикл вывода вопросов
    for k, v in words.items():
        print(f"\n{number_question + 1}. {k}, букв: {len(v)}, начинается на {v[0]}...")

        user_answer = input("Введи перевод: ")
        number_question += 1

        # Цикл проверки ответов:
        if user_answer.lower() == v.lower():
            print(f"Верно! {k} — это {v}.")
            answers[v] = True
        else:
            print(f"Неверно. {k} — это {v}.")
            answers[v] = False

    # Возвращаем словарь ответов:
    return answers


# Функция проверки ответов:
def display_results(answers):
    """
    Проверяет и выводит ответы.
    """

    # Списки ответов:
    true_answers = []
    false_answers = []

    # Цикл проверки:
    for k, v in answers.items():
        if v:
            true_answers.append(k)
        else:
            false_answers.append(k)

    # Вывод правильных ответов:
    print("\nПравильно отвечены слова:")
    if true_answers:
        for i in true_answers:
            print(i, end="\n")
    else:
        print("Таких нет.")

    # Вывод неправильных ответов:
    print("\nНеправильно отвечены слова:")
    if false_answers:
        for i in false_answers:
            print(i, end="\n")
    else:
        print("Таких нет.")


# Функция формирования рангов:
def calculate_rank(answers):
    """
    Считает правильные ответы и возвращает ранк.
    """

    score = 0

    # Считаем правильные ответы:
    for k, v in answers.items():
        if v:
            score += 1

    # Формируем ранк:
    for k, v in levels.items():
        if score == k:
            return v


# Приветствие:
print("""Привет! Давай сыграем в "Угадай перевод"!
Тебе нужно будет несколько раз угадать, какой перевод у слова.
""")

# Знакомство:
print("Для начала, давай познакомимся!")
user_name = input("Напиши своё имя: ")
if user_name == "":
    user_name = "Мистер Фиш"

# Выбор словаря:
print(
    f"\nПриятно познакомится, {user_name}!\n"
    "Выбери уровень сложности:\n"
    "Легкий, средний или сложный."
)

words = choose_difficulty()

print("\nОтлично, теперь приступим к игре!")
print(f"Мы предложим {len(words)} слов, подбери перевод.")

# Игра "Угадай перевод":
game = play_game(words)

# Вывод итогов:
print(f"\nВот и всё, {user_name}!\n" "Подведём итоги:")

# Проверка ответов:
display_results(game)

# Система рангов:
rank = calculate_rank(game)
print("\nТвой ранг:")
print(rank)
