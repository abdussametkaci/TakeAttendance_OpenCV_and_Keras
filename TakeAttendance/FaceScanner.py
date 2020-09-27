import cv2
from TakeAttendance.file_operations import *
from random import sample  # create random numbers uniquely
from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np


class FaceScanner:
    def __init__(self):
        self.face_casc = cv2.CascadeClassifier(r"haarcascades\haarcascade_frontalface_default.xml")
        self.objects = []

    def scan_person(self, person_name, path):
        open_dir(path + "/" + person_name)
        cam = cv2.VideoCapture(0)

        counter = 0

        while True:
            ret, frame = cam.read()

            label = f"{path}/{person_name}/{counter}.jpg"
            resized_frame = cv2.resize(frame, (1000, 1000))
            cv2.imwrite(label, resized_frame)
            counter += 1

            cv2.imshow("Face", frame)

            if cv2.waitKey(25) == ord('q'):  # wait until 'q' key is pressed
                break

        cam.release()
        cv2.destroyAllWindows()

    def preprocess_images(self, path, to_directory):
        clearDir(to_directory)
        for (root, dirs, files) in os.walk(path, topdown=True):
            if files:
                newPath = f"{to_directory}/" + getDirecoryFromPath(root, getDirectoryName(path))

                open_dir(newPath)
                counter = 0

                for file in files:
                    image = cv2.imread(root + "/" + file)

                    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

                    faces = self.face_casc.detectMultiScale(gray_image, 1.3, 5)

                    for (x, y, w, h) in faces:
                        gray_face = gray_image[y:y + h, x:x + w]
                        faces2 = self.face_casc.detectMultiScale(gray_face, 1.3, 5)
                        for (x2, y2, w2, h2) in faces2:
                            face = gray_face[y2:y2 + h2, x2:x2 + w2]
                            face = cv2.resize(face, (64, 64))
                            cv2.imwrite(newPath + "/" + file, face)

                            newFileName = f"{counter}.jpg"
                            renameFile(newPath + "/" + file, newPath + "/" + newFileName)
                            counter += 1

    def getObjects(self, path):
        return list(os.listdir(path))

    def split_test_train(self, split_path, to_path):
        self.objects = self.getObjects(split_path)
        (root, dirs, _files) = list(os.walk(split_path, topdown=True))[0]

        for dir in dirs:
            files = os.listdir(f"{split_path}/{dir}")

            counter = 0
            open_dir(f"{to_path}/train_set/{dir}")
            open_dir(f"{to_path}/test_set/{dir}")

            number_file = len(files)

            train_num = int(number_file * 0.66)
            # test_num = number_file - train_num

            a = sample(range(0, number_file), number_file)  # uniquely random indexes
            # print(a)

            for i in a:
                if counter < train_num:
                    image = read(f"{split_path}/{dir}/{i}.jpg")
                    write(f"{to_path}/train_set/{dir}/{i}.jpg", image)
                else:
                    image = read(f"{split_path}/{dir}/{i}.jpg")
                    write(f"{to_path}/test_set/{dir}/{i}.jpg", image)

                counter += 1

    def load_model(self, model_name):
        # load model
        model = model_from_json(open(f"{model_name}.json", "r").read())
        # load weights
        model.load_weights(f'{model_name}.h5')

        return model

    def recognize_face(self, model_name, path=""):
        model = self.load_model(model_name)
        foundeds = []

        if path:
            mode = path   # video file
        else:
            mode = 0      # open cam

        cap = cv2.VideoCapture(mode)

        while True:
            ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
            if not ret:
                break

            gray_img = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

            faces_detected = self.face_casc.detectMultiScale(gray_img, 1.3, 5)

            for (x, y, w, h) in faces_detected:
                cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)
                roi_gray = gray_img[y:y + h, x:x + w]  # cropping region of interest i.e. face area from  image
                roi_gray = cv2.resize(roi_gray, (64, 64))

                img_pixels = image.img_to_array(roi_gray)
                img_pixels = np.expand_dims(img_pixels, axis=0)
                img_pixels /= 255

                predictions = model.predict(img_pixels)

                # find max indexed array
                max_index = np.argmax(predictions[0])

                predicted = self.objects[max_index]

                percent = predictions[0][max_index] * 100

                if percent >= 80:
                    self.addUniquely(predicted, foundeds)

                label = "{}: {:.2f}".format(predicted, percent)
                cv2.putText(test_img, label, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # resized_img = cv2.resize(test_img, (1000, 700))
            cv2.imshow('Face', test_img)

            if cv2.waitKey(25) == ord('q'):  # wait until 'q' key is pressed
                break

        cap.release()
        cv2.destroyAllWindows()

        return foundeds

    def addUniquely(self, item, _list):
        if not item in _list:
            _list.append(item)

    """
       def scan_faces(self, person_name, path):
           open_dir(path + "/" + person_name)
           cam = cv2.VideoCapture(0)

           counter = 0

           while True:
               ret, frame = cam.read()
               gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

               faces = self.face_casc.detectMultiScale(gray_frame, 1.3, 5)

               for (x, y, w, h) in faces:
                   cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                   gray_face = gray_frame[y:y + h, x:x + w]
                   label = f"{path}/{person_name}/{counter}.jpg"
                   gray_face = cv2.resize(gray_face, (64, 64))
                   cv2.imwrite(label, gray_face)
                   counter += 1

               cv2.imshow("Face", frame)

               if cv2.waitKey(25) == ord('q'):  # wait until 'q' key is pressed
                   break

           cam.release()
           cv2.destroyAllWindows()
       """
