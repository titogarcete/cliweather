import requests
from requests.exceptions import HTTPError, ConnectionError
import json
import argparse
from dotenv import load_dotenv
import os
import csv

# Configurar los argumentos CLI
parser = argparse.ArgumentParser(description='Este es un script para solicitar el clima de una ubicación.')
parser.add_argument('ciudad', help='Agregue la ubicación que desee.')
parser.add_argument('formato', help='Elija el formato de salida: json, texto o csv.')
parser.add_argument('--guardar', action='store_true', help='Guarde los resultados en un archivo.')

# Procesa los argumentos
args = parser.parse_args()
ciudad = args.ciudad  # Ciudad desde CLI
formato = args.formato.lower()  # Formato de salida (convertido a minúsculas)
guardar = args.guardar  #para guardar en archivo
# Cargar la API_KEY desde .env
load_dotenv()
API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("La API_KEY no está configurada en el archivo .env")


base = "https://api.openweathermap.org/data/2.5/weather?"
url = f"{base}q={ciudad}&appid={API_KEY}&units=metric"

# Función para obtener los datos de clima
def obtener_clima(url):
    try:
        respuesta = requests.get(url,)
        respuesta.raise_for_status()  # Lanza error si no se recibe código 200
        return respuesta.json()
    except HTTPError as http_err:
        print(f"Error HTTP: {http_err}")
    except ConnectionError as conn_err:
        print(f"Error de conexión: {conn_err}")
    except Exception as err:
        print(f"Ocurrió un error inesperado: {err}")
    return None

# Obtener los datos del clima
r = obtener_clima(url=url)
if r:
    temperatura = r['main']['temp']
    humedad = r['main']['humidity']
    descripcion = r['weather'][0]['description']

    clima_dic = {
        "humedad": humedad,
        "temperatura": temperatura,
        "descripcion": descripcion
    }

    if formato == 'json':
        print(json.dumps(clima_dic, indent=4))

        if guardar:
            with open("clima_dic.json", "w") as json_file:
                json.dump(clima_dic, json_file, indent=4)
            print("Datos guardados en formato JSON: 'clima_dic.json'.")

    elif formato == 'texto':
        for k, v in clima_dic.items():
            print(f"{k}: {v}")

        if guardar:
            with open("clima_dic.txt", "w") as txt_file:
                for k, v in clima_dic.items():
                    txt_file.write(f"{k}: {v}\n")
            print("Datos guardados en formato de texto: 'clima_dic.txt'.")

    elif formato == 'csv':
        print("Parámetro, Valor")
        for k, v in clima_dic.items():
            print(f"{k}, {v}")

        if guardar:
            with open("clima_dic.csv", "w", newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(["Parámetro", "Valor"])
                for k, v in clima_dic.items():
                    writer.writerow([k, v])
            print("Datos guardados en formato CSV: 'clima_dic.csv'.")

    else:
        # Si el formato no es válido, mostrar un mensaje de error
        print(f"Formato '{formato}' no reconocido. Use 'json', 'texto' o 'csv'.")
else:
    print("No se pudo obtener el clima.")