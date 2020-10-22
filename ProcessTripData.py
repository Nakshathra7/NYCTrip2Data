#gc trip_data_2.csv | select -first;  10
#head trip_data_2.csv

import csv, sys, datetime
from collections import defaultdict

tripCSVFile = 'trip_data_2.csv'

'''
f = open(fn,'r')
n = 0
for line in f:
    n+=1
    if n % 100000 == 0:
        print(n)

print(n)
'''

tripFile = open(tripCSVFile,'r')
reader = csv.reader(tripFile)

n = 0

timeList = []
passengerList = []
rrTimeList = []
rrPassengerList = []

distVendorid = []
distRateCode = []
distStoreFwdFlag = []
distPassengerCount = []

all_pickuptimestamps = []
all_dropofftimestamps = []
all_passengercount = []
all_triptimeinsecs = []
all_tripdistance = []
all_pickupLatitude = []
all_pickupLongitude = []
all_dropoffLatitude = []
all_dropoffLongitude = []

all_pickuptimestampsSet = set()
all_dropofftimestampsSet = set()
all_passengercountSet = set()
all_triptimeinsecsSet = set()
all_tripdistanceSet = set()
all_pickupLatitudeSet = set()
all_pickupLongitudeSet = set()
all_dropoffLatitudeSet = set()
all_dropoffLongitudeSet = set()
hourTimeDict = defaultdict(list)
rrHourTimeDict = defaultdict(list)

result1000RowFile = open('EveryThousandRows.csv', 'w')
result1000RowFile.write('')
result1000RowFile.close()

avgPassengerCountFile = open('AvgPassengerCount.csv', 'w')
avgPassengerCountFile.write('')
avgPassengerCountFile.close()

rravgPassengerCountFile = open('RRAvgPassengerCount.csv', 'w')
rravgPassengerCountFile.write('')
rravgPassengerCountFile.close()

for header in reader:
    #Question-2 Starts
    if n < 1:
        print("\nQuestion-2: Fieldnames in Given Data:\n\n", header)
        break

print("\nProcessing Trip Data ...\n")

with open(tripCSVFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    next(csvreader)

    with open('EveryThousandRows.csv', 'a') as comFile:
        writer = csv.writer(comFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in csvreader:    
            timeList = (row[5].split(" ")[-1].split(":"))
            hourTimeDict[int(timeList[0])].append(int(row[7]))

            if row[2] not in distVendorid:
                distVendorid.append(row[2])

            if row[3] not in distRateCode:
                distRateCode.append(row[3])

            if row[4] not in distStoreFwdFlag:
                distStoreFwdFlag.append(row[4])

            if row[7] not in distPassengerCount:
                distPassengerCount.append(row[7])

            #Question-9 Starts
            
            if n % 100000 == 0:
                #way to write to csv file
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]])
            
            n += 1

            all_pickuptimestampsSet.add(row[5])
            all_dropofftimestampsSet.add(row[6])
            all_passengercountSet.add(row[7])
            all_triptimeinsecsSet.add(row[8])
            all_tripdistanceSet.add(row[9])
            all_pickupLatitudeSet.add(row[11])
            all_pickupLongitudeSet.add(row[10])
            all_dropoffLatitudeSet.add(row[13])
            all_dropoffLongitudeSet.add(row[12])

all_pickuptimestamps = list(all_pickuptimestampsSet)
all_dropofftimestamps = list(all_dropofftimestampsSet)
all_passengercount = list(all_passengercountSet)
all_triptimeinsecs = list(all_triptimeinsecsSet)
all_tripdistance = list(all_tripdistanceSet)
all_pickupLatitude = list(all_pickupLatitudeSet)
all_pickupLongitude = list(all_pickupLongitudeSet)
all_dropoffLatitude = list(all_dropoffLatitudeSet)
all_dropoffLongitude = list(all_dropoffLongitudeSet)

all_pickuptimestamps.sort()
all_dropofftimestamps.sort()
all_passengercount.sort()
all_triptimeinsecs.sort()
all_tripdistance.sort()
all_pickupLatitude.sort()
all_pickupLongitude.sort()
all_dropoffLatitude.sort()
all_dropoffLongitude.sort()

#Question-1 Starts

# get min/max
print("\nQuestion-1: DateTime Range & Total Records in Data\n\n")
pickupTimestampLen = len(all_pickuptimestamps)
dropoffTimestampLen = len(all_dropofftimestamps)

datetimeFormat = '%Y-%m-%d %H:%M:%S'
dateTimeDiff = datetime.datetime.strptime(all_dropofftimestamps[dropoffTimestampLen-1], datetimeFormat) - datetime.datetime.strptime(all_pickuptimestamps[0], datetimeFormat)

print('Pickup Start time: ', all_pickuptimestamps[0])
print('Pickup End time:   ', all_pickuptimestamps[pickupTimestampLen-1])
print('Dropoff Start time: ', all_dropofftimestamps[0])
print('Dropoff End time:   ', all_dropofftimestamps[dropoffTimestampLen-1])

print("Difference:", dateTimeDiff)
print("Days:", dateTimeDiff.days)
print("Microseconds:", dateTimeDiff.microseconds)
print("Seconds:", dateTimeDiff.seconds)
print("\nTotal Number of Records in Data: ", n)
print("Datetime Range Covered in Data:\nFrom: ", all_pickuptimestamps[0], "\nTo: ", all_dropofftimestamps[dropoffTimestampLen-1], "\nAnd The Difference in Datetime is: ", dateTimeDiff)

#Question-5 Starts
print("\nQuestion-5: Geographic Range of Data\n\n")
pickupLatitudeLen = len(all_pickupLatitude)
print("Maximum Pickup Latitude: ", all_pickupLatitude[pickupLatitudeLen-1])
print("Minimum Pickup Latitude: ", all_pickupLatitude[0])

pickupLongitudeLen = len(all_pickupLongitude)
print("Maximum Pickup Longitude: ", all_pickupLongitude[pickupLongitudeLen-1])
print("Minimum Pickup Longitude: ", all_pickupLongitude[0])

dropoffLatitudeLen = len(all_dropoffLatitude)
print("\nMaximum Dropoff Latitude: ", all_dropoffLatitude[dropoffLatitudeLen-1])
if (all_dropoffLatitude[0] == ' ' or all_dropoffLatitude[0] == ''):
    print("Minimum Dropoff Latitude: ", all_dropoffLatitude[1])
else:
    print("Minimum Dropoff Latitude: ", all_dropoffLatitude[0])

dropoffLongitudeLen = len(all_dropoffLongitude)
print("Maximum Dropoff Longitude: ", all_dropoffLongitude[dropoffLongitudeLen-1])
if (all_dropoffLongitude[0] == ' ' or all_dropoffLongitude[0] == ''):
    print("Minimum Dropoff Longitude: ", all_dropoffLongitude[1])
else:
    print("Minimum Dropoff Longitude: ", all_dropoffLongitude[0])

#Question-6 Starts
print("\nQuestion-6: Distinct Values\n\n")
print("Distinct Vendor Id: ", distVendorid)
#print("Distinct Rate Code: ", distRateCode)
print("Distinct Store And Forward Flag: ", distStoreFwdFlag)
#print("Distinct Passenger Count: ", distPassengerCount)

#Question-7 Starts
print("\nQuestion-7: Min & Max Numeric Fields\n\n")
passengerCountLen = len(all_passengercount)
print("Maximum Passenger Count: ", all_passengercount[passengerCountLen-1])
print("Minimum Passenger Count: ", all_passengercount[0])

tripTimeInSecsLen = len(all_triptimeinsecs)
print("\nMaximum Trip Time in Secs: ", all_triptimeinsecs[tripTimeInSecsLen-1])
print("Minimum Trip Time in Secs: ", all_triptimeinsecs[0])

tripDistanceLen = len(all_tripdistance)
print("\nMaximum Trip Distance: ", all_tripdistance[tripDistanceLen-1])
print("Minimum Trip Distance: ", all_tripdistance[0])

#Question-8 Starts

with open('AvgPassengerCount.csv', 'a') as avgFile:
    writer = csv.writer(avgFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Hours","AvgPassengerCount"])
    for key, value in sorted(hourTimeDict.items()):
        average = sum(value)/(dateTimeDiff.days)
        writer.writerow([key,average])


#Question-10 Starts

with open('EveryThousandRows.csv', 'r') as csvReducedRowFile:
    csvReducedRowReader = csv.reader(csvReducedRowFile)

    # This skips the first row of the CSV file.
    next(csvReducedRowReader)

    for row in csvReducedRowReader:
        rrTimeList = (row[5].split(" ")[-1].split(":"))
        rrPassengerList.append(row[7])
        rrHourTimeDict[int(rrTimeList[0])].append(int(row[7]))

with open('RRAvgPassengerCount.csv', 'a') as avgFile:
    writer = csv.writer(avgFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["RRHours","RRAvgPassengerCount"])
    for key, value in sorted(rrHourTimeDict.items()):
        rrAverage = sum(value)/(dateTimeDiff.days)
        writer.writerow([key,rrAverage])


