# Задача 1
def identify_uniqueness(*list_):
    return list(set(list_))


print(identify_uniqueness(1, 2, 1, 3, 2, 4, 4, 5))


# Задача 2
def filter_above(numbers, min_value=5):
    list_ = []

    for number in numbers:
        if number >= min_value:
            list_.append(number)

    return list_


print(filter_above([6, 4, 7, 2, 5, 1, 23, 6, 4, 5, 8]))


# Задача 2.1
def filter_above2(numbers, min_value=5):
    n = len(numbers)
    i = 0
    while i < n:
        if numbers[i] < min_value:
            numbers.remove(numbers[i])
            n -= 1
        elif numbers[i] >= min_value:
            i += 1
        else:
            break

    return numbers


print(filter_above([6, 4, 7, 2, 5, 1, 23, 6, 4, 5, 8]))


# Задача 3
def get_average(*numbers):
    total = 0

    for n in numbers:
        total += n
    return round(total / len(numbers), 1)


print(get_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 50))


# Задача 3.1
def get_average2(*numbers):
    return sum(numbers) / len(numbers)


print(get_average(1, 2, 3, 4, 5, 6, 7, 8, 9, 50))
