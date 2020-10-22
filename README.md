# IA 626: Big Data Processing & Cloud Services -  Project Documentation

## Project Title : 

#### Big Data Inspection - NYC Taxi Trips-2
 
## Project Description:

##### The main purpose of this project is to analyze the dataset which contains information about taxi rides in NYC and perform verious operations to understand the data.

## Question-1: DateTime Range & Total Records in Data

##### There were 2 datetime fields in given data. One is pickup timestamp and other one is dropoff timestamp. First, I found the minimum and maximum timestamp value for each field separately. Then, I took the difference between maximum dropoff timestamp and minimum pickup timestamp to get the total number of days in between these two timestamps. The result are as follows,

* **Pickup Start time:**  2013-02-01 00:00:00
* **Pickup End time:**   2013-02-28 23:59:59
* **Dropoff Start time:**  2013-02-01 00:00:55
* **Dropoff End time:**   2013-03-01 01:15:48

* **Difference:** 28 days, 1:15:48
* **Days:** 28
* **Microseconds:** 0
* **Seconds:** 4548

#### Total Number of Records in Given Data:  **_13990176_**

#### Datetime Range Covered in Data:
**_From:  2013-02-01 00:00:00_**
**_To:  2013-03-01 01:15:48_**
And The Difference in Datetime is: **_28 days, 1:15:48_**


## Question-2: Fieldnames & their Descriptions

#### Fieldnames in Given Data:

* **'medallion':** Encrypted Form of Registered Taxi Cab  
* **'hack_license':** Encrypted Form of License Number 
* **'vendor_id':** Vendor ID of Registered Taxis 
* **'rate_code':** Rate Code for Taxi Trips 
* **'store_and_fwd_flag':** Trip Indicator Flag 
* **'pickup_datetime':** Timestamp at the Time of Trip Pickup 
* **'dropoff_datetime':** Timestamp at the Time of Trip Dropoff 
* **'passenger_count':** Number of Passengers At the time of Pickup During Taxi Trip 
* **'trip_time_in_secs':** Total Time Taken for the Trip, Measured in Seconds 
* **'trip_distance':** Total Distance Covered During the Trip 
* **'pickup_longitude':** Longitude Position at the Time of Trip Pickup 
* **'pickup_latitude':** Latitude Position at the Time of Trip Pickup  
* **'dropoff_longitude':** Longitude Position at the Time of Trip Dropoff 
* **'dropoff_latitude':** Latitude Position at the Time of Trip Dropoff 

## Question-3: Sample Data for Each Field

| medallion | hack_license | vendor_id | rate_code | store_and_fwd_flag | pickup_datetime | dropoff_datetime | passenger_count | trip_time_in_secs | trip_distance | pickup_longitude | pickup_latitude | dropoff_longitude | dropoff_latitude |
| ----- | ------------- |------------- | ----- | ------------- |------------- | ----- | ------------- |------------- | ----- | ------------- |------------- | ----- | ------------- |
| 1B5C0970F2AE8CFFBA8AE4584BEAED29 | D961332334524990D1BBD462E2EFB8A4  | CMT | 1 | N | 2/8/2013  11:35:00 PM | 2/8/2013  11:42:00 PM | 1 | 463 | 0.8 | -73.992439 | 40.724487 | -73.984421 | 40.718903 |
| B42249AE16E2B8E556F1CB1F940D6FB4 | D4BB308D1F3FCB3434D9DB282CDC93D7 | CMT | 1 | N | 2/7/2013  12:20:00 PM | 2/7/2013  12:50:00 PM | 4 | 1810 | 3.1 | -73.989494 | 40.769588 | -73.990303 | 40.737347 |
| 890699222C47C09FBC898758CEC69762 | 6318C3AEC02248928C3345B5805EB905 | CMT | 1 | N | 2/8/2013  8:56:00 AM | 2/8/2013  8:59:00 AM | 1 | 168 | 1 | -73.963036 | 40.799141 | -73.972168 | 40.786446 |


## Question-4: MySQL Data types and Length to Store Each Field

| Fieldnames  | DataType With Length |
| ----- | ------------- |
| medallion | VARCHAR(100)  |
| hack_license | VARCHAR(100) |
| vendor_id | VARCHAR(5) |
| rate_code | INT(5) |
| store_and_fwd_flag | VARCHAR(1) |
| pickup_datetime | DATETIME |
| dropoff_datetime | DATETIME |
| passenger_count | INT(1) |
| trip_time_in_secs | INT(4) |
| trip_distance | DECIMAL(3,2) |
| pickup_longitude | DECIMAL(9,6) |
| pickup_latitude | DECIMAL(8,6) |
| dropoff_longitude | DECIMAL(9,6) |
| dropoff_latitude | DECIMAL(8,6) |


## Question-5: Geographic Range of the Data

##### For calculating the minimum and maximum latitude and longitude geographic range, I used list to get the min and max data points. To remove the outliers in data, I sorted the list in ascending order and took the minimum value at the index position **_'10000'_** from left and maximum value at the index position **_'10000'_** from right. This helped to get the range of values for pickup and dropoff latitude and longitude. The sample code is as follows,

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

* **Maximum Pickup Latitude:**  40.82988
* **Minimum Pickup Latitude:**  40.660435
* **Maximum Pickup Longitude:**  -73.995476
* **Minimum Pickup Longitude:**  -73.833504

* **Maximum Dropoff Latitude:**  40.877312
* **Minimum Dropoff Latitude:**  40.614243
* **Maximum Dropoff Longitude:**  -74.038765
* **Minimum Dropoff Longitude:**  -73.759254

##### The below screenshot shows the geographic range of NYC trip dataset.

![GitHub Logo](/images/GeographicRange.png)

## Question-6: Distinct Values of the Field

##### From the given data, I found the distinct value for 2 fields which has discrete values. Rest all field values are continuous and didn't have distinct values to extract. The sample code for finding distinct values are as follows,

    if row[2] not in distVendorid:
        distVendorid.append(row[2])
    if row[4] not in distStoreFwdFlag:
        distStoreFwdFlag.append(row[4])

* **Distinct Vendor Id:**  ['CMT', 'VTS']
* **Distinct Store And Forward Flag:**  ['N', 'Y', '']

## Question-7: Min & Max Values of Numeric Fields

###### Besides Latitude & Longitude fields, the data contains few other numeric datatype fields which are listed below and the minimum and maximum values of those fields are as follows.

* **Maximum Passenger Count:**  9
* **Minimum Passenger Count:**  0

* **Maximum Trip Time in Secs:**  999
* **Minimum Trip Time in Secs:**  0

* **Maximum Trip Distance:**  99.70
* **Minimum Trip Distance:**  .00

## Question-8: Chart to Show the Average Number of Passengers Each Hour of the Day.

To get the average number of passengers each hour of the day, I used dictionary to store hour as key and number of passenger count as value. The sample code is as follows,

    timeList = (row[5].split(" ")[-1].split(":"))
    hourTimeDict[int(timeList[0])].append(int(row[7]))

Then I stored the average computation result in separate CSV file which contains hour and average passenger count as follows,

    with open('generatedFiles/AvgPassengerCount.csv', 'a') as avgFile:
        writer = csv.writer(avgFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Hours","AvgPassengerCount"])
        for key, value in sorted(hourTimeDict.items()):
            average = sum(value)/(dateTimeDiff.days)
            writer.writerow([key,average])

### Average Number of Passengers Vs Hour for All Records in Given Data

##### The graph shows that the average passenger count is increasing with respect to hours. And tha maximum point is reached between 6PM to 8PM. Whereas the minimum passenger count with respect to hour is seen at 5AM after which there is an increase in average count across hours.

![GitHub Logo](/images/AvgPassengerCount.png)

## Question-9: New CSV File Which Has Only One Out of Every Thousand Rows.

##### The new CSV file has been generated to store the every thousand row from the given data. And the **_"EveryThousandRows.csv"_** file is included inside the "generatedFiles" folder during execution. The code for the same is as follows,

    with open('generatedFiles/EveryThousandRows.csv', 'a') as comFile:
        writer = csv.writer(comFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if n % 100000 == 0:
            #write to csv file
            writer.writerow([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13]])

## Question-10: Compare Charts From Normal Dataset and Reduced Row From Q-9 Dataset.

##### The new CSV file has been generated from the reduced rows dataset to store the hour and average number of passenger details . And the **_"RRAvgPassengerCount.csv"_** file is included inside the "generatedFiles" folder during execution. The code for the same is as follows,

    with open('generatedFiles/RRAvgPassengerCount.csv', 'a') as avgFile:
        writer = csv.writer(avgFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["RRHours","RRAvgPassengerCount"])
        for key, value in sorted(rrHourTimeDict.items()):
            rrAverage = sum(value)/(dateTimeDiff.days)
            writer.writerow([key,rrAverage])

##### From the reduced rows dataset, the graph is generated between hours and average number of passengers. The graph clearly shows, that the average number passenger count fluctuates between hours. And this is not similar to normal dataset graph. The only common factor between these two graphs are the average number of passenger count attains the peak value at the hour 6PM.

### Average Number of Passengers for Reduced Row Vs Hour for All Records in Reduced Data

![GitHub Logo](/images/RRAvgPassengerCount.png)

## Console Output

##### The below screenshot shows the console output during execution of NYC trip dataset.

![GitHub Logo](/images/Console_Output_SS.png)
