#test install of tensorflow
import tensorflow as tf

hello = tf.constant('Hello from TensorFlow!')
sess = tf.Session()
print(sess.run(hello))