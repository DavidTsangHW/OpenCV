import cv2
vidcap = cv2.VideoCapture('t2.mp4')
success,image = vidcap.read()
count = 0
while success:
  if count >= 1:
    cv2.imwrite("img2\\frame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ' + str(count), success)
  count = count + 1
