from urllib.parse import quote_plus
from pathlib import Path
from sqlalchemy import create_engine
from dotenv import dotenv_values


class DatabaseEngine:
    """
    A class used to create a SQLAlchemy engine object for the PostgreSQL database.

    ...

    Attributes
    ----------
    env_path : Path
        path to the .env file containing database configuration

    Methods
    -------
    create():
        Creates and returns a SQLAlchemy engine object for the PostgreSQL database.
    """

    def __init__(self):
        """
        Constructs all the necessary attributes for the DatabaseEngine object.
        """
        self.env_path = Path(__file__).parent / ".env"

    def create(self):
        """
        Creates and returns a SQLAlchemy engine object for the PostgreSQL database.

        Returns:
            engine: A SQLAlchemy engine object connected to the PostgreSQL database.

        Raises:
            Exception: If there is a problem connecting to the database.
        """
        env_values = dotenv_values(dotenv_path=self.env_path)

        db_password = env_values["POSTGRES_PASSWORD"]
        encoded_password = quote_plus(db_password)
        database = env_values["POSTGRES_DB"]
        user = env_values["POSTGRES_USER"]
        server = env_values["POSTGRES_SERVER"]

        engine = create_engine(
            f"postgresql://{user}:{encoded_password}@{server}/{database}"
        )
        try:
            with engine.connect() as connection_str:
                print(f'Successfully connected to the PostgreSQL "{database}" database')
        except Exception as ex:
            print(f"Sorry failed to connect: {ex}")

        return engine
