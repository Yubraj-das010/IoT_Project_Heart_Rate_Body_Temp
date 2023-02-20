import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model_regressor.pkl", 'rb'))

@app.route("/")
def home():
    return render_template('index_regressor.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0])

    return render_template('index_regressor.html', prediction_text='Heart rate of the patient is supposed to be {} beats/min'.format(output))


if __name__ == "__main__":
    app.run(debug=True)

'''if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)'''
