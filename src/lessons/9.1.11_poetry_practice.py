# Задача 1
def to_generalize(first_list: list[int], second_list: list[int]) -> list[int]:
    """
    Принимает два списка чисели.
    Возвращает список с общими числами.
    """
    general_list = []

    for i in first_list:
        if i in second_list:
            general_list.append(i)
    return general_list


print(to_generalize([1, 2, 3, 4], [3, 4, 5, 6]))

# Задача 2
def to_palindrome_number(new_list: list[int]) -> list[int]:
    """
    Принимает список чисел.
    Возвращает список палиндромных чисел.
    """
    palindrome_list = []

    for number in new_list:
        if str(number) == str(number)[::-1]:
            palindrome_list.append(number)

    return palindrome_list


print(to_palindrome_number([121, 123, 131, 34543]))

# Задача 3
def to_generalize(first_list: list[int], second_list: list[int]) -> list[int]:
    """
    Принимает два списка чисели.
    Возвращает список с общими числами.
    """
    general_list = []

    for i in first_list:
        if i not in second_list:
            general_list.append(i)

    for i in second_list:
        if i not in first_list:
            general_list.append(i)

    return general_list


print(to_generalize([1, 2, 3, 4], [3, 4, 5, 6]))

# Задача 4
def circle_area(r: int) -> float:
    """
    Принимает радиус окружности.
    Возвращает длину окружности.
    """
    PI = 3.14
    circle_area = PI * r ** 2
    return circle_area


def format_description(r: int, area: float) -> str:
    return "Radius is " + str(r) + "; area is " + str(round(area, 2))


def get_info(r: int) -> float:
    area = circle_area(r)
    description = format_description(r, area)
    print(description)
    return area


radius = int(input("Enter circle radius (int): "))
get_info(radius)
