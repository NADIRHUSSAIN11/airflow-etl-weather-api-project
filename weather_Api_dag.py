#Imports 

from airflow import DAG
from datetime import timedelta, datetime
from airflow.providers.http.sensors.http import HttpSensor
import json
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python import PythonOperator
import pandas as pd

# Functions to convert kelvin to fahrenheit

def k_to_f(temp_in_k):
    temp_in_f= (temp_in_k - 273.15) * (9/5) + 32
    return temp_in_f

# ETL Process for the Weather API

def data_etl(task_instance):
    
    
    # Handling the Json Data (Extraction)
    data = task_instance.xcom_pull(task_ids="extract_weather_data")
    city_name = data['name']
    weather_description = data['weather'][0]['description']
    temperature_fahrenheit = k_to_f(data["main"]["temp"])
    feels_like_temperature_fahrenheit = k_to_f(data["main"]["feels_like"])
    min_temperature_fahrenheit = k_to_f(data["main"]["temp_min"])
    max_temperature_fahrenheit = k_to_f(data["main"]["temp_max"])
    atmospheric_pressure = data['main']['pressure']
    humidity_percentage = data['main']['humidity']
    wind_speed_value = data['wind']['speed']
    recorded_time = datetime.utcfromtimestamp(data['dt'] + data['timezone'])
    sunrise_timestamp = datetime.utcfromtimestamp(data['sys']['sunrise'] + data['timezone'])
    sunset_timestamp = datetime.utcfromtimestamp(data['sys']['sunset'] + data['timezone'])
    
    # Transforming the Json Data to the dictionary
    transformed_data = {"City": city_name,
                        "Description": weather_description,
                        "Temperature(F)": temperature_fahrenheit,
                        "Feels Like(F)": feels_like_temperature_fahrenheit,
                        "Minimun Temp(F)":min_temperature_fahrenheit,
                        "Maximum Temp(F)": max_temperature_fahrenheit,
                        "Pressure": atmospheric_pressure,
                        "Humidty": humidity_percentage,
                        "Wind Speed": wind_speed_value,
                        "Time of Record": recorded_time,
                        "Sunrise (Local Time)":sunrise_timestamp,
                        "Sunset (Local Time)": sunset_timestamp                        
                        }
    
    # Storing the Data to List and converting it to Pandas DataFrame
    data_list=[transformed_data]
    df=pd.DataFrame(data_list)
    
    # AWS login credrentials 
    aws_credentials = {"key": "*************", "secret": "*********************************"}

    # Storing the Data into Amazone S3 with timestamps
    now = datetime.now()
    date_string = now.strftime("%d%m%Y%H%M%S")
    date_string = 'current_weather_data_Karachi_' + date_string
    df.to_csv(f"s3://weatherdatakarachi/{date_string}.csv", index=False, storage_options=aws_credentials)
    


# DAG default Arguments
default_args={
    
    'owner':'nadir',
    'depends_on_past':False,
    'start_date':datetime(2023,12,16),
    'email':['nadirarain111@gmail.com'],
    'email_on_failure':False,
    'email_on_retry':False,
    'retries':1,
    'retry_delay':timedelta(minutes=2)
    
}

# DAG Defination
with DAG(
    dag_id='weather_etl',
    default_args=default_args,
    schedule_interval="@daily",
    description="weather etl dag",
    catchup=False 
) as dag:

    # Task Definations for the checking API availibility
    is_api_ready= HttpSensor(        
        task_id="is_api_ready",
        http_conn_id='api_weather',
        endpoint='/data/2.5/weather?q=karachi&appid=**************************'
        
    )
    
    # Task Definations for the extraction of API data 
    extract_weather_data = SimpleHttpOperator(
        task_id = 'extract_weather_data',
        http_conn_id = 'api_weather',
        endpoint='/data/2.5/weather?q=karachi&appid=**************************',
        method = 'GET',
        response_filter= lambda r: json.loads(r.text),
        log_response=True
        )    
    
    
    # Task Definations for calling transformation function
    transform_data= PythonOperator(
        
        task_id='weather_data_transform',
        python_callable=data_etl    
    )
    
    
    # Flow of the Tasks
    is_api_ready >> extract_weather_data  >> transform_data

