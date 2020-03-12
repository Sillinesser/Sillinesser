import sv1
import sv2
import sv3
import sv4
import GoogleMapsAPI

a1 = '49.8636526,24.0337803'  #livo-pravo
a2 = '49.8651275,24.0505164'   #pravo-livo
a3 = '49.8671412,24.0436580'    #verh - nyz
a4 = '49.8659421,24.0441053'  # nyz - verh
b1 = '49.8651275,24.0505164'
b2 = '49.8649367,24.0404964'
b3 = '49.8624983,24.0437072'
b4 = '49.8639094,24.0439664'


speed1 = GoogleMapsAPI.whatSpeed(a1,b1)
speed2 = GoogleMapsAPI.whatSpeed(a2,b2)
speed3 = GoogleMapsAPI.whatSpeed(a3,b3)
speed4 = GoogleMapsAPI.whatSpeed(a4,b4)

print('speed1: ', speed1, 'km/hour')
print('speed2: ', speed2, 'km/hour')
print('speed3: ', speed3, 'km/hour')
print('speed4: ', speed4, 'km/hour')

sh = [speed1, speed2, speed3, speed4]

hs = sorted(sh)
print(hs[0])



if speed1 == speed2 == speed3 == speed4:
    red1=red2=red3=red4=0
    green1=green2=green3=green4=2

elif speed1>speed2 and speed1>speed3 and speed1>speed4:
    red1=red2=red3=red4=0
    green1=5
    green2=green3=green4=2
elif speed2>speed1 and speed2>speed3 and speed2>speed4:
    red1=red2=red3=0
    green2=5
    green1=green3=green4=2
elif speed3>speed1 and speed3>speed2 and speed3>speed4:
    red1=red2=red3=red4=0
    green3=5
    green1=green3=green4=2
elif speed4>speed1 and speed4>speed3 and speed4>speed3:
    red1=red2=red3=red4=0
    green4=5
    green1=green2=green3=2

else:
    red1 = 0
    red2 = 0
    red3 = 0
    red4 = 0
    green1 = 2
    green2 = 2
    green3 = 2
    green4 = 2






while True:
 sv1.sv1(red1,green1)
 sv2.sv1(red2,green2)
 sv3.sv1(red3,green3)
 sv4.sv1(red4,green4)
   


else:
    GPIO.cleanup()
    print("finished loop")
