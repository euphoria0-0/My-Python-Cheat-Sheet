#ref: https://keras.io/getting-started/faq/#how-can-i-obtain-reproducible-results-using-keras-during-development
import os
import random
import numpy as np
import tensorflow as tf
from tensorflow.keras import backend as K

sd = random.randint(0,99999999)
print(sd)

np.random.seed(sd)
random.seed(sd)
os.environ['PYTHONHASHSEED']=str(sd)

config = tf.ConfigProto(intra_op_parallelism_threads=1,inter_op_parallelism_threads=1)
tf.set_random_seed(sd)

sess = tf.Session(graph=tf.get_default_graph(), config=config)
K.set_session(sess)

tf.logging.set_verbosity(tf.logging.ERROR)