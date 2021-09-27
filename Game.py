def check_input(input_fuel):
    float_input = 0
    try:
        float_input = abs(float(input_fuel))
        if float(fuel) - float_input < 0:
            print("У вас нет столько топлива!")
            valid_result = False
        else:
            valid_result = True
    except ValueError:
        print("Некорректный ввод! Введите число")
        int_input = 0
        valid_result = False
    return float_input, valid_result


def control_remeing_fuel(fuel):
    if fuel < 0:
        return False


def check_flight_status(curr_height, curr_speed):
    if 0 > curr_height > (-30) and curr_speed < 5000:
        return 1
    elif curr_height < (-3):
        return -1
    else:
        return 0


def make_calculations(curr_height, curr_speed, curr_fuel):
    pass


fuel = 1000
speed = 0
height = 1000
g = 1.62
mass = 15000
burnt_fuel = 0
k = 0.1
validation = True
end_game = False


print(f' Добро Пожаловать в Lunar Module!\n Здесь тебе предстоит посадить космический модуль на луну!\n '
      f'Вот начальные данные, чтобы сориентироваться:\n Топливо:  {fuel}\n Твоя начальная скорость:  {speed}\n'
      f' Твоя текущая высота: {height}\n ну что, ПОЕХАЛИ!')

while not end_game:
    input_fuel = input(" Сколько топлива сжечь? ")
    burnt_fuel, validation = check_input(input_fuel)

    if validation:
        make_calculations(height,speed,fuel)
        fuel -= burnt_fuel
        speed += (2 * g * height) ** 0.5 - burnt_fuel * k
        height -= speed * 60

# TODO: сделать расчет остатка топлива. Не должно быть отрицательного

        print("Топлива сожжено: ", burnt_fuel, "кг")
        print("Топлива осталось: ", fuel, "кг")
        if speed < 0:
            print("Скорость взлёта: ", -speed, "м/с")
        elif speed > 0:
            print("Скорость посадки: ", speed, "м/с")
        else:
            print("Зависание")
        print("Текущая высота: ", height, "м")
        print("------------")
        if check_flight_status(height, speed) == 1:
            print("Вы успешно посадили корабль!")
            end_game = True
        elif check_flight_status(height, speed) == -1:
            print("Космический модуль разбился!")
            end_game = True

input()
