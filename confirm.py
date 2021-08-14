#!/usr/bin/env python
import tensorflow as tf

print(f"Running TensorFlow {tf.__version__} with {len(tf.config.list_physical_devices('GPU'))} GPUs recognized")
