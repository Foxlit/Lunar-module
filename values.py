# Main values
def get_values_by_level(chosen_level):
    # Level 1
    if chosen_level == 1:
        fuel = 5000
        speed = 0
        height = 1000
        g = 1.62
        mass = 15000
        burnt_fuel = 0
        k = 0.1

    # Level 2
    if chosen_level == 2:
        fuel = 1000
        speed = 0
        height = 1000
        g = 1.62
        mass = 15000
        burnt_fuel = 0
        k = 0.1

    # Level 3
    if chosen_level == 3:
        fuel = 500
        speed = 0
        height = 1000
        g = 1.62
        mass = 15000
        burnt_fuel = 0
        k = 0.1

    return fuel, speed, height, g, mass, k

