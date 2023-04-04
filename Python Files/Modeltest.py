import tensorflow as tf
from tensorflow import keras
import numpy as np
import TextPreprocessing
model=keras.models.load_model('rnn.h5')
text='وفي مقطع من فيديو الاستجواب الذي نشرته السلطات الروسية،'
text_arr=[]
input_data = text
input_text=TextPreprocessing.preprocess_text(input_data)
tfidf_mat,reduced_mat=TextPreprocessing.applytfidf_1string([input_text])
reduced_int=reduced_mat.toarray().astype(np.float32)

# Run the model on the input data
predictions=model.predict(reduced_int)
print(predictions[0][0])

label=round(predictions[0][0])
print(label)
if label==0:
    print("Fake")
else:
    print("Real")
