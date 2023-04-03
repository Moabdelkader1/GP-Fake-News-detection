from keras.models import Sequential
from keras.layers import Embedding,LSTM,Dense,SpatialDropout1D,Dropout



def create_model1(numoffeatures):
    model=Sequential()
    model.add(Embedding(input_dim=numoffeatures,output_dim=50))
    model.add(LSTM(units=64))
    model.add(Dense(1,activation='sigmoid'))
    model.summary()
    model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])
    return model

def create_model2(numoffeatures):
    model_lstm = Sequential()
    model_lstm.add(Embedding(input_dim=numoffeatures, output_dim=256,))
    model_lstm.add(SpatialDropout1D(0.3))
    model_lstm.add(LSTM(256, dropout=0.3, recurrent_dropout=0.3))
    model_lstm.add(Dense(256, activation='relu'))
    model_lstm.add(Dropout(0.3))
    model_lstm.add(Dense(1, activation='sigmoid'))
    model_lstm.compile(
        loss='categorical_crossentropy',
        optimizer='Adam',
        metrics=['accuracy']
    )
    return model_lstm
