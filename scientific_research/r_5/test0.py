import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

inp_shp = (4, 250, 250, 3)
ran = tf.random.normal(inp_shp)
lay = layers.Conv2D(16, 2, padding='same', activation='relu', input_shape=inp_shp[1:])
out = lay(ran)
lay = layers.MaxPooling2D()
out = lay(out)
print(out.shape)
