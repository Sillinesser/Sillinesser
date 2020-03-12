
import googlemaps        
import urllib.request
import json

def whatSpeed(a,b):

    marsh1 = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins='+a+'&destinations='+b+'&key=<API_KEY>'

    info_marsh1 = json.loads(urllib.request.urlopen(marsh1).read())      #результат запиту про маршрут з а1 до b1

    sec1 = info_marsh1['rows'][0]['elements'][0]['duration']['value']     #прогнозований час у секундах на проходження маршруту з а1 до b1

    dist1 = info_marsh1['rows'][0]['elements'][0]['distance']['value']     #дистанція між пунктами відправлення та прибуття

    return round(dist1/sec1, 3)    #повертаємо швидкість потоку машин
    
print(whatSpeed("lviv","Kyiv"))
