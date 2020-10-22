import csv, sys, time, datetime
from collections import defaultdict

#Accessing NYC Taxi Trip CSV Dataset
tripCSVFile = 'trip_data_2.csv'
tripFile = open(tripCSVFile,'r')
reader = csv.reader(tripFile)

#Variable Declarations
n = 0

timeList = []
passengerList = []
rrTimeList = []
rrPassengerList = []

distVendorid = []
distStoreFwdFlag = []

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
distVendoridSet = set()
distStoreFwdFlagSet = set()
hourTimeDict = defaultdict(list)
rrHourTimeDict = defaultdict(list)

#Clearing the CSV files Before Execution
result1000RowFile = open('generatedFiles/EveryThousandRows.csv', 'w')
result1000RowFile.write('')
result1000RowFile.close()

avgPassengerCountFile = open('generatedFiles/AvgPassengerCount.csv', 'w')
avgPassengerCountFile.write('')
avgPassengerCountFile.close()

rravgPassengerCountFile = open('generatedFiles/RRAvgPassengerCount.csv', 'w')
rravgPassengerCountFile.write('')
rravgPassengerCountFile.close()

for header in reader:
    start = time.time()

    #Question-2 Starts
    if n < 1:
        print("\nQuestion-2: Fieldnames in Given Data:\n\n", header)
        break

print("\nProcessing Trip Data ...\n")

with open(tripCSVFile, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # This skips the first row of the CSV file.
    next(csvreader)

    with open('generatedFiles/EveryThousandRows.csv', 'a') as comFile:
        writer = csv.writer(comFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for row in csvreader:    
            timeList = (row[5].split(" ")[-1].split(":"))
            hourTimeDict[int(timeList[0])].append(int(row[7]))

            #Checking for Distinct Values
            if row[2] not in distVendorid:
                distVendoridSet.add(row[2])

            if row[4] not in distStoreFwdFlag:
                distStoreFwdFlagSet.add(row[4])

            #Question-9 Starts
            
            if n % 100000 == 0:
                #write to csv file
                writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]])
            
            n += 1

            #Adding the CSV Filtered Data into Set Data Structure - Set executes faster compare to List

            all_pickuptimestampsSet.add(row[5])
            all_dropofftimestampsSet.add(row[6])
            all_passengercountSet.add(row[7])
            all_triptimeinsecsSet.add(row[8])
            all_tripdistanceSet.add(row[9])
            all_pickupLatitudeSet.add(row[11])
            all_pickupLongitudeSet.add(row[10])
            all_dropoffLatitudeSet.add(row[13])
            all_dropoffLongitudeSet.add(row[12])

#After Assigning All Data to Set, Moving them to List For Manipulation
all_pickuptimestamps = list(all_pickuptimestampsSet)
all_dropofftimestamps = list(all_dropofftimestampsSet)
all_passengercount = list(all_passengercountSet)
all_triptimeinsecs = list(all_triptimeinsecsSet)
all_tripdistance = list(all_tripdistanceSet)
all_pickupLatitude = list(all_pickupLatitudeSet)
all_pickupLongitude = list(all_pickupLongitudeSet)
all_dropoffLatitude = list(all_dropoffLatitudeSet)
all_dropoffLongitude = list(all_dropoffLongitudeSet)
distVendorid = list(distVendoridSet)
distStoreFwdFlag = list(distStoreFwdFlagSet)

#Sorting the List Elements and Storing Back to Same List
all_pickuptimestamps.sort()
all_dropofftimestamps.sort()
all_passengercount.sort()
all_triptimeinsecs.sort()
all_tripdistance.sort()
all_pickupLatitude.sort()
all_pickupLongitude.sort()
all_dropoffLatitude.sort()
all_dropoffLongitude.sort()
distVendorid.sort()
distStoreFwdFlag.sort()

#Question-1 Starts

#Getting Minimum & Maximum Values
print("\nQuestion-1: DateTime Range & Total Records in Data\n\n")

pickupTimestampLen = len(all_pickuptimestamps)
dropoffTimestampLen = len(all_dropofftimestamps)

#Using DataTime to Calculate the Difference Between Two Timestamps
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

#Calculating Minimum & Maximum Latitude and Longitude Values For Pickup and Dropoff Fields
#To Remove Outliers - Getting Minimum Value at the Index Position '10000' From Left And Maximum Value At The Index Position '10000' From Right. 

pickupLatitudeLen = len(all_pickupLatitude)
if (all_pickupLatitude[pickupLatitudeLen-1] == ' ' or all_pickupLatitude[pickupLatitudeLen-1] == '' or all_pickupLatitude[pickupLatitudeLen-1] == 0):
    print("Maximum Pickup Latitude: ", all_pickupLatitude[pickupLatitudeLen-10000])
else:
    print("Maximum Pickup Latitude: ", all_pickupLatitude[pickupLatitudeLen-10000])

if (all_pickupLatitude[0] == ' ' or all_pickupLatitude[0] == '' or all_pickupLatitude[0] == 0):
    print("Minimum Pickup Latitude: ", all_pickupLatitude[10000])
else:
    print("Minimum Pickup Latitude: ", all_pickupLatitude[10000])

pickupLongitudeLen = len(all_pickupLongitude)
if (all_pickupLongitude[pickupLongitudeLen-1] == ' ' or all_pickupLongitude[pickupLongitudeLen-1] == '' or all_pickupLongitude[pickupLongitudeLen-1] == 0):
    print("Maximum Pickup Longitude: ", all_pickupLongitude[pickupLongitudeLen-10000])
else:
    print("Maximum Pickup Longitude: ", all_pickupLongitude[pickupLongitudeLen-10000])

if (all_pickupLongitude[0] == ' ' or all_pickupLongitude[0] == '' or all_pickupLongitude[0] == 0):
    print("Minimum Pickup Longitude: ", all_pickupLongitude[10000])
else:
    print("Minimum Pickup Longitude: ", all_pickupLongitude[10000])

dropoffLatitudeLen = len(all_dropoffLatitude)
if (all_dropoffLatitude[dropoffLatitudeLen-1] == ' ' or all_dropoffLatitude[dropoffLatitudeLen-1] == '' or all_dropoffLatitude[dropoffLatitudeLen-1] == 0):
    print("\nMaximum Dropoff Latitude: ", all_dropoffLatitude[dropoffLatitudeLen-10000])
else: 
    print("\nMaximum Dropoff Latitude: ", all_dropoffLatitude[dropoffLatitudeLen-10000])

if (all_dropoffLatitude[0] == ' ' or all_dropoffLatitude[0] == '' or all_dropoffLatitude[0] == 0):
    print("Minimum Dropoff Latitude: ", all_dropoffLatitude[10000])
else:
    print("Minimum Dropoff Latitude: ", all_dropoffLatitude[10000])

dropoffLongitudeLen = len(all_dropoffLongitude)
if (all_dropoffLongitude[dropoffLongitudeLen-1] == ' ' or all_dropoffLongitude[dropoffLongitudeLen-1] == '' or all_dropoffLongitude[dropoffLongitudeLen-1] == 0):
    print("Maximum Dropoff Longitude: ", all_dropoffLongitude[dropoffLongitudeLen-10000])
else:
    print("Maximum Dropoff Longitude: ", all_dropoffLongitude[dropoffLongitudeLen-10000])

if (all_dropoffLongitude[0] == ' ' or all_dropoffLongitude[0] == '' or all_dropoffLongitude[0] == 0):
    print("Minimum Dropoff Longitude: ", all_dropoffLongitude[10000])
else:
    print("Minimum Dropoff Longitude: ", all_dropoffLongitude[10000])

#Question-6 Starts
#Getting Distinct Values of Fields

print("\nQuestion-6: Distinct Values\n\n")
print("Distinct Vendor Id: ", distVendorid)
print("Distinct Store And Forward Flag: ", distStoreFwdFlag)

#Question-7 Starts
#Getting Minimum & Maximum Values For Numeric Fields

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
#Generating New CSV File to Load Hour and Average Passenger Count For all Records in Given Dataset

with open('generatedFiles/AvgPassengerCount.csv', 'a') as avgFile:
    writer = csv.writer(avgFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Hours","AvgPassengerCount"])
    for key, value in sorted(hourTimeDict.items()):
        average = sum(value)/(dateTimeDiff.days)
        writer.writerow([key,average])

print("\nGenerated AvgPassengerCount.csv File")

#Question-10 Starts
#Reading CSV File Which Contains Data of Every Thousand Rows From Given Dataset

with open('generatedFiles/EveryThousandRows.csv', 'r') as csvReducedRowFile:
    csvReducedRowReader = csv.reader(csvReducedRowFile)

    # This skips the first row of the CSV file.
    next(csvReducedRowReader)

    for row in csvReducedRowReader:
        rrTimeList = (row[5].split(" ")[-1].split(":"))
        rrPassengerList.append(row[7])
        rrHourTimeDict[int(rrTimeList[0])].append(int(row[7]))

#Generating New CSV File to Load Hour and Average Passenger Count For Reduced Records From EveryThousandRows.csv

with open('generatedFiles/RRAvgPassengerCount.csv', 'a') as avgFile:
    writer = csv.writer(avgFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["RRHours","RRAvgPassengerCount"])
    for key, value in sorted(rrHourTimeDict.items()):
        rrAverage = sum(value)/(dateTimeDiff.days)
        writer.writerow([key,rrAverage])

print("Generated RRAvgPassengerCount.csv File")
print ("\nTotal Time Taken for Execution: " + str(time.time() - start))
print("\n")
