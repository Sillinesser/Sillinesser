# import pyowm



# place = str(input('Введіть місцезнаходження'))




# owm = pyowm.OWM('ef2206ff5da67de63306d0b143e20872')  # You MUST provide a valid API key

# # Have a pro subscription? Then use:
# # owm = pyowm.OWM(API_key='your-API-key', subscription_type='pro')

# # Search for current weather in London (Great Britain)
# observation = owm.weather_at_place(place)
# w = observation.get_weather()
# #print(w)                      # <Weather - reference time=2013-12-18 09:20,
#                               # status=Clouds>
# print('Швидкість вітру', w.get_wind()['speed'], 'м/с',  )
# # Weather details
# w.get_wind()                  # {'speed': 4.6, 'deg': 330}
# w.get_humidity()              # 87
# w.get_temperature('celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

# # Search current weather observations in the surroundings of
# # lat=22.57W, lon=43.12S (Rio de Janeiro, BR)
# observation_list = owm.weather_around_coords(-22.57, -43.12)


#     # 1.  Напишіть скрипт-гру, яка генерує випадковим чином число з діапазону чисе.....
# from random import randint as R

# x = R(0,100)
# print(x)
# def sche():
#     n = int(input("Вгадайте число"))
#     while n < 100:
#         if n == x:
#             print('Ви вгадали')
#             break
#         elif n <= x:
#             print('x більше')
#             return sche()
#         else:
#             print("x менше")
#             return sche()

# sche()

    #2.  Напишіть скрипт, який обчислює площу прямокутника a*b, площ....
# from math import pow
# from math import pi

# def pr():
#     a = float(input('Введіть довжину однієї сторони:'))
#     b = float(input('Введіть довжину другої сторони:'))
#     print('площа прямокутника:', a*b, 'периметр:', a*2+b*2)

# def tr():
#     t1 = float(input('Введіть довжину однієї сторони:'))
#     h1 = float(input('Висоту, опущену на третю сторону:'))
#     print("Площа трикутника:", 0.5*t1*h1)

# def kr():
#     r = float(input('Введи радіус круга:'))
#     print('Площа круга:', pi*pow(r,2))


# print('Введіть: Площа прямокутника - 1/Площа круга - 2/Площа трикутника - 3')
# n = input()

# if n == "1":
#     pr()
# elif n == "2":
#     tr()
# elif n == "3":
#     kr()
# else:
#     print("не розумію(")
