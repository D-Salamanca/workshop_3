# workshop_3
Aquí tienes un ejemplo de un archivo `README.md` para tu proyecto de predicción de felicidad utilizando **Kafka**, **PostgreSQL**, **Docker**, y **Machine Learning**.

# Happiness Score Prediction with Kafka, PostgreSQL, and Machine Learning

Este proyecto implementa un sistema de predicción del `Happiness Score` utilizando modelos de machine learning. La arquitectura incluye un productor y un consumidor de Kafka para manejar las predicciones en tiempo real y almacenarlas en una base de datos PostgreSQL. Docker se utiliza para la configuración y el despliegue de los servicios.

## Tabla de Contenidos

- [Descripción](#descripción)
- [Arquitectura](#arquitectura)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno)
- [Comandos Docker](#comandos-docker)
- [Comandos Git](#comandos-git)

## Descripción

Este sistema predice el puntaje de felicidad de diferentes países utilizando un modelo de Random Forest. Los datos de predicción se envían a Kafka, que actúa como una cola de mensajes, y luego son consumidos y almacenados en una base de datos PostgreSQL para futuras consultas y análisis.

## Arquitectura

1. **Kafka Producer**: Envía características de datos al tópico `happiness_score_predictions`.
2. **Kafka Consumer**: Lee las predicciones de felicidad y las almacena en PostgreSQL.
3. **PostgreSQL**: Base de datos para almacenar las predicciones de felicidad.
4. **Modelo de Machine Learning**: Random Forest, entrenado para predecir `Happiness Score`.

## Tecnologías Utilizadas

- **Python**: Para implementar el modelo de machine learning y el manejo de Kafka.
- **Kafka**: Sistema de mensajería para la transmisión de predicciones en tiempo real.
- **PostgreSQL**: Base de datos relacional para almacenar las predicciones.
- **Docker**: Para contenerizar los servicios de Kafka, PostgreSQL y los consumidores.
- **SQLAlchemy**: ORM para conectar Python con PostgreSQL.
- **scikit-learn**: Biblioteca de machine learning utilizada para entrenar el modelo.

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd <NOMBRE_DEL_REPOSITORIO>


2. Crear un entorno virtual e instalar dependencias:

   ```bash
   python -m venv env
   source env/bin/activate  # En Linux o Mac
   env\Scripts\activate  # En Windows
   pip install -r requirements.txt
   ```

3. Configurar las variables de entorno en un archivo `.env`. Ver sección [Configuración de Variables de Entorno](#configuración-de-variables-de-entorno) para más detalles.

## Uso

1. **Entrenar el modelo**: Entrena el modelo de `Happiness Score` y guárdalo en `Model/random_forest_model.pkl`.
2. **Levantar los servicios con Docker Compose**:

   ```bash
   docker-compose up -d
   ```

3. **Ejecutar el productor**: Usa `kafka_producer.py` para enviar datos de predicción al tópico de Kafka.
4. **Consumir predicciones**: `kafka_consumer.py` consume los datos y almacena los resultados en PostgreSQL.

## Estructura del Proyecto

```plaintext
├── data                    # Datos y resultados de prueba
├── models                  # Modelos entrenados
├── kafka_producer.py       # Productor de Kafka para enviar datos
├── kafka_consumer.py       # Consumidor de Kafka para almacenar predicciones en PostgreSQL
├── Dockerfile              # Dockerfile para el consumidor de Kafka
├── docker-compose.yml      # Configuración de Docker Compose
├── requirements.txt        # Dependencias del proyecto
└── README.md               # Documentación del proyecto
```

## Configuración de Variables de Entorno

Configura un archivo `.env` en el directorio principal del proyecto con las siguientes variables:

```dotenv
# Configuración de PostgreSQL
DB_USER=tu_usuario
DB_PASSWORD=tu_contraseña
DB_HOST=localhost
DB_NAME=nombre_base_de_datos

# URL de la base de datos (alternativa a las variables individuales)
DATABASE_URL=postgresql://tu_usuario:tu_contraseña@localhost/nombre_base_de_datos
```

## Comandos Docker

- Levantar servicios en segundo plano:

  ```bash
  docker-compose up -d
  ```

- Parar servicios:

  ```bash
  docker-compose down
  ```

## Comandos Git

- Inicializar el repositorio:

  ```bash
  git init
  git add .
  git commit -m "Primera versión del proyecto de Kafka y PostgreSQL"
  ```

- Subir cambios a GitHub:

  ```bash
  git remote add origin <URL_REPOSITORIO>
  git push -u origin main
  ```

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue para discutir cambios importantes antes de realizar un pull request.
