from urllib.parse import quote_plus
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import dotenv_values


def create_db_engine():
    """
    Creates and returns a SQLAlchemy engine object for the PostgreSQL database.

    This function reads the database configuration from a .env file located in the same directory as this script.
    The .env file should contain the following keys: POSTGRES_PASSWORD, POSTGRES_DB, POSTGRES_USER, POSTGRES_SERVER.

    Returns:
        engine: A SQLAlchemy engine object connected to the PostgreSQL database.

    Raises:
        Exception: If there is a problem connecting to the database.
    """
    env_path = Path(__file__).parent / ".env"
    env_values = dotenv_values(dotenv_path=env_path)

    db_password = env_values["POSTGRES_PASSWORD"]
    encoded_password = quote_plus(db_password)
    database = env_values["POSTGRES_DB"]
    user = env_values["POSTGRES_USER"]
    server = env_values["POSTGRES_SERVER"]

    engine = create_engine(f"postgresql://{user}:{encoded_password}@{server}/{database}")
    try:
        with engine.connect() as connection_str:
            print(f'Successfully connected to the PostgreSQL "{database}" database')
    except Exception as ex:
        print(f"Sorry failed to connect: {ex}")

    return engine


eng = create_db_engine()
