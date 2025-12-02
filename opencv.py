import cv2, os

haar_file = 'haarcascade_frontalface_default.xml'
datasets = 'dataset'
sub_Data = 'akanksha'

path = os.path.join(datasets, sub_Data)
if not os.path.isdir(path):
    os.makedirs(path)

(width, height) = (130, 100)

face_cascade = cv2.CascadeClassifier(haar_file)

# Check cascade loaded
if face_cascade.empty():
    print("Error: Cascade file not loaded!")
    exit()

webcam = cv2.VideoCapture(0)

count = 1
while count < 31:
    print(count)
    ret, im = webcam.read()
    
    if not ret:
        print("Camera not detected")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(im, (x, y), (x+w, y+h), (255, 0, 0), 2)
        face = gray[y:y + h, x:x + w]
        face_resize = cv2.resize(face, (width, height))
        cv2.imwrite('%s/%s.png' % (path, count), face_resize)
        count += 1

    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()
