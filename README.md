# Extract, Transform, Load (ETL) for Weather Data using Apache Airflow and Amazon S3

## Overview
![airflowproject](https://github.com/NADIRHUSSAIN11/airflow-etl-weather-api-project/assets/89727973/9103dae8-f90b-434d-b5f6-60475486526b)



This data engineering project involves the extraction of weather data from the OpenWeatherMap API, the transformation of the data using Apache Airflow and Pandas hosted on Ubuntu, and the loading of the processed data into Amazon S3 for storage and analysis.

## Project Components

### 1. Extraction

![Screenshot (126)](https://github.com/NADIRHUSSAIN11/airflow-etl-weather-api-project/assets/89727973/175b6bfe-3576-433d-b3eb-9ee068d6be81)


- **Source:** OpenWeatherMap API
- **Method:** Utilized Airflow to schedule and execute data extraction remotely through SSH from a local PC.
- **Details:** Extracted real-time weather data, including temperature, humidity, wind speed, and other relevant metrics.

### 2. Transformation

![Screenshot 2023-12-16 185017](https://github.com/NADIRHUSSAIN11/airflow-etl-weather-api-project/assets/89727973/2a853bed-0f71-4c9f-9660-dcb13da237c6)


- **Tools:** Apache Airflow, Python
- **DAGs (Directed Acyclic Graphs):** Developed Airflow DAGs to automate the ETL process.
- **Tasks:**
  - **Data Cleaning:** Ensured data consistency.
  - **Data Enrichment:** Added additional information to the dataset for comprehensive analysis.
  - **Data Formatting:** Ensured that the data was in a standardized format for easy integration and analysis.

### 3. Loading

![Screenshot (127)](https://github.com/NADIRHUSSAIN11/airflow-etl-weather-api-project/assets/89727973/e9c0728a-3821-49e4-852b-d7934464cf9a)


- **Destination:** Amazon S3
- **Method:** Leveraged Airflow tasks to load the cleaned and transformed data into an S3 bucket.
- **Benefits:** Enables scalable and secure storage of the weather data on the cloud.

## Project Workflow

1. **Data Extraction:**
   - Airflow DAG triggers the data extraction task remotely from the local PC.
   - OpenWeatherMap API responds with real-time weather data.

2. **Data Transformation:**
   - Airflow DAG orchestrates the transformation tasks.
   - Python scripts perform cleaning, enrichment, and formatting of the data.

3. **Data Loading:**
   - Transformed data is loaded into an Amazon S3 bucket.
   - S3 provides a reliable and scalable storage solution for weather data.

## Environment

- **Hosting:** Ubuntu
- **Remote Access:** SSH for interaction with Airflow hosted on Ubuntu.
- **Codebase:** Python scripts for data processing tasks.

## Future Enhancements

- **Data Analytics:** Incorporate tools like Apache Spark or AWS Athena for in-depth analysis.
- **Visualization:** Integrate tools like Tableau or Power BI for creating insightful visualizations.

## Conclusion

This project demonstrates effective data engineering practices for ETL processes, leveraging Apache Airflow for automation and Amazon S3 for scalable storage. It serves as a foundation for further exploration and analysis of weather patterns.

## How to Run

1. Clone the repository.
2. Set up Airflow on your Ubuntu host.
3. Configure the OpenWeatherMap API key.
4. Adjust DAG configurations as needed.
5. Run Airflow scheduler and webserver.

Feel free to contribute, provide feedback, or use this project as a reference for your data engineering endeavors!

