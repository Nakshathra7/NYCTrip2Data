#gc trip_data_2.csv | select -first;  10
#head trip_data_2.csv

import csv, sys, datetime
from datetime import timedelta

fn = 'trip_data_2.csv'

'''
f = open(fn,'r')
n = 0
for line in f:
	n+=1
	if n % 100000 == 0:
		print(n)

print(n)
'''

f = open(fn,'r')
reader = csv.reader(f)

n = 0
all_pickuptimestamps = []
all_dropofftimestamps = []
all_passengercount = []
all_triptimeinsecs = []
all_tripdistance = []
all_pickupLatitude = []
all_pickupLongitude = []
all_dropoffLatitude = []
all_dropoffLongitude = []

resultFile = open('EveryThousandRows.csv', 'w')
resultFile.write('')
resultFile.close()

for row in reader:
	#Question-2 Starts
	if n < 1:
		print("Fieldnames in Given Data:\n", row)

	#Question-9 Starts
	if n % 100000 == 0:
		with open('EveryThousandRows.csv', 'a') as comFile:
		    writer = csv.writer(comFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		    #way to write to csv file
		    writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]])
		print(n)
	n += 1

	all_pickuptimestamps.append(row[5])
	all_dropofftimestamps.append(row[6])
	all_passengercount.append(row[7])
	all_triptimeinsecs.append(row[8])
	all_tripdistance.append(row[9])
	all_pickupLatitude.append(row[11])
	all_pickupLongitude.append(row[10])
	all_dropoffLatitude.append(row[13])
	all_dropoffLongitude.append(row[12])

all_pickuptimestamps.remove("pickup_datetime")
all_dropofftimestamps.remove("dropoff_datetime")
all_passengercount.remove("passenger_count")
all_triptimeinsecs.remove("trip_time_in_secs")
all_tripdistance.remove("trip_distance")
all_pickupLatitude.remove("pickup_latitude")
all_pickupLongitude.remove("pickup_longitude")
all_dropoffLatitude.remove("dropoff_latitude")
all_dropoffLongitude.remove("dropoff_longitude")

#Question-1 Starts
 
	# get min/max
pickupfinal = max(all_pickuptimestamps)   
pickupinitial = min(all_pickuptimestamps)

dropofffinal = max(all_dropofftimestamps)   
dropoffinitial = min(all_dropofftimestamps)

datetimeFormat = '%Y-%m-%d %H:%M:%S'
dateTimeDiff = datetime.datetime.strptime(dropofffinal, datetimeFormat) - datetime.datetime.strptime(pickupinitial, datetimeFormat)

print('Pickup Start time: ', pickupinitial)
print('Pickup End time:   ', pickupfinal)
print('Dropoff Start time: ', dropoffinitial)
print('Dropoff End time:   ', dropofffinal)

print("Difference:", dateTimeDiff)
print("Days:", dateTimeDiff.days)
print("Microseconds:", dateTimeDiff.microseconds)
print("Seconds:", dateTimeDiff.seconds)
print("Total Number of Records in Data: ", n)
print("Datetime Range Covered in Data:\nFrom: ", pickupinitial, "\nTo: ", dropofffinal, "\nAnd The Difference in Datetime is: ", dateTimeDiff)

#Question-5 Starts

pickupLatitudeFinal = max(all_pickupLatitude)
pickupLatitudeInitial = min(all_pickupLatitude)
print("Maximum Pickup Latitude: ", pickupLatitudeFinal)
print("Minimum Pickup Latitude: ", pickupLatitudeInitial)

pickupLongitudeFinal = max(all_pickupLongitude)
pickupLongitudeInitial = min(all_pickupLongitude)
print("Maximum Pickup Longitude: ", pickupLongitudeFinal)
print("Minimum Pickup Longitude: ", pickupLongitudeInitial)

dropoffLatitudeFinal = max(all_dropoffLatitude)
dropoffLatitudeInitial = min(all_dropoffLatitude)
print("Maximum Dropoff Latitude: ", dropoffLatitudeFinal)
print("Minimum Dropoff Latitude: ", dropoffLatitudeInitial)

dropoffLongitudeFinal = max(all_dropoffLongitude)
dropoffLongitudeInitial = min(all_dropoffLongitude)
print("Maximum Dropoff Longitude: ", dropoffLongitudeFinal)
print("Minimum Dropoff Longitude: ", dropoffLongitudeInitial)

with open('GeographicDetails.csv', 'a') as f:
    sys.stdout = f
    for value in sorted(all_pickupLatitude):
	    print(key)
    sys.stdout = original_stdout 

#Question-7 Starts

passengerCountFinal = max(all_passengercount)
passengerCountInitial = min(all_passengercount)
print("Maximum Passenger Count: ", passengerCountFinal)
print("Minimum Passenger Count: ", passengerCountInitial)

tripTimeInSecsFinal = max(all_triptimeinsecs)
tripTimeInSecsInitial = min(all_triptimeinsecs)
tripTimeInSecsDiff = tripTimeInSecsFinal - tripTimeInSecsInitial 
print("Maximum Trip Time in Secs: ", tripTimeInSecsFinal)
print("Minimum Trip Time in Secs: ", tripTimeInSecsInitial)

tripDistanceFinal = max(all_tripdistance)
tripDistanceInitial = min(all_tripdistance)
tripDistanceDiff = tripDistanceFinal - tripDistanceInitial
print("Maximum Trip Distance: ", tripDistanceFinal)
print("Minimum Trip Distance: ", tripDistanceInitial)

'''
	with open('GeographicDetails.csv', mode='w') as file:
	    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

	    #way to write to csv file
	    writer.writerow([row[11],row[10],row[13],row[12]])
'''

#Question-8 Starts






