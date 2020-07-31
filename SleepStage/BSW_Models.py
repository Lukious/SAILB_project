from __future__ import absolute_import, division, print_function, unicode_literals, unicode_literals


import BSW_Loader


import tensorflow as tf
from keras.models import Sequential
from keras import optimizers
from keras.layers import Dense, Activation, Flatten, Conv2D, MaxPooling2D
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tf.Session()

print(tf.__version__)

if __name__ == '__main__': 
    X,Y = BSW_Loader.Data()
    X = np.array(X)
    print(X.shape)
    print(len(Y))
    
    X = np.array(X).reshape(-1, 6, 3000, 1)
    Y = np.array(Y)
    
    print("Load is Done")

    #keras.layers.Flatten(input_shape=(6, 3000)),
    model = Sequential()

    model.add(Conv2D(input_shape = (X.shape[1], X.shape[2], X.shape[3]), filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))
    model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    model.add(Conv2D(filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    #model.add(MaxPooling2D(pool_size = (5,5)))

    # prior layer should be flattend to be connected to dense layers
    model.add(Flatten())
    # dense layer with 50 neurons
    model.add(Dense(50, activation = 'relu'))
    # final layer with 10 neurons to classify the instances
    model.add(Dense(5, activation = 'softmax'))

    adam = optimizers.Adam(lr = 0.001)


    '''
    model.add(Conv2D(input_shape = (X.shape[1], X.shape[2], X.shape[3]), filters = 50, kernel_size = (3,3), strides = (1,1), padding = 'same'))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size = (2,2)))
    '''
    #keras.layers.Conv2D(filters= 128,strides = (1,1),kernel_size= (3,3),activation= 'relu',padding = 'valid',name = 'C1'),
    #keras.layers.MaxPooling2D(pool_size = (2,2)),
    #keras.layers.Conv2D(filters= 64,strides = (1,1),kernel_size= (3,3),activation= 'relu',padding = 'valid',name = 'C2'),
    #eras.layers.MaxPooling2D(pool_size = (2,2)),
    #keras.layers.Flatten(),
    #keras.layers.Dense(128, activation='relu'),
    #keras.layers.Dense(5, activation='softmax')
    #])
    
    model.compile(loss = 'sparse_categorical_crossentropy', optimizer = adam, metrics = ['accuracy'])
    model.summary()
    model.fit(X, Y, batch_size = 50, validation_split = 0.2, epochs = 100, verbose = 0)
    #history = model.fit(X, Y, batch_size = 50, validation_split = 0.2, epochs = 100, verbose = 0)

    plt.plot(history.history['acc'])
    plt.plot(history.history['val_acc'])
    plt.legend(['training', 'validation'], loc = 'upper left')
    plt.show()

    #Test Process
    # Todo for Test!!!
    results = model.evaluate(X, Y)
    print('Test accuracy: ', results[1])

    ################################
    #test_loss, test_acc = model.evaluate(X,  Y, verbose=2) #Should Be Test
    #predictions = model.predict(X)  #Should Be Test
    #print(np.argmax(predictions[0]))
    #print(Y[0])

