user_name = input("Введите ФИО: ")

new_list = user_name.split()

for i in range(len(new_list)):
    if new_list[i].isalpha():
        new_list[i] = new_list[i].title()
    else:
        print("Имя должно содержать только буквы.")
        break
else:
    print(new_list)

#######################################


true_pin = '1111'
attempts = 3

while attempts > 0:
    attempts -= 1
    pin = input('Введите пин-код: ')

    if pin == true_pin:
        print('Пин-код верный.')
        break
    else:
        print('Пин-код неверный.')

        if attempts == 0:
            continue
        print('Повторите ещё раз.\n'
              f'\nПопыток осталось: {attempts}')
else:
    print('\nВы превысили число попыток.')
