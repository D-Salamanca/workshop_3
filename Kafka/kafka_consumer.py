from kafka import KafkaConsumer
from sqlalchemy import create_engine, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import json

# Cargar variables de entorno
load_dotenv()  
DATABASE_URL = os.getenv("DATABASE_URL")

# Configuración de conexión a la base de datos
if not DATABASE_URL:
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_NAME = os.getenv("DB_NAME")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

# Definir el modelo para la tabla happiness_predictions
class HappinessPrediction(Base):
    __tablename__ = 'happiness_predictions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    country = Column(String(255))
    economy_gdp_per_capita = Column(Float)
    social_support = Column(Float)
    health_life_expectancy = Column(Float)
    freedom = Column(Float)
    perceptions_of_corruption = Column(Float)
    economy_social_support = Column(Float)
    health_freedom = Column(Float)
    economy_health = Column(Float)
    log_economy = Column(Float)
    health_squared = Column(Float)
    freedom_squared = Column(Float)
    continent = Column(String(255))
    predicted_happiness_score = Column(Float)

# Crear tabla en PostgreSQL si no existe
Base.metadata.create_all(engine)

# Configurar consumidor de Kafka
consumer = KafkaConsumer(
    'happiness_score_predictions',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

# Consumir mensajes de Kafka y almacenarlos en PostgreSQL
for message in consumer:
    data = message.value
    features = data['features']
    predicted_score = data['predicted_happiness_score']
    
    # Crear instancia de HappinessPrediction
    prediction = HappinessPrediction(
        country=features.get('Country', 'Unknown'),
        economy_gdp_per_capita=features.get('Economy (GDP per Capita)', None),
        social_support=features.get('Social support', None),
        health_life_expectancy=features.get('Health (Life Expectancy)', None),
        freedom=features.get('Freedom', None),
        perceptions_of_corruption=features.get('Perceptions of corruption', None),
        economy_social_support=features.get('Economy_SocialSupport', None),
        health_freedom=features.get('Health_Freedom', None),
        economy_health=features.get('Economy_Health', None),
        log_economy=features.get('Log_Economy', None),
        health_squared=features.get('Health_Squared', None),
        freedom_squared=features.get('Freedom_Squared', None),
        continent=features.get('Continent', 'Unknown'),
        predicted_happiness_score=predicted_score
    )
    
    # Agregar a la sesión y guardar en la base de datos
    session.add(prediction)
    session.commit()

print("Predicciones recibidas y almacenadas en PostgreSQL usando SQLAlchemy.")

# Cerrar la sesión
session.close()