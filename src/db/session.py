from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.core.config import settings  # Asegúrate de que 'settings' esté correctamente configurado

# Crea el motor (engine) utilizando la URL de la base de datos desde la configuración
engine = create_engine(settings.DATABASE_URL)

# Crea una fábrica de sesiones que puede ser utilizada para obtener una nueva sesión en cada solicitud
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
