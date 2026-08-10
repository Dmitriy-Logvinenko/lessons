# Метод count или как упростить поиск

numbers = [10, 4, 5, 1, 2, 10, 7, 8, 1, 2, 10]
print(numbers.count(1), numbers.count(2))

numbers = [10, 4, 5, 1, 2, 10, 7, 8, 1, 2, 10]

counter_1 = 0
counter_2 = 0

for i in numbers:
    if i == 1:
        counter_1 += 1
    if i == 2:
        counter_2 += 1

print(f"Единиц: {counter_1}")
print(f"Двоек: {counter_2}")

print("\n\n")

# Подсчёт до нужной суммы

numbers = [12, 27, 36, 55, 3, 16, 24, 33, 55]
user_input = int(input("ввод: "))

summ = 0
score = 0

for i in numbers:
    if summ < user_input:
        summ += i
        score += 1

print(f"Сумма: {summ}, Счёт: {score}")

print("\n\n")

numbers = [1, 2, 3, 4, 5, 6]

for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers[i] = numbers[i] // 2
    else:
        numbers.pop(i)

print(numbers)

numbers = [1, 2, 3, 4, 5, 6]
n = len(numbers)
i = 0

while i < n:
    if numbers[i] % 2 == 0:
        numbers[i] = numbers[i] // 2
        i += 1
    else:
        numbers.pop(i)
        n -= 1

print(numbers)
