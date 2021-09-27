def check_input(input_fuel):
    try:
        int_input = abs(float(input_fuel))
        valid_result = True
    except ValueError:
        print("Некорректный ввод! Введите число")
        int_input = 0
        valid_result = False
    return int_input, valid_result


fuel = 1000
speed = 0
height = 100000
g = 1.62
mass = 15000
burnt_fuel = 0
k = 15
validation = True
while height > 0:
    input_fuel = input("Сколько топлива сжечь? ")
    burnt_fuel, validation = check_input(input_fuel)
    if validation:
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
        if height == 0:
            print("Вы успешно посадили корабль!")
        if height < 0:
            print("Космический модуль разбился!")
input()
