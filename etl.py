# Import libraries and helper dictionaries
import configparser
import os
import logging
from pyspark.sql import SparkSession

from pyspark.sql import functions as F
from pyspark.sql import types as T
from datetime import datetime, timedelta

from pyspark.sql.functions import udf, col
from pyspark.sql.functions import year, month, dayofmonth, date_format

import numpy as np
import pandas as pd

from support import ports_dictionary, states_dictionary

# Set up AWS credentials configuration
config = configparser.ConfigParser()
config.read('dl.cfg')

os.environ['AWS_ACCESS_KEY_ID']=config['AWS']['AWS_ACCESS_KEY_ID']
os.environ['AWS_SECRET_ACCESS_KEY']=config['AWS']['AWS_SECRET_ACCESS_KEY']


def create_spark_session():
    spark = SparkSession \
        .builder \
        .config("spark.jars.packages", "org.apache.hadoop:hadoop-aws:2.7.0") \
        .getOrCreate()
    return spark


def process_city_data(spark, city_data, output_data):
    """
    Function to read/process city information data in the USA and produce a dimension table for
    various indicators by location.

    """

    # read in city data as csv
    cities = pd.read_csv(city_data, sep=';')

    # Select rows needed and drop duplicates
    cities_table = cities[['City', 'State', 'Median Age', 'Total Population', 'Foreign-born']].drop_duplicates()

    # Make foreign ratio column
    cities_table['Foreign_ratio'] = cities_table['Foreign-born']/cities_table['Total Population']

    # Create Location_d by replacing states name with abbreviation, upper case city name and join on ', '
    cities_table = cities_table.replace({"State":states_dictionary})
    cities_table['City'] = cities_table.City.apply(lambda x : x.upper())
    cities_table['Location_id'] = cities_table['City'].fillna('') + ', ' + cities_table['State'].fillna('')
    cities_table['Location_id'] = cities_table['Location_id'].str.strip(',')

    # Rename columns
    cities_table = cities_table.rename(columns = {'Foreign-born':'Foreign_born', 'Total Population':'Total_population',
                                                  'Median Age':'Median_age'})

    # Change data types
    cities_table.Total_population = cities_table.Total_population.astype(int)

    # Change to PySpark dataframe
    location_table = spark.createDataFrame(cities_table)

    # Test 1 - Check that primary key for location_table is unique
    if location_table.select('Location_id').distinct().count() == location_table.select('Location_id').count():
        logging.info("Primary key for Location table is unique. Test 1 passed.")
        print("Primary key for Location table is unique. Test 1 passed.")
    else:
        logging.warning("Primary key for Location table is not unique. Test 1 failed.")

    # Write table to parquet
    logging.info("Writing location table to parquet files")
    location_table.write.parquet(path = output_data+'location_table', mode = "overwrite")


def process_event_data(spark, immigration_event_data, output_data):
    """
    Function to read/process immigration event data and produce/write admissions and time tables.
    """

    # read in immigration data as parquet data file
    df_spark=spark.read.parquet(immigration_event_data)

    # Select needed columns from event data
    admissions_table = df_spark.select('cicid','i94port', 'arrdate', 'i94bir', 'gender', 'visatype')

    # change date to timestamp
    get_timestamp = F.udf(lambda x: (datetime(1960,1,1) + timedelta(x - 1)).strftime("%Y-%m-%d"))
    admissions_table = admissions_table.withColumn("tempdate",
                                                   get_timestamp(admissions_table.arrdate)).drop(admissions_table.arrdate)
    admissions_table = admissions_table.withColumn('Date',
                                                   admissions_table.tempdate.cast(dataType=T.TimestampType())).drop(admissions_table.tempdate)

    # Rename columns and change datatypes
    admissions_table = admissions_table.withColumnRenamed('visatype','Visa_type')
    admissions_table = admissions_table.withColumnRenamed('i94port','Location_id')
    admissions_table = admissions_table.withColumnRenamed('gender','Gender')

    admissions_table = admissions_table.withColumn("Admission_id", admissions_table["cicid"].cast(T.IntegerType())).drop(admissions_table.cicid)
    admissions_table = admissions_table.withColumn("Age", admissions_table["i94bir"].cast(T.IntegerType())).drop(admissions_table.i94bir)

    # replace port with dictionary
    admissions_table = admissions_table.na.replace(ports_dictionary,'Location_id')

    # Make time table
    time_table = admissions_table.select('Date')
    time_table = time_table.dropDuplicates()
    time_table = time_table.withColumn("day", F.dayofmonth("Date"))
    time_table = time_table.withColumn("month", F.month("Date"))
    time_table = time_table.withColumn("year", F.year("Date"))

    # Test 2 - Check that primary key for admission_table is unique
    if admissions_table.select('Admission_id').distinct().count() == admissions_table.select('Admission_id').count():
        logging.info("Primary key for Admissions table is unique. Test 2 passed.")
        print("Primary key for Admissions table is unique. Test 2 passed.")
    else:
        logging.warning("Primary key for Admissions table is not unique. Test 2 failed.")

    # Test 3 - Check that primary key for admission_table is unique
    if time_table.select('Date').distinct().count() == time_table.select('Date').count():
        logging.info("Primary key for Time table is unique. Test 3 passed.")
        print("Primary key for Time table is unique. Test 3 passed.")
    else:
        logging.warning("Primary key for Time table is not unique. Test 3 failed.")

    # Write tables to parquet
    logging.info("Writing admissions table to parquet files")
    admissions_table.write.parquet(path = output_data+'admissions_table', mode = "overwrite", partitionBy = ['Date','Visa_type'])

    logging.info("Writing time table to parquet files")
    time_table.write.parquet(path = output_data+'time_table', mode = "overwrite")


def main():
    spark = create_spark_session()
    city_data = "s3a://your-s3-bucket-name/us-cities-demographics.csv"
    immigration_event_data = "s3a://your-s3-bucket-name/sas_data"
    output_data = "s3a://your-s3-bucket-name/outputs/"

    process_city_data(spark, city_data, output_data)
    process_event_data(spark, immigration_event_data, output_data)
    logging.info("program run to completion")


if __name__ == "__main__":
    main()
