# Main values
def get_values_by_level(chosen_level):
    # Level 1
    if chosen_level == 1:
        fuel = 5000
        speed = 0
        height = 1000
        g = 1.62
        mass = 8000
        k = 0.1

    # Level 2
    elif chosen_level == 2:
        fuel = 1500
        speed = 0
        height = 1000
        g = 1.62
        mass = 15000
        k = 0.3

    # Level 3
    else:
        fuel = 1000
        speed = 0
        height = 1000
        g = 1.62
        mass = 20000
        k = 0.5

    return fuel, speed, height, g, mass, k
