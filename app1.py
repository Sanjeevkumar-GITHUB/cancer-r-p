import numpy as np
import pickle
from flask import Flask, request, render_template

# Load ML model
model = pickle.load(open('canp_model.pkl', 'rb')) 

# Create application
app = Flask(__name__)

# Bind home function to URL
@app.route('/')
def home():
    return render_template('index.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [i for i in request.form.values()]
    # Convert features to array
    array_features = [np.array(features)]
    # Predict features
    prediction = model.predict(array_features)
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 3:
        return render_template('index.html', 
                               result = 'The patient is likely to have high risk!')
    elif output == 1:
        return render_template('index.html', 
                               result = 'The patient is likely to have low risk!')
    elif output == 2:
         return render_template('index.html', 
                               result = 'The patient is likely to have medium risk!')

if __name__ == '__main__':
#Run the application
    app.run()
