import cv2
import numpy as np
import os

# Dataset folder
dataset = 'dataset'
haar_file = 'haarcascade_frontalface_default.xml'

print("Training...")

# Prepare training data
(images, labels, names, id) = ([], [], {}, 0)

for subdir in os.listdir(dataset):
    names[id] = subdir
    subjectpath = os.path.join(dataset, subdir)

    for filename in os.listdir(subjectpath):
        path = os.path.join(subjectpath, filename)
        img = cv2.imread(path, 0)

        if img is not None:
            images.append(img)
            labels.append(id)

    id += 1

# Convert to numpy arrays
(images, labels) = [np.array(lis) for lis in [images, labels]]

# Train model
model = cv2.face.LBPHFaceRecognizer_create()
model.train(images, labels)

# Load classifier
face_cascade = cv2.CascadeClassifier(haar_file)
webcam = cv2.VideoCapture(0)

while True:
    ret, img = webcam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        face_resize = cv2.resize(face, (130, 100))

        prediction = model.predict(face_resize)

        if prediction[1] < 80:
            name = names[prediction[0]]
            cv2.putText(img, name, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        else:
            cv2.putText(img, "Unknown", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 0), 2)

    cv2.imshow("Face Recognition", img)

    if cv2.waitKey(10) == 27:  # Press ESC to EXIT
        break

webcam.release()
cv2.destroyAllWindows()
