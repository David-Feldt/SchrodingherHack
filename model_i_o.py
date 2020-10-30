<<<<<<< HEAD
import tensorflow as tf
from tensorflow import keras
import numpy as np

# take input
inp = np.zeros([2,12])

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

model.load_weights('final_checkpoint')

#spit out output

out = model.predict(inp)
out = out[:1,:]
if out[0][0] < 0.5:
    out[0][0] = 0.0
else:
    out[0][0] = 1.0
if out[0][1] < 0.5:
    out[0][1] = 0.0
else:
    out[0][1] = 1.0
=======
import tensorflow as tf
from tensorflow import keras
import numpy as np

# take input
inp = np.zeros([2,12])

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

model.load_weights('final_checkpoint')

#spit out output

out = model.predict(inp)
out = out[:1,:]
if out[0] < 0.5:
    out[0] = 0.0
else:
    out[0] = 1.0
if out[1] < 0.5:
    out[1] = 0.0
else:
    out[1] = 1.0
>>>>>>> e0591ec2d8da38e414e94887d564cf027a8b8bde
