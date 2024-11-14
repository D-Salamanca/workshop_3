from kafka import KafkaProducer
import pandas as pd
import joblib  # Usamos joblib para cargar el modelo
import json
import os

# Ruta del modelo entrenado
model_path = os.path.join(os.path.dirname(__file__), '../Model/random_forest_model.pkl')
model = joblib.load(model_path)  # Cargar el modelo usando joblib

# Ruta del archivo de datos de prueba
test_data_path = os.path.join(os.path.dirname(__file__), '../data/happiness_test_data.csv')
test_data = pd.read_csv(test_data_path)

# Configuración del productor de Kafka
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serializar el valor en JSON
)

# Realizar predicciones y enviarlas a Kafka
for index, row in test_data.iterrows():
    # Extraer las características necesarias para la predicción
    features = row[["Economy (GDP per Capita)", "Social support", "Health (Life Expectancy)", 
                    "Freedom", "Perceptions of corruption", "Economy_SocialSupport", "Health_Freedom", 
                    "Economy_Health", "Log_Economy", "Health_Squared", "Freedom_Squared", 
                    "Continent_Africa", "Continent_Asia", "Continent_Europe", 
                    "Continent_North America", "Continent_Oceania", "Continent_South America"]].to_dict()

    # Crear un DataFrame con una fila para la predicción
    features_df = pd.DataFrame([features])

    # Realizar la predicción con el modelo cargado
    predicted_score = model.predict(features_df)[0]

    # Crear el mensaje para enviar a Kafka
    message = {
        'index': index,
        'features': features,
        'predicted_happiness_score': predicted_score
    }

    # Enviar el mensaje al tópico de Kafka
    producer.send('happiness_score_predictions', value=message)

print("Las predicciones han sido enviadas a Kafka.")
producer.flush()  # Asegurarse de que todos los mensajes hayan sido enviados
producer.close()  # Cerrar el productor de Kafka
