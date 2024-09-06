from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import MetaData

app = Flask(__name__)

# Asegúrate de que el nombre de la clave esté bien escrita
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:35912768@localhost:5432/postgres"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Definir la clase base con la convención de nombres personalizada
class Base(DeclarativeBase):
    metadata = MetaData(naming_convention={
        "ix": 'ix_%(column_0_label)s',
        "uq": "uq_%(table_name)s_%(column_0_name)s",
        "ck": "ck_%(table_name)s_%(constraint_name)s",
        "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
        "pk": "pk_%(table_name)s"
    })
    __table_args__ = {'schema': 'flask_test'}  # Establece el esquema por defecto
db = SQLAlchemy(app, model_class=Base)