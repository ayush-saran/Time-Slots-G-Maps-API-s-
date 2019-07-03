import googlemaps
from datetime import datetime

map = googlemaps.Client(key='AIzaSyBElZh6cYTLtMjfRvGJRqbxcbhSLFbcf7M')

print("Flight Details:- ")
print("Departure Time from Bangalore - 21:05:00.000000")
print("Arrival Time at Mumbai - 23:30:00.000000")


dep_t = '2019-08-25 19:05:00.000000'
arr_t = '2019-08-26 00:30:00.000000'

#Flight departs at 10:05 and arrives at 12:30

dep_time = datetime.strptime(dep_t,'%Y-%m-%d %H:%M:%S.%f')
arr_time = datetime.strptime(arr_t,'%Y-%m-%d %H:%M:%S.%f')

#Let the city of departure be Bangalore and arrival be Mumbai.

#Let the pickup and dropoff points in Bangalore and Mumbai be predefined

city1 = map.directions("Sobha Dahlia","Kempegowda International Airport",mode="driving",departure_time=dep_time)
airport1 = city1[0]['legs'][0]['duration']['value']

city2 = map.directions("Mumbai Airport","Bandra",mode="driving",departure_time = arr_time)
airport2 = city2[0]['legs'][0]['duration']['value']

drop_hrs = (int)(airport2/3600)
drop_mins = (int)((airport2-(drop_hrs*3600))/60)

pick_hrs = (int)(airport1/3600)
pick_mins = (int)((airport1-(pick_hrs*3600))/60)

# Summing to get time in 24hrs format for when the luggage will reach the destination
drop_hour = drop_hrs + arr_time.hour
drop_minute = drop_mins + arr_time.minute

if(drop_minute>60):
    drop_minute = drop_minute - 60
    drop_hour+=1

pick_hour = dep_time.hour - pick_hrs
pick_minute = dep_time.minute - pick_mins

if pick_minute<0:
    pick_minute = pick_minute+60
    pick_hour-=1

if pick_minute<15:
    pick_hour-=1

if drop_minute>45:
    drop_hour+=1

if pick_hour<0 :
    pick_hour = 24 + pick_hour

if drop_hour>24:
    drop_hour = drop_hour - 24



if drop_hour>=0 and drop_hour<=6:
    drop_hour+=6

if drop_hour>=21 and drop_hour<=23:
    drop_hour+=9
    drop_hour = drop_hour-24

if pick_hour>=0 and pick_hour<=9:
    pick_hour -=9
    pick_hour = 24+pick_hour


#second slot



drop_hour2 = drop_hour + 3
pick_hour2 = pick_hour - 3

if drop_hour2 >= 0 and drop_hour2 <= 6:
    drop_hour2 += 6

if drop_hour2 >= 21 and drop_hour2 <= 23:
    drop_hour2 += 9
    drop_hour2 = drop_hour2 - 24

if pick_hour2 >= 0 and pick_hour2 <= 9:
    pick_hour2 -= 9
    pick_hour2 = 24 + pick_hour2


print("\nThe Luggage will be picked between " + str(pick_hour-3) + " hours to " + str(pick_hour) + " hours from Dahlia")
print("The Luggage will be picked between " + str(pick_hour2 - 3) + " hours to " + str(pick_hour2) + " hours from Dahlia\n")

print("The Luggage will be dropped between " + str(drop_hour) + " hours to " + str(drop_hour+3) + " hours IST at Bandra (dropoff)")
print("The Luggage will be dropped between " + str(drop_hour2) + " hours to " + str(drop_hour2 + 3) + " hours IST at Bandra (dropoff)")

