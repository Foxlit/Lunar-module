import values


burnt_fuel = 0
validation = True
end_game = False


def check_input(curr_fuel_portion):
    float_input_fuel = 0
    try:
        float_input_fuel = abs(float(curr_fuel_portion))
        if float(fuel) - float_input_fuel < 0:
            print("У вас нет столько топлива!")
            valid_result = False
        else:
            valid_result = True
    except ValueError:
        print("Некорректный ввод! Введите число")
        valid_result = False
    return float_input_fuel, valid_result


def control_remaining_fuel(curr_fuel):
    if curr_fuel < 0:
        return False


def check_flight_status(curr_height, curr_speed):
    if 0 > curr_height > (-30) and curr_speed < 50:
        return 1  # successful landing
    elif curr_height < (-10):
        return -1  # crashed
    else:
        return 0  # still flying


def make_calculations(curr_height, curr_speed, curr_fuel, curr_fuel_portion):
    curr_fuel -= curr_fuel_portion
    curr_speed += g - curr_fuel_portion * k
    curr_height -= curr_speed
    return curr_height, curr_speed, curr_fuel


def check_level_input(chosen_level):
    correct_level = chosen_level
    while True:
        try:
            correct_level = int(correct_level)
        except ValueError:
            pass
        if correct_level in range(1, 4):
            return correct_level
        else:
            correct_level = input('Некорректный выбор. Выберите от 1 до 3: ')



print(f' Добро Пожаловать в Lunar Module!\n Здесь тебе предстоит посадить космический модуль на Луну!\n ')
level = check_level_input(input('Введите уровень от 1 до 3: '))

fuel, speed, height, g, mass, k = values.get_values_by_level(level)


print(f'Вот начальные данные, чтобы сориентироваться:\nТопливо:  {fuel} кг\nТвоя начальная скорость:  {speed}\n'
      f'Твоя текущая высота: {height}\nну что, ПОЕХАЛИ!\n===============================')

motion = 1
while not end_game:
    input_fuel = input("Сколько топлива сжечь? ")
    burnt_fuel, validation = check_input(input_fuel)

    if validation:

        height, speed, fuel = make_calculations(height, speed, fuel, burnt_fuel)

        print("Топлива сожжено: ", burnt_fuel, "кг")
        print("Топлива осталось: ", fuel, "кг")

        if speed < 0:
            print("Скорость взлёта: ", round(-speed, 3), "м/с")
        elif speed > 0:
            print("Скорость посадки: ", round(speed, 3), "м/с")
        else:
            print("Зависание")

        print("Текущая высота: ", round(height, 3), "м")
        print(f'Сейчас {motion} ход')
        print("===============================")

        motion += 1

        if check_flight_status(height, speed) == 1:
            print("Вы успешно посадили корабль!")
            print(f'Вы справились с задчей за {motion} шагов')
            end_game = True
        elif check_flight_status(height, speed) == -1:
            print("Космический модуль разбился!")
            end_game = True

input()
