# IA 626: Big Data Processing & Cloud Services -  Project Documentation

## Project Title : 

#### Big Data Inspection - NYC Taxi Trips-2
 
## Project Description:

##### The main purpose of this project is to analyze the dataset which contains information about taxi rides in NYC and perform verious operations to understand the data.

## Question-1: DateTime Range & Total Records in Data

* Pickup Start time:  2013-02-01 00:00:00
* Pickup End time:    2013-02-28 23:59:59
* Dropoff Start time:  2013-02-01 00:00:55
* Dropoff End time:    2013-03-01 01:15:48

* Difference: 28 days, 1:15:48
* Days: 28
* Microseconds: 0
* Seconds: 4548

#### Total Number of Records in Given Data:  13990176

#### Datetime Range Covered in Data:
From:  2013-02-01 00:00:00 
To:  2013-03-01 01:15:48 
And The Difference in Datetime is:  28 days, 1:15:48


## Question-2: Fieldnames & their Descriptions

#### Fieldnames in Given Data:

* 'medallion': Encrypted Form of Registered Taxi Cab  
* 'hack_license': Encrypted Form of License Number 
* 'vendor_id': Vendor ID of Registered Taxis 
* 'rate_code': Rate Code for Taxi Trips 
* 'store_and_fwd_flag': Trip Indicator Flag 
* 'pickup_datetime': Timestamp at the Time of Trip Pickup 
* 'dropoff_datetime': Timestamp at the Time of Trip Dropoff 
* 'passenger_count': Number of Passengers At the time of Pickup During Taxi Trip 
* 'trip_time_in_secs': Total Time Taken for the Trip, Measured in Seconds 
* 'trip_distance': Total Distance Covered During the Trip 
* 'pickup_longitude': Longitude Position at the Time of Trip Pickup 
* 'pickup_latitude': Latitude Position at the Time of Trip Pickup  
* 'dropoff_longitude': Longitude Position at the Time of Trip Dropoff 
* 'dropoff_latitude': Latitude Position at the Time of Trip Dropoff 

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

* Maximum Pickup Latitude:  96.685364
* Minimum Pickup Latitude:  -0.000042
* Maximum Pickup Longitude:  9.0799999E-4
* Minimum Pickup Longitude:  -0.000002

* Maximum Dropoff Latitude:  9.8999997E-4
* Minimum Dropoff Latitude:  -0.000008
* Maximum Dropoff Longitude:  9.6999996E-5
* Minimum Dropoff Longitude:  -0.000163

## Question-6: Distinct Values of the Field

* Distinct Vendor Id:  ['CMT', 'VTS']
* Distinct Store And Forward Flag:  ['N', 'Y', '']

## Question-7: Min & Max Values of Numeric Fields

* Maximum Passenger Count:  9
* Minimum Passenger Count:  0

* Maximum Trip Time in Secs:  999
* Minimum Trip Time in Secs:  0

* Maximum Trip Distance:  99.70
* Minimum Trip Distance:  .00

## Question-8: Chart to Show the Average Number of Passengers Each Hour of the Day.

### Average Number of Passengers Vs Hour for All Records in Given Data

![GitHub Logo](/images/AvgPassengerCount.png)

## Question-9: New CSV File Which Has Only One Out of Every Thousand Rows.


## Question-10: Compare Charts From Normal Dataset and Reduced Row From Q-9 Dataset.

### Average Number of Passengers for Reduced Row Vs Hour for All Records in Reduced Data

![GitHub Logo](/images/RRAvgPassengerCount.png)

## Console Output

![GitHub Logo](/images/Console_Output_SS.png)
