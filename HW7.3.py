def solution(number):
    sum = 0
    while number > 0:
        number -= 1
        if number % 5 == 0:
            sum += number
        elif number % 3 == 0:
            sum += number
    return sum


solution(12)