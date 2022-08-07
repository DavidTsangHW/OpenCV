import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')

# To capture video from webcam. 
#cap = cv2.VideoCapture(0)
# To use a video file as input 
cap = cv2.VideoCapture('HPIM180523-185249F.mov')

outputDir="plates\\"
iCount = 0

while True:
    # Read the frame
    iCount = iCount + 1    
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    # 1.05- Down scaling by 5% each time
    faces = face_cascade.detectMultiScale(gray, 1.03, 6)

    fCount = 0
    for (x, y, w, h) in faces:
        fCount = fCount + 1
        fileName = str(iCount) + "-" + str(fCount)
        
        
        w2 = w*2
        h2= h*2
        x2 = x - w2
        y2 = y - h2
        if x2 <1:
            x2 = 1
        if y2 <1:
            y2 = 1
        
        #print(x, x2, y, y2)
        
        face = img[y:y+h, x:x+w] #slice the face from the image

        if iCount >= 1:

            cv2.imwrite(outputDir + fileName +'.jpg', face) #save the image        

            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    #Display
    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k==27 or iCount >= 1459:
        break
    
# Release the VideoCapture object
cap.release()
