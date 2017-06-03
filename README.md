# TensorFlow-Notebooks

## cnn-1.ipynb
This is a basic four-layer convolutional neural network originally taken from Udacity's deep learning course's Assignment 4. I heavily reorganized it, added some extra machine learning tricks, updated it for TensorFlow 1.0, and replaced some pieces of it with bits of Google's cifar10.py code.

## PausibleTraining.ipynb
Skeletal framework for long-term, indefinite training that is conducted in multiple, discrete sessions spread out over time.  Using this as a template for a machine learning experiment, the training phase works like this:
- Hit the switch to start training.
- Open up TensorBoard and see the graph of the loss function, check out the kernels, etc.
- Wait for a while, refresh TensorBoard, and see how things are coming along.
- Hit some kind of "pause button" and shut everything down for a while.
- Come back later, fire it up again, and it picks up right where it left off without misssing a beat.
