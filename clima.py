import requests
from bs4 import BeautifulSoup

# URL del sitio web con datos climáticos
url = 'https://weather.com/es-CO/tiempo/hoy/l/5.54,-73.36?par=google'

def scrape_weather(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f'Error al acceder a la página: {response.status_code}')
        return None

    # Analizar el contenido de la página con BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extraer la información climática relevante
    weather_data = {}

    try:
        location = soup.find('h1', class_='CurrentConditions--location--1YWj_').text
        temperature = soup.find('span', class_='CurrentConditions--tempValue--MHmYY').text
        condition = soup.find('div', class_='CurrentConditions--phraseValue--mZC_p').text

        weather_data = {
            'location': location,
            'temperature': temperature,
            'condition': condition
            
        }
    except AttributeError as e:
        print(f'Error al extraer los datos: {e}')
    
    return weather_data

# Ejecutar el web scraping y mostrar los datos
data = scrape_weather(url)
if data:
    for key, value in data.items():
        print(f'{key}: {value}')
else:
    print('No se pudo obtener la información climática.')
