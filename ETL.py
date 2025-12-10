# Here we are going to devlope a complete ETL pipeline such that it asks user for enter the city then it extracts the weather condition for last 7 days of that particular city and convert it into csv file
# first of all we are going to import some certain libraries for data processing
import requests
import json
from datetime import datetime, timedelta
import pandas as pd
def Extract(city,n):
    try:
        raw_responses = []
        API_KEY = 'a79ba54d12904a2b83364116250812' # use your API Key insted of this
        for i in range(n):
            date = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d")
            url = f"http://api.weatherapi.com/v1/history.json?key={API_KEY}&q={city}&dt={date}"  # and if want then you can use your url instead. 
            response = requests.get(url)
            data = response.json()
            raw_responses.append(data)
        return raw_responses
    except Exception as e:
        print(f'The operation got failed due to\n {e}')
def Transform(a):
    records = []
    for raw in a:
        record = {
        'City' : raw['location']['name'],
        'Location': raw['location']['region'],
        'Country': raw['location']['country'],
        'Latitude': raw['location']['lat'],
        'Longitude': raw['location']['lon'],
        'Day': raw['forecast']['forecastday'][0]['date'],
        'Teperature_C': raw['forecast']['forecastday'][0]['day']['avgtemp_c'],
        'Humidity': raw['forecast']['forecastday'][0]['day']['avghumidity'],
        'Wind Speed': raw['forecast']['forecastday'][0]['day']['maxwind_kph'],
        'Condition': raw['forecast']['forecastday'][0]['day']['condition']['text'],
        'Precipitation':raw['forecast']['forecastday'][0]['day']['totalprecip_mm']}
        records.append(record)
    df = pd.DataFrame(records)
    return df
def Load(df):
    return df.to_csv('Weather_data.csv',index=False)

if __name__ == "__main__":
    city = input('Enter the name of the city for which you want the weather record:')
    n = eval(input('Enter the number of record you want:'))
    a = Extract(city,n)
    data = Transform(a)
    Load(data)
    
