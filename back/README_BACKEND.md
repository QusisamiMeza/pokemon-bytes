# Pokemon Bytes
Este proyecto es un backend construido con FastAPI. A continuación, encontrarás las instrucciones necesarias para configurarlo y ejecutarlo correctamente.
Está diseñado principalmente para ser ejecutado en sistemas Linux, y las instrucciones están orientadas a este entorno.

## Requisitos previos
Asegurate de tener instalados los siguientes componentes:

- Python 3.10
- pip
- Git

## Instalación

1. **Clona el repositorio:**
    ```bash
    git clone git@github.com:Ginorris/pokemon-bytes.git
    cd pokemon-bytes
    ```

1. **Crea un entorno virtual (puede ser python en vez de python3 dependiendo del sistema)**
    ```bash
    python3 -m venv env
    source env/bin/activate


2. **Instala las dependencias**
    ```bash
    pip install -r requirements.txt
    ```

3. **(Opcional) Moverse a la rama en desarrollo, actualmente:**
    ```bash
    git switch parte_2
    git pull
    ```

4. **Aplica las migraciones de la base de datos**
    ```bash
    alembic upgrade head
    ```

5. **Ejecutar Servidor (en modo desarrollo):**
    **Para desarrollo**
    ```bash
    fastapi dev app/main.py
    ```
    **Para Produccion**
    ```bash
    uvicorn app.main:app --reload
    ```


## Aclaracion:
La carga inicial de datos (seed) del backend se ejecuta automáticamente al iniciar la aplicación. No es necesario realizar pasos adicionales para poblar la base de datos.


# Notas
## Base de Datos

### Migraciones
#### - Para generar las migraciones de forma manual se puede hacer:
```bash
alembic revision -m "Crear tabla alumnos"
```
#### Y luego modificar el archivo con los cambios


####  - Para generar las migracione en base a los modelos SQLModel se pueden importar en alembic/.env,
#### luego agregar su metadata de la forma:
```bash
target_metadata = Pokemon.metadata # nombre del modelo
```

#### Y se corren las migraciones de la siguiente manera:
```bash
alembic revision --autogenerate -m "se crea el modelo pokemon"
```

## Importante! revisar las migraciones una vez creadas.

#### En cualquiera de los casos para aplicar las migraciones se usa:
```bash
alembic upgrade head
```

#### Nota: usando sqlite cuando se aplican migraciones se crea el archivo.db si no existe.


## Dependencias
### Instalar los paquetes necesarios en el venv local:

```bash
pip install -r requirements.txt
```

### Actualizar las dependencias:

```bash
pip freeze > requirements.txt
```

## Tests
### Correr tests
```bash
pytest
```

### Correr tests con coverage
```bash
coverage run -m pytest
coverage report -m
```
