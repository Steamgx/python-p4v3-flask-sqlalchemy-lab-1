from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin  

db = SQLAlchemy()

class Earthquake(db.Model, SerializerMixin):  
    __tablename__ = "earthquakes"

    id = db.Column(db.Integer, primary_key=True)
    magnitude = db.Column(db.Float, nullable=False)
    location = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)

    serialize_rules = ("-id",)

    def to_dict(self):  # Explicitly define to_dict()
        return {
            "id": self.id,
            "magnitude": self.magnitude,
            "location": self.location,
            "year": self.year,
        }

    def __repr__(self):
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
