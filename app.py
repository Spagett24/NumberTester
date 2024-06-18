from flask import Flask, request, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# Replace with your actual MongoDB connection string
app.config["MONGO_URI"] = "mongodb+srv://vpapolu24:pcjhhWPxD7MjjFYD@cluster0.jkvndbj.mongodb.net/test?retryWrites=true&w=majority"
mongo = PyMongo(app)

@app.route('/submit-number', methods=['POST'])
def submit_number():
    data = request.get_json()
    number = data.get('number')

    if len(number) == 10 and number.isdigit():
        mongo.db.numbers.insert_one({'number': number})
        return jsonify({'message': 'Number saved successfully'}), 201
    else:
        return jsonify({'error': 'Please enter a valid 10-digit number.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
