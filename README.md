# Clima API - Script CLI

Este script permite consultar el clima de una ciudad específica usando la API de OpenWeatherMap y mostrar los resultados en varios formatos: JSON, texto o CSV. Además, incluye la opción de guardar los datos en un archivo.

## Requisitos

- **Python 3.x**
- Librerías de Python: `requests`, `dotenv`, `argparse`, `json`, `csv`

Para instalar las dependencias necesarias, ejecuta:

```bash
pip install requests python-dotenv
```

## Configuración

1. Crea un archivo `.env` en el mismo directorio que el script y agrega tu API key de OpenWeatherMap:

   ```
   API_KEY=tu_clave_api
   ```

2. Asegúrate de que la clave API esté disponible en el entorno de ejecución del script.

## Uso

Ejecuta el script desde la terminal con el siguiente comando:

```bash
python script.py <ciudad> <formato> [--guardar]
```

- `<ciudad>`: Nombre de la ciudad.
- `<formato>`: Formato de salida (`json`, `texto`, `csv`).
- `--guardar`: (Opcional) Guarda los resultados en un archivo.

### Ejemplos:

1. Clima de Asunción en formato JSON:

   ```bash
   python script.py Asunción json
   ```

2. Clima de Madrid en texto, guardando el resultado en un archivo:

   ```bash
   python script.py Madrid texto --guardar
   ```

3. Clima de Buenos Aires en formato CSV:

   ```bash
   python script.py "Buenos Aires" csv
   ```

## Archivos Guardados

- `clima_dic.json` para formato JSON.
- `clima_dic.txt` para formato de texto.
- `clima_dic.csv` para formato CSV.

## Manejo de Errores

El script captura errores relacionados con la conexión y solicitudes HTTP, mostrando mensajes apropiados si algo sale mal.

---

Este README proporciona una guía clara para configurar y utilizar el script sin entrar en detalles innecesarios.
