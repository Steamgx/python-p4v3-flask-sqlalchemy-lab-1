from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Earthquake  # Ensure you import db and Earthquake from models
from flask import jsonify

app = Flask(__name__)

# Configure the database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///earthquakes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)  # Ensure db is initialized with the app

migrate = Migrate(app, db)  # Ensure db is defined before this line

@app.route('/earthquakes/<int:id>', methods=['GET'])
def get_earthquake(id):
    earthquake = Earthquake.query.get(id)
    if earthquake:
        return jsonify({
            "id": earthquake.id,
            "location": earthquake.location,
            "magnitude": earthquake.magnitude,
            "year": earthquake.year
        }), 200
    else:
        return jsonify({"message": f"Earthquake {id} not found."}), 404

@app.route('/earthquakes/magnitude/<float:magnitude>', methods=['GET'])
def get_earthquakes_by_magnitude(magnitude):
    quakes = Earthquake.query.filter(Earthquake.magnitude >= magnitude).all()
    return jsonify({
        "count": len(quakes),
        "quakes": [{"id": quake.id, "location": quake.location, "magnitude": quake.magnitude, "year": quake.year} for quake in quakes]
    }), 200

if __name__ == "__main__":
    app.run(debug=True)
