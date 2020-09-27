from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.preprocessing.image import ImageDataGenerator
from TakeAttendance.file_operations import *


class DataSet:
    def __init__(self, directory_path, image_size):
        self.directory_path = directory_path
        self.image_size = image_size

        self.train_path = f"{directory_path}/train_set"
        self.test_path = f"{directory_path}/test_set"
        self.number_object = len(os.listdir(self.train_path))

        self.classifier = Sequential()

    def createNeuralNetwork(self):
        shape = self.image_size + (1,)

        # Step 1 - Convolution
        self.classifier.add(
            Convolution2D(32, 3, 3, input_shape=shape, activation='relu'))  # 2 Dimensional neural network
        # image is 64x64 and it has 1 layer, so it is gray image (not color image)
        # Step 2 - Pooling
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))

        # 2. convolution layer
        self.classifier.add(Convolution2D(32, 3, 3, input_shape=shape, activation='relu'))
        self.classifier.add(MaxPooling2D(pool_size=(2, 2)))

        # Step 3 - Flattening
        self.classifier.add(Flatten())  # inputs are sorted in 1 row

        # Creating Neural Network
        # Step 4
        self.classifier.add(Dense(output_dim=128, activation='relu'))
        self.classifier.add(Dense(output_dim=self.image_size[0], activation='relu'))  # generally 64 pixel
        self.classifier.add(Dense(output_dim=self.number_object, activation='sigmoid'))

        # CNN
        self.classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    def process_images(self):
        train_datagen = ImageDataGenerator(rescale=1. / 255,
                                           shear_range=0.2,
                                           zoom_range=0.2,
                                           horizontal_flip=True)

        test_datagen = ImageDataGenerator(rescale=1. / 255,
                                          shear_range=0.2,
                                          zoom_range=0.2,
                                          horizontal_flip=True)

        training_set = train_datagen.flow_from_directory(self.train_path,
                                                         target_size=self.image_size,
                                                         color_mode="grayscale",
                                                         batch_size=1,
                                                         class_mode='categorical')

        test_set = test_datagen.flow_from_directory(self.test_path,
                                                    target_size=self.image_size,
                                                    color_mode="grayscale",
                                                    batch_size=1,
                                                    class_mode='categorical')

        self.classifier.fit_generator(training_set,
                                      samples_per_epoch=1000,
                                      nb_epoch=8,
                                      validation_data=test_set,
                                      nb_val_samples=2000)

    def save_model(self):
        # Saving the  model to  use it later on
        model_name = self.directory_path + "/" + getDirectoryName(self.directory_path)
        fer_json = self.classifier.to_json()
        with open(f"{model_name}.json", "w") as json_file:
            json_file.write(fer_json)

        self.classifier.save_weights(f"{model_name}.h5")
