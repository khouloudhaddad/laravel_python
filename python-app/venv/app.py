from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@mysql:3306/your_database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Text, nullable=False)

@app.route('/data', methods=['GET'])
def get_data():
    all_data = Data.query.all()
    return jsonify([{'id': d.id, 'key': d.key, 'value': d.value} for d in all_data]), 200

@app.route('/data', methods=['POST'])
def create_data():
    if not request.json or 'key' not in request.json or 'value' not in request.json:
        return jsonify({'error': 'Invalid input'}), 400

    new_data = Data(key=request.json['key'], value=request.json['value'])
    db.session.add(new_data)
    db.session.commit()
    return jsonify({'id': new_data.id, 'key': new_data.key, 'value': new_data.value}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)