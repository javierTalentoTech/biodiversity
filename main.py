import requests
import pandas as pd
# Endpoint de la API de GBIF
url = 'https://api.gbif.org/v1/occurrence/search'

# Parámetros de búsqueda
params = {
    'country': 'CO',  # Código del país para Colombia
    'limit': 1000       # Número de registros a obtener
}

# Hacer una solicitud GET a la API de GBIF
response = requests.get(url, params=params)

# Verificar que la solicitud fue exitosa
if response.status_code == 200:
    data = response.json()
    listado = []
    for record in data['results']:
        if  'Cundinamarca' in record.get('verbatimLocality'):
            dic = {
                'nombre': record.get('species'),
                'tipo': record.get('kingdom'),
                'imagen': record.get('occurrenceID'),
                'ubicacion': record.get('verbatimLocality')
            }
            listado.append(dic)
    
    df = pd.DataFrame(listado)
    # print(df)

    # # Mostrar el DataFrame
    df.to_csv('datos.csv', index=False)
    print('successful file creation')

else:
    print(f"Error al acceder a la API de GBIF: {response.status_code}")

