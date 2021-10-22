import cv2
from random import randrange
# # This is for image only >> image detector

# # Load some pre-trained data on face frontals from opencv (haar cascade algorithm)
# trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# # Choose image to detect in
# img = cv2.imread('mr_bean.png')

# # Must convert to grayscale
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)


# # draw rectangle around the faces
# for (x, y, w, h) in face_coordinates:
# # (x, y, w, h) = face_coordinates[0]
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)

# # print(face_coordinates)

# #
# cv2.imshow('Clever Programmer Face Detector', img)
# cv2.waitKey()

# print("Code Complete")









# This is for video from webcam detector >> webcam detector.
trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture video from webcam
webcam = cv2.VideoCapture(0)

# iterate forever over frames
while True:
    # Read the current frame
    successful_frame_read, frame = webcam.read()

    # must convert to grayscale
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

    # draw rectangle around the faces
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (randrange(256), randrange(256), randrange(256)), 5)

    cv2.imshow('Clever Programmer Face Detector', frame)
    key = cv2.waitKey(1)

    # Stop if Q key is Pressed
    if key == 81 or key == 113:
        break
    
# release the video capture object
webcam.release()

print("Code Complete")