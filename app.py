from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def helloworld():
    return 'Bienvenido a todos'

@app.route('/predict')
def predict():
    return 'Predicciones'

if __name__ == "__main__":
    app.run()