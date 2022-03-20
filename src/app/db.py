import sqlalchemy
from databases import Database
from src.app.settings import settings

db = Database(settings.db_dsn, force_rollback=(settings.environment == "TESTING"))
metadata = sqlalchemy.MetaData()
