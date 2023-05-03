import tensorflow as tf
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Parameters
NUM_EPOCHS = 1500
BATCH_SIZE = 128
VALIDATION_SPLIT = 0.2
LEARNING_RATE = 0.01
OPTIMIZER = Adam(learning_rate=LEARNING_RATE, clipvalue=1.0)
VERBOSE = 2

# Load Data
dataset = pd.read_csv('combined-stats.csv')
dataset = dataset.dropna()
X = dataset[['batter', 'pitcher', 'babip_value', 'iso_value', 'game_temp', 'game_wind', 'game_humidity']].values
Y = dataset['woba_value'].values.reshape(-1, 1)

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)


# Normalize inputs by scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Define the neural network architecture
model = Sequential()
model.add(Dense(64, input_dim=7, activation='sigmoid', kernel_initializer='glorot_uniform'))
model.add(Dense(128,  activation='sigmoid', kernel_initializer='glorot_uniform'))
model.add(Dense(128, activation='sigmoid', kernel_initializer='glorot_uniform'))
model.add(Dense(64, activation='sigmoid', kernel_initializer='glorot_uniform'))
model.add(Dense(32,  activation='sigmoid', kernel_initializer='glorot_uniform'))
model.add(Dense(1, activation='linear', kernel_initializer='glorot_uniform'))


model.compile(loss='mean_squared_error', optimizer=OPTIMIZER, metrics=['mse'])
# Train the model


model.fit(X_train, Y_train, epochs=NUM_EPOCHS, batch_size=BATCH_SIZE, validation_data=(X_test, Y_test), verbose=VERBOSE)



model.save("short.h5")

# Evaluate the model on the testing set
loss, mse = model.evaluate(X_test, Y_test, verbose=0)
print('Mean Squared Error:', mse)
print("Loss: ", loss)

# Obtain model's predictions
y_pred = model.predict(X_test)

print("output")

# Print some predicted and true values
for i in range(20):
    print("Predicted: {:.2f}, True: {:.2f}".format(y_pred[i][0], Y_test[i][0]))