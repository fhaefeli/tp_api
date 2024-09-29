# Flask App con Modelo Entrenado
Este proyecto es una aplicación web desarrollada con Flask que utiliza un modelo de Machine Learning entrenado previamente. 
El modelo ha sido exportado y es utilizado en la aplicación para realizar predicciones sobre si un cliente abandonará el servicio (hará "churn"), siendo esta la clase positiva. 
La aplicación está desplegada en AWS.

## Estructura del Proyecto
1. **Creación del Modelo**: 
   - Se entrenó un modelo de Machine Learning usando `scikit-learn`.
   
2. **Exportación del Modelo**:
   - El modelo entrenado fue guardado en formato `pickle` para ser reutilizado en la aplicación web.

3. **Creación del archivo `Main`**:
   - Se usó `Flask` para crear la aplicación web.
   - Se importó el modelo entrenado desde el archivo `pickle`.

4.  **Creación del archivo `Index`**:
   - Se definió el formato del front de la app web donde el usuario insertará su input.

5. **Creación del archivo `Result`**:
   - Se definió el formato del front de la app web donde el usuario recibirá el resultado (output del modelo).

## Despliegue en GitHub

1. **Subida de la App Flask**:
   - Subimos el código de la aplicación Flask al repositorio de GitHub.
   
2. **Requirements**:
   - Se incluyó un archivo `requirements.txt` con las dependencias necesarias para ejecutar la aplicación.

3. **Git Ignore**:
   - Se creó un archivo `.gitignore` para evitar subir archivos locales no deseados al repositorio.

## Despliegue en AWS

1. **Creación de la Instancia**:
   - Se creó una instancia en AWS EC2 con las configuraciones necesarias.

2. **Habilitación de Puertos**:
   - Se habilitó el puerto necesario para que la aplicación web sea accesible públicamente.

3. **Importación de Archivos desde GitHub**:
   - Se clonó el repositorio en la instancia de AWS.

4. **Ejecución de la App**:
   - Se ejecutó la aplicación Flask en la instancia.

5. **Hacemos la App Pública**:
   - Se configuró la instancia para que la app esté disponible públicamente en la web.

## Requisitos
- Python 3.10+
- Flask
- scikit-learn
- pickle

Instalar dependencias con:
```bash
pip install -r requirements.txt
