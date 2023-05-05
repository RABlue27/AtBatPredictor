import tensorflow.keras as keras
import tensorflow as tf
import numpy as np
# Load the model from the file
model = keras.models.load_model("C:\\Users\\Alex\\Desktop\\School\\AtBatPredictor\\no_scaler_2.h5")


test = np.array([[572362, 570600, .156, .151, 45, 4,36.0]])

print(model.predict(test))