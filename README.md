# TensorFlow-Notebooks

## cnn-1.ipynb
**My First Convolutional Neural Network**
This is a basic four-layer convolutional neural network originally taken from Udacity's deep learning course's Assignment 4. I heavily reorganized it, added some extra machine learning tricks, updated it for TensorFlow 1.0, and replaced some pieces of it with bits of Google's cifar10.py code.

## cnn-2.ipynb
**Second Convolutional Neural Network**

## apparatus-1.ipynb
**Skeletal Machine Learning Framework 1: "Pausable" training**
Demonstrates how to do long-term, indefinite training that is conducted in multiple, discrete sessions spread out over time.  This notebook can be used as a template for a machine learning experiment in which the training phase proceeds as follows:
- Hit the switch to start training (i.e. run the notebook).
- Open up TensorBoard and see the graph of the loss function, check out the kernels, etc.
- Wait for a while, refresh TensorBoard, and see how things are coming along.
- Hit a "pause button" and shut everything down for a while.
- Come back later, fire it up again, and it picks up right where it left off without misssing a beat.

The "pause button" is implemented by watching for the existence of a file (named "pause") in the training directory. Once such a file is detected, the model is saved, training shuts down, and the *pause* file is deleted (to prepare for the next training session).  

On Linux, training is paused with the shell command
```
touch /path/to/training/directory/pause
```

## generate\_data.ipynb
**Random Data Factory**
Small notebook to create a random 2D dataset, visualize it, and store it in a directory of CSV files to be read by a binary classifier.

## apparatus-2.ipynb
**Skeletal Machine Learning Framework 2: High-volume Logistic Regression with Pausable Training**
Demonstrates how to build a robust, multi-threaded input pipeline that rifles through a directory of CSV files, preparing shuffled batches of examples from them indefinitely.  *generate\_data.ipynb* can be used to create the input files.  Ends with the pausable training scheme used in *apparatus-1.ipynb*.

The input pipeline is used to train a simple logisitic regression model in a "pausable" training session (as developed in *apparatus-1.ipynb*.
