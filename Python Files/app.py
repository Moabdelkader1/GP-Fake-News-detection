from flask import Flask, request, jsonify
import tensorflow as tf
import TextPreprocessing
import numpy as np

# Load your TensorFlow model
model = tf.keras.models.load_model('rnn.h5')
print("here")

# Create a Flask app
app = Flask(__name__)

# Define an API endpoint for predictions
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    input_data = request.json['text']
    input_text = TextPreprocessing.preprocess_text(input_data)
    tfidf_mat, reduced_mat = TextPreprocessing.applytfidf_1string([input_text])
    reduced_flt = reduced_mat.toarray().astype(np.float32)
    prediction=model.predict(reduced_flt)

    label = round(prediction[0][0])
    if label == 0:
        output_data="Fake"
    else:
        output_data ="Real"
    # Run the model on the input data


    # Return the output data as JSON
    return jsonify({'result': output_data})

# Run the Flask app
if __name__ == '__main__':
    app.run()
