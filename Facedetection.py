import cv2

#enabling camera
face_cap = cv2.CascadeClassifier("C:/Users/Ayush/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    colour = cv2.cvtColor(video_data, cv2.COLOR_BGR2GRAY)
    face  = face_cap.detectMultiScale(
        colour,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30, 30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    for(x, y, w, h) in face:
        cv2.rectangle(video_data, (x,y), (x+w, y+h), (0,225,0), 2)
        
        
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(1) == ord("q") :
        break
    
video_cap.release()

