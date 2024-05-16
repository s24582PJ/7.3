from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@database:5432/mydatabase'
db = SQLAlchemy(app)

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)

@app.route('/cars', methods=['GET'])
def get_cars():
    year = request.args.get('year')
    if year:
        cars = Car.query.filter_by(year=year).all()
    else:
        cars = Car.query.all()
    return jsonify([{'id': car.id, 'make': car.make, 'model': car.model, 'year': car.year} for car in cars])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
