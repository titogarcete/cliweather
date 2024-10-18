#!/bin/bash

echo "Bash script..."

# Crear entorno virtual (comando)
if [ ! -d ".venv" ]; then
    echo "crear entorno virtual"
    python -m venv .venv
    echo "entorno virtual creado"
fi

# Activar entorno virtual
echo "Activar entorno virtual"
source .venv/Scripts/activate
echo "entorno virtual activado"

# Instalar requerimientos
echo "Instalando los requerimientos necesarios"
pip install -r requirements.txt

# Ejecutar la aplicación con parámetros predeterminados
echo "ejecutando el cli..."
python weather.py asuncion json


# bash script.sh 

# chmod +x script.sh 