#!/usr/bin/env python
import tensorflow as tf
tf.debugging.set_log_device_placement(True)

print(f"Running TensorFlow {tf.__version__} with {len(tf.config.list_physical_devices('GPU'))} GPUs recognized")

with tf.device('/gpu:0'):
  d = tf.random_normal([])
  print(d)

