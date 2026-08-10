# Задача 1
# 1. Запись начального лог-сообщения
with open("log.txt", "w", encoding="windows-1251") as file:
    file.write("Log Entry 1\n")

# 2. Чтение содержимого файла
with open("log.txt", "r", encoding="windows-1251") as file:
    content = file.read()
    print("Содержимое файла после первой записи:")
    print(content)

# 3. Добавление нового лог-сообщения
with open("log.txt", "a", encoding="windows-1251") as file:
    file.write("Log Entry 2\n")

# 4. Чтение содержимого файла после добавления
with open("log.txt", "r", encoding="windows-1251") as file:
    content = file.read()
    print("Содержимое файла после добавления нового лог-сообщения:")
    print(content)

# Задача 2
# 1. Запись списка покупок
with open("shopping_list.txt", "w", encoding="windows-1251") as file:
    file.write("Milk\n")
    file.write("Bread\n")
    file.write("Eggs\n")

# 2. Чтение содержимого файла
with open("shopping_list.txt", "r", encoding="windows-1251") as file:
    print(file.read())

# 3. Добавление новых элементов
with open("shopping_list.txt", "a", encoding="windows-1251") as file:
    file.write("Butter\n")
    file.write("Cheese\n")

# 4. Чтение содержимого файла после добавления
with open("shopping_list.txt", "r", encoding="windows-1251") as file:
    print(file.read())
