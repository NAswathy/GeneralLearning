#%tensorflow_version 2.x
try:
    import tensorflow
    tensorflow.__version__
except ImportError:
    print("TensorFlow not installed. Please install it using: pip install tensorflow")

# Initialize the random number generator
import random
random.seed(0)

# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")

import numpy as np
x = np.array([1, 3, 6, 5, 4, 7, 1, 6, 10, 13, 5])
y = np.array([3, 7, 13, 11, 9, 15, 3, 13, 21, 27, 11])

model = tensorflow.keras.models.Sequential([
          tensorflow.keras.layers.Flatten(),
          tensorflow.keras.layers.Dense(1)
])
model.compile(optimizer='sgd', loss='mean_squared_error')
model.fit(x, y, epochs=50)

