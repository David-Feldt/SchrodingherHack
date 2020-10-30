import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing

import pandas as pd
import numpy as np
import math

asteroid_data = pd.read_csv("C:/Users/BCimr/Documents/Schrodinger's Hack/SchrodingherHack/asteroid_data.csv")
asteroid_train = pd.read_csv("C:/Users/BCimr/Documents/Schrodinger's Hack/SchrodingherHack/asteroid_PHA_data.csv")

# preprocessing 
asteroid_data = np.array(asteroid_data)
asteroid_train = np.array(asteroid_train)
asteroid_data = asteroid_data[1:1000000,:12]
asteroid_train = asteroid_train[1:1000000,:]

maxs_data = np.zeros([12,1])

for j in range(12):
    print(j)
    maxs_data[j] = max(asteroid_data[:,j])
    
max_moid = max(asteroid_train[:,2])

# normalize

for i in range(len(asteroid_data)):

    if (asteroid_train[i][1] == 'Y'):
        asteroid_train[i][1] = 0.9999999

    else:
        asteroid_train[i][1] = 0.0

    if (asteroid_train[i][0] == 'Y'):
        asteroid_train[i][0] = 0.9999999
    else:
        asteroid_train[i][0] = 0.0
    for j in range(12):
        asteroid_data[i][j] /= maxs_data[j]
    asteroid_train[i][2] /= max_moid

# build and train model

lr = 0.1
model = tf.keras.models.Sequential([
        tf.keras.layers.Flatten(input_shape = (12,)),
        tf.keras.layers.Dense(30, activation = 'relu'),
        tf.keras.layers.Dense(30, activation = 'relu'),
        tf.keras.layers.Dense(30, activation = 'relu'),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(3, activation = 'softmax')

   ])

opt = keras.optimizers.Adam(learning_rate=0.9e-5)


model.compile(optimizer = opt,
                  loss = 'categorical_crossentropy',
                  metrics = ['accuracy'])

    
asteroid_data = np.asarray(asteroid_data).astype('float32')
asteroid_train = np.asarray(asteroid_train).astype('float32')
    

for i in range(5):
    model.fit(asteroid_data[20000*i:20000*(i+1),:],asteroid_train[20000*i:20000*(i+1),:],epochs = 1, verbose = 2)



    
