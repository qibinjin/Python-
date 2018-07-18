
from keras.models import Sequential
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense,Dropout
from keras import backend as K

class SmallerVGGNet(object):
    @staticmethod
    def build(width, height, depth, classes, finalAct = 'softmax'):
        model = Sequential()
        inputShape = (height, width, depth)
        chanDim = -1
        if K.image_data_format() == 'channels_first':
            inputShape = (depth, height, width)
            chanDim = 1
        model.add(Conv2D(32, (3, 3), padding = 'same', 
                         input_shape = inputShape))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(MaxPooling2D(pool_size = (3, 3)))
        model.add(Dropout(0.25))
        
        model.add(Conv2D(64, (3, 3), padding = 'same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(Conv2D(64, (3, 3), padding = 'same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(MaxPooling2D(pool_size = (2, 2)))
        model.add(Dropout(0.25))
        
        model.add(Conv2D(128, (3, 3), padding = 'same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(Conv2D(128, (3, 3), padding = 'same'))
        model.add(Activation('relu'))
        model.add(BatchNormalization(axis = chanDim))
        model.add(MaxPooling2D(pool_size = (2, 2)))
        model.add(Dropout(0.25))
        
        model.add(Flatten())
        model.add(Dense(1024))
        model.add(Activation('relu'))
        model.add(BatchNormalization())
        model.add(Dropout(0.25))
        
        model.add(Dense(classes))
        model.add(Activation(finalAct))
        
        return model