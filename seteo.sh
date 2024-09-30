#!/bin/bash

# Actualizar la lista de paquetes
sudo apt-get update -y

# Instalar Python y pip
sudo apt-get install python3 python3-pip -y

# Crear un entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias necesarias
pip install flask
pip install numpy
pip install scikit-learn

# Mostrar el estado del repositorio git
git status

# Ejecutar el archivo main.py
python main.py
