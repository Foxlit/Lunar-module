# Main values
import random


def get_values_by_level(chosen_level):
    # Level 0 (test)
    if chosen_level == 0:
        fuel = 5000
        speed = 0
        height = 5
        g = 1.62
        mass = 8000
        k = 0.1
        portion_percentage = 5

    # Level 1
    elif chosen_level == 1:
        fuel = 5000
        speed = 0
        height = random.randint(1000, 1500)
        g = 1.62
        mass = 8000
        k = 0.1
        portion_percentage = 5

    # Level 2
    elif chosen_level == 2:
        fuel = 1500
        speed = 0
        height = random.randint(1000, 2000)
        g = 1.62
        mass = 15000
        k = 0.3
        portion_percentage = 5

    # Level 3
    else:
        fuel = 1000
        speed = 0
        height = random.randint(1000, 3000)
        g = 1.62
        mass = 20000
        k = 0.5
        portion_percentage = 5

    return fuel, speed, height, g, mass, k, portion_percentage
