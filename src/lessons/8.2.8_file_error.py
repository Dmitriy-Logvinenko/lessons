import os

# Вариант 1
full_path = os.path.join(os.path.dirname(__file__), "../utils", "example.txt")

with open(full_path, "r") as file:
    print(file.read())

# Вариант 2
base_path = os.path.dirname(__file__)
full_path = os.path.join(base_path, "../utils", "example.txt")

with open(full_path, "r") as file:
    print(file.read())

# Вариант 3
base_path = r"C:\Users\Dmitr\PycharmProjects\my_projects"

with open("utils/example.txt", "r") as file:
    print(file.read())
