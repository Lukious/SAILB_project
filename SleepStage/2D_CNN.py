#######################Change 2D_CNN MNIST to 3000 by 6 #####################
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
import numpy as np
np.random.seed(7)

print('Python version : ', sys.version)
print('TensorFlow version : ', tf.__version__)
print('Keras version : ', keras.__version__)

img_rows = 3000 
img_cols = 6

(x_train, y_train), (x_test, y_test) = #"NEED to change"# #keras.datasets.mnist.load_data()

input_shape = (img_rows, img_cols, 1)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

batch_size = 128
num_classes = 10
epochs = 12

model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), padding='same',
                 activation='relu',
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (2, 2), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.summary()


y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(x_train, y_train,
                 batch_size=batch_size,
                 epochs=epochs,
                 verbose=1, 
                 validation_data=(x_test, y_test))


score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1]

#######################Success to operate MNIST#####################
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import sys
import tensorflow as tf
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers.convolutional import Conv2D, MaxPooling2D
import numpy as np
np.random.seed(7)

print('Python version : ', sys.version)
print('TensorFlow version : ', tf.__version__)
print('Keras version : ', keras.__version__)

img_rows = 28 
img_cols = 28

(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

input_shape = (img_rows, img_cols, 1)
x_train = x_train.reshape(x_train.shape[0], img_rows, img_cols, 1)
x_test = x_test.reshape(x_test.shape[0], img_rows, img_cols, 1)

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.

print('x_train shape:', x_train.shape)
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

batch_size = 128
num_classes = 10
epochs = 12

model = Sequential()
model.add(Conv2D(32, kernel_size=(5, 5), strides=(1, 1), padding='same',
                 activation='relu',
                 input_shape=input_shape))
model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
model.add(Conv2D(64, (2, 2), activation='relu', padding='same'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(1000, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(num_classes, activation='softmax'))
model.summary()


y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
hist = model.fit(x_train, y_train,
                 batch_size=batch_size,
                 epochs=epochs,
                 verbose=1, 
                 validation_data=(x_test, y_test))


score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1]


###########################Fail to operate###########################
#import keras
#from keras.datasets import mnist

##load mnist dataset
#(X_train, y_train), (X_test, y_test) = mnist.load_data()

#import matplotlib.pyplot as plt
#fig = plt.figure()
#for i in range(9):
#  plt.subplot(3,3,i+1)
#  plt.tight_layout()
#  plt.imshow(X_train[i], cmap='gray', interpolation='none')
#  plt.title("Digit: {}".format(y_train[i]))
#  plt.xticks([])
#  plt.yticks([])
#fig

#reshaping
#this assumes our data format
#For 3D data, "channels_last" assumes (conv_dim1, conv_dim2, conv_dim3, channels) while 
#"channels_first" assumes (channels, conv_dim1, conv_dim2, conv_dim3).
#if k.image_data_format() == 'channels_first':
#    X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
#    X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)
#    input_shape = (1, img_rows, img_cols)
#else:
#    X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1)
#    X_test = X_test.reshape(X_test.shape[0], img_rows, img_cols, 1)
#    input_shape = (img_rows, img_cols, 1)
##more reshaping
#X_train = X_train.astype('float32')
#X_test = X_test.astype('float32')
#X_train /= 255
#X_test /= 255
#print('X_train shape:', X_train.shape) #X_train shape: ( 20000, 3000, 6, 1) #[3000,6]

##import keras
##set number of categories
#num_category = 10
## convert class vectors to binary class matrices
#y_train = keras.utils.to_categorical(y_train, num_category)
#y_test = keras.utils.to_categorical(y_test, num_category)

##model building
#model = Sequential()

#convolutional layer with rectified linear unit activation
#model.add(Conv2D(32, kernel_size=(6, 6), # 6by6
#                 activation='relu',
#                 input_shape=input_shape))

#32 convolution filters used each of size 3x3 -> 6x6
#again
#model.add(Conv2D(64, (6, 6), activation='relu')) # 3 x 3 -> 6 x 6

#64 convolution filters used each of size 6x6
#choose the best features via pooling
#model.add(MaxPooling2D(pool_size=(2, 2)))

#randomly turn neurons on and off to improve convergence
#model.add(Dropout(0.25))

#flatten since too many dimensions, we only want a classification output
#model.add(Flatten())

#fully connected to get all relevant data
#model.add(Dense(128, activation='relu'))

#one more dropout for convergence' sake :) 
#model.add(Dropout(0.5))

#output a softmax to squash the matrix into output probabilities
#model.add(Dense(num_category, activation='softmax'))

#Adaptive learning rate (adaDelta) is a popular form of gradient descent rivaled only by adam and adagrad
#categorical ce since we have multiple classes (10) 
#model.compile(loss=keras.losses.categorical_crossentropy,
#              optimizer=keras.optimizers.Adadelta(),
#              metrics=['accuracy'])

#batch_size = 128
#num_epoch = 10

#model training
#model_log = model.fit(X_train, y_train,
#          batch_size=batch_size,
#          epochs=num_epoch,
#          verbose=1,
#          validation_data=(X_test, y_test))

#score = model.evaluate(X_test, y_test, verbose=0)
#print('Test loss:', score[0]) 				#Test loss: 0.0296396646054
#print('Test accuracy:', score[1])			#Test accuracy: 0.9904

#Save the model
# serialize model to JSON
##model_digit_json = model.to_json()
#with open("model_digit.json", "w") as json_file:
#    json_file.write(model_digit_json)
# serialize weights to HDF5
#model.save_weights("model_digit.h5")
#print("Saved model to disk")
