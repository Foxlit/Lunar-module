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


fuel = 1000
speed = 0
height = 100000
g = 1.62
mass = 15000
burnt_fuel = 0
k = 15
validation = True
print(f' Добро Пожаловать в Lunar Module!\n Здесь тебе предстоит посадить космический модуль на луну!\n '
      f'Вот начальные данные, чтобы сориентироваться:\n Топливо:  {fuel}\n Твоя начальная скорость:  {speed}\n'
      f' Твоя текущая высота: {height}\n ну что, ПОЕХАЛИ!')

while height > 0:
    input_fuel = input(" Сколько топлива сжечь? ")
    burnt_fuel, validation = check_input(input_fuel)

    if validation:
        fuel -= burnt_fuel
        speed += (2 * g * height) ** 0.5 - burnt_fuel * k
        height -= speed * 60

# TODO: сделать расчет остатка топлива. Не должно быть отрицательного

        print("У вас нет столько топлива!")
        print("Топлива сожжено: ", round(burnt_fuel, 3), "кг")
        print("Топлива осталось: ", round(fuel, 3), "кг")
        if speed < 0:
            print("Скорость взлёта: ", round(-speed, 3), "м/с")
        elif speed > 0:
            print("Скорость посадки: ", round(speed, 3), "м/с")
        else:
            print("Зависание")
        print("Текущая высота: ", round(height, 3), "м")
        print("===============================")
        if height == 0:
            print("Вы успешно посадили корабль!")
        if height < 0:
            print("Космический модуль разбился!")
input()
