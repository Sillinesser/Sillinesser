def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump > fuel_left * mpg:
        return False
    else:
        return True
print (zero_fuel(50, 25, 2))