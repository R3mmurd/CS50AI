# Project 5: Neural Networks

## Traffic

An AI to identify which traffic sign appears in a photograph.

### Background

As research continues in the development of self-driving cars, one of the key challenges is computer vision,
allowing these cars to develop an understanding of their environment from digital images. In particular, this
involves the ability to recognize and distinguish road signs – stop signs, speed limit signs, yield signs, and more.

In this project, you’ll use TensorFlow to build a neural network to classify road signs based on an image of
those signs. To do so, you’ll need a labeled dataset: a collection of images that have already been categorized
by the road sign represented in them.

Several such data sets exist, but for this project, we’ll use the German Traffic Sign Recognition Benchmark (GTSRB)
dataset, which contains thousands of images of 43 different kinds of road signs.

### Getting Started

- Download the [data set](https://cdn.cs50.net/ai/2020/x/projects/5/gtsrb.zip) for this project and unzip it.
  Move the resulting gtsrb directory inside of your traffic directory.

- Inside of the traffic directory, `run pip3 install -r requirements.txt` to install this project’s dependencies:
  opencv-python for image processing, scikit-learn for ML-related functions, and tensorflow for neural networks.

### Usage
```bash
$ python traffic.py gtsrb
Epoch 1/10
500/500 [==============================] - 5s 9ms/step - loss: 3.7139 - accuracy: 0.1545
Epoch 2/10
500/500 [==============================] - 6s 11ms/step - loss: 2.0086 - accuracy: 0.4082
Epoch 3/10
500/500 [==============================] - 6s 12ms/step - loss: 1.3055 - accuracy: 0.5917
Epoch 4/10
500/500 [==============================] - 5s 11ms/step - loss: 0.9181 - accuracy: 0.7171
Epoch 5/10
500/500 [==============================] - 7s 13ms/step - loss: 0.6560 - accuracy: 0.7974
Epoch 6/10
500/500 [==============================] - 9s 18ms/step - loss: 0.5078 - accuracy: 0.8470
Epoch 7/10
500/500 [==============================] - 9s 18ms/step - loss: 0.4216 - accuracy: 0.8754
Epoch 8/10
500/500 [==============================] - 10s 20ms/step - loss: 0.3526 - accuracy: 0.8946
Epoch 9/10
500/500 [==============================] - 10s 21ms/step - loss: 0.3016 - accuracy: 0.9086
Epoch 10/10
500/500 [==============================] - 10s 20ms/step - loss: 0.2497 - accuracy: 0.9256
333/333 - 5s - loss: 0.1616 - accuracy: 0.9535
```

## Demo

<a href="http://www.youtube.com/watch?feature=player_embedded&v=SnZeJ6aCYJQ
" target="_blank"><img src="http://img.youtube.com/vi/SnZeJ6aCYJQ/0.jpg"
alt="Demo Traffic" width="240" height="180" border="10" /></a>
