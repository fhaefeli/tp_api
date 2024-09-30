#!/bin/bash

#
# Actualiza los repositorios
sudo apt-get update -y

# Instala Python y pip
sudo apt-get install python3 python3-pip -y

#entorno virtual
sudo apt-get install python3-venv -y

#crear entorno virtual
python3 -m venv venv

#activar entorno virtual
source venv/bin/activate

# Instala librerías necesarias
pip install flask scikit-learn numpy pandas

# Instala otras herramientas comunes
# sudo apt-get install git -y
# sudo apt-get install awscli -y

# Otras librerías que necesites
# pip3 install <otra_libreria>

# Opcional: Crear un directorio de trabajo
# mkdir ~/mi_proyecto

# Confirmar que todo está instalado correctamente
python3 --version
pip --version
git --version
