import tensorflow as tf
import numpy as np

import matplotlib.pyplot as plt

import pandas as pd
import os
import pathlib

np.set_printoptions(precision=4)

dataset = tf.data.Dataset.from_tensor_slices([8, 3, 0, 8, 2, 1])
dataset1 = tf.data.Dataset.from_tensor_slices(
    tf.random.uniform([4, 10], minval=1, maxval=10, dtype=tf.int32)
)

dataset1
for elem in dataset1:
    print(elem.numpy())

