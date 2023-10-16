from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

with open('dv.bin', 'rb') as f:
    dv = pickle.load(f)

with open('model1.bin', 'rb') as f:
    model = pickle.load(f)


@app.route('/predict', methods=['POST'])
def predict():
    client_data = request.json
    X = dv.transform([client_data])
    probability = model.predict_proba(X)[:, 1][0]
    return jsonify({'probability': probability})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
