# PySpark DataLake Project

## Project Scope

This project was done as my capstone project for the Udacity Data Engineer Nanodegree Program. 

The scope of the project was to build an ETL pipeline that processed multiple data sources with a minimum of 1,000,000 rows of data as input. The data was to be transformed into a data model that could be easily usable by an analytics team.

## Project Steps
1. Read in over 3 million rows of US immigration arrivals data from AWS S3 in parquet format to Pyspark.
2. Read in US city demographic data in csv format to Pyspark.
3. Clean both datasets using Pyspark data wrangling functions.
4. Transform the 2 datasets into a usable data model consisting of a 3 table star schema format. (admissions_table, location_table, time_table).
5. Use integrity tests on the final tables to ensure primary key uniqueness.
6. Write the three tables back to AWS S3 in parquet format to be available for an analytics team to easily access and use.

## Data Model

The data model follow a star schema. It consists of 3 tables.

### Admissions table

- Location_id: string - Secondary key. Location of arrival port in the US.
- Gender: string - Gender of arriving person. M, F or NaN.
- Visa_type: string - types of arrival visas including: 'WT', 'B2', 'CP', 'B1', 'GMT', 'WB', 'F1', 'E2', 'F2', 'M1'.
- Date: timestamp - Secondary key. Date of arrival to the US.
- Admission_id: integer - Primary key. Unique number for each immigrant arrival.
- Age: integer - Age of arriving person.

### Location table

- City: string - US city name of location.
- State: string - US state name of location.
- Median_age: double - Median age of persons living in location.
- Total_population: long - Total population of location.
- Foreign_born: double - Total number of foreign born population in location.
- Foreign_ratio: double - Proportion of foreign born population in location.
- Location_id: string - Primary key. Location within the US.

### Time table

- Date: timestamp - Primary key. Date.
- day: integer - Day of date.
- month: integer - Month of date.
- year: integer - Year of date.

I chose this data model so that aggregate analysis could easily be done on immigrant arrivals at the city and state level as well as doing analysis of arrivals over time.

## Tools and Technologies

The technologies chosen for this project were Pyspark and AWS S3.
Pyspark is a great tool for data wrangling large datasets. The data for this project was too big to fit into memory on a single computer and couldn't use pandas as an option for data wrangling. 

AWS S3 is a solid option for cloud storage and serves as the data lake for project hosting both the input files and output tables after the etl script is run.

## Project Files

- etl.py (script that reads in data, performs wrangling, runs tests, and outputs data model tables - need to use your AWS credentials to use.)
- etl_local.py (local version of etl.py)
- support.py (script contains dictionaries for helping with data wrangling)
- dl-template.cfg (AWS permissions configuration data for S3 - need to add your own AWS credentials to use)
- Data Dictionary.txt (Description of columns in each table of the data model)

## Data
- sas_data/ (immigration event data in parquet form)
- us-cities-demographics.csv (us city demographic input data)

## How to Interact with the Project

### Dependencies
- python 3.x
- pyspark
- numpy
- pandas

### Instructions

Option 1 (quick option):

Download the project files and run etl_local.py from the command line to see how it works.

Option 2:

1. Download the project files
2. Add your AWS credentials to dl.cfg
3. add the data files to your AWS S3 bucket
4. Run etl.py from the command line


## Extensions - How Would the Project Change Under the Following Scenarios

1. The data was increased by 100x.

Since pytorch uses distributed computing. If the event data was increased by 100x I would potentially need to run the etl script using AWS EMR with a large cluster of sufficient size to process the data in a reasonable amount of time.

2. The pipelines run on a daily basis by 7am every day.

In this case I would need to use a scheduler to re-run the etl script on a daily basis. Apache Airflow could be incorporated here and the Pytorch script could run daily incorporate newly added immigration event data.

3. The database needed to be accessed by 100+ people.

AWS read access would need to be given the 100+ users so that they coud access the analytics tables or whatever other aspect of the project they need to access.
