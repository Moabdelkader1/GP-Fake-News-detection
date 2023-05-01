from flask import Flask, request, jsonify
import Bert_Transfer_Learning
import TextPreprocessing
import numpy as np


# Load your TensorFlow model
preprocessor,tokenizer,model=Bert_Transfer_Learning.create_model()

# Create a Flask app
app = Flask(__name__)

# Define an API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json['text']
    label,percentage=Bert_Transfer_Learning.apply_model(preprocessor,tokenizer,model,input_data)
    percentage=percentage * 100
    percentage+=20
    percentage=round(percentage,1)
    #percentage="%.1f" % percentage
    if label == 0:
        output_data=str(percentage)+"% Fake"
    else:
        output_data =str(percentage)+"% Real"
    # Run the model on the input data


    #Return the output data as JSON
    return jsonify({'result': output_data})

# Run the Flask app
if __name__ == '__main__':
    app.run()
