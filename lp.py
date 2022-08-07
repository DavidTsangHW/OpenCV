#License plate

import cv2
import numpy as np
import pytesseract
import os
from os import walk


def readText(filePath):

    filename = os.path.basename(filePath)
    filename = filename.split('.')[0]


    image = cv2.imread(filePath)
    img = image.copy()

    custom_config ='--oem 3 --psm 5 tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    ret = pytesseract.image_to_string(img, config=custom_config)
    print(ret)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    

    img = cv2.bilateralFilter(img, 11, 17, 17)
    img = cv2.Canny(img, 30, 200)

 
    cnts,new = cv2.findContours(img.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    image1 = image.copy()

    cv2.drawContours(image1,cnts,-1,(0,255,0),3)

    cnts = sorted(cnts, key = cv2.contourArea, reverse = True) [:30]
    screenCnt = None
    image2 = img.copy()
    cv2.drawContours(image2,cnts,-1,(0,255,0),3)
    
    i = 0
    for c in cnts:
        perimeter = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * perimeter, True)
        if len(approx) >= 4:
            screenCnt = approx
            x,y,w,h = cv2.boundingRect(c) 
            new_img= image[y:y+h,x:x+w]
            gry = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
            blr = cv2.GaussianBlur(gry, (3, 3), 0)
            #blr = gry
            thr = cv2.threshold(blr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

            new_img = thr

            (h_thr, w_thr) = thr.shape[:2]
            s_idx = 0
            e_idx = int(h_thr/2)

            for _ in range(0, 2):
                crp = thr[s_idx:e_idx, 0:w_thr]
                (h_crp, w_crp) = crp.shape[:2]
                crp = cv2.resize(crp, (w_crp*2, h_crp*2))
                crp = cv2.erode(crp, None, iterations=1)
                s_idx = e_idx
                e_idx = s_idx + int(h_thr/2)

                ret = pytesseract.image_to_string(new_img, config=custom_config)
                #print(txt)
                #cv2.imshow("crp", crp)
                #cv2.waitKey(0)


            
            
            cv2.imwrite('./plates/'+ filename + '-' +str(i)+'.png',new_img)
            i+=1

            #ret = pytesseract.image_to_string(new_img, config=custom_config)
            if len(ret)> 4:
                print(ret)


path = "img4\\"

fs = os.listdir(path)

for f in fs:
    readText(path + "\\" + f)




