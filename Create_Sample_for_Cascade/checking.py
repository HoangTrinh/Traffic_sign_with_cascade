import cv2
import os
def check(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
    with open('info.dat') as readf:
        stemp = readf.read()
    i= 0
    for line in stemp.split('\n'):
        line = line.replace('/', ' ')
        c = line.split()
        name = c[1]
        (x,y,w,h) = (int(c[3]),int(c[4]),int(c[5]),int(c[6]))
        img = cv2.imread('imgs/'+name)
        cv2.rectangle(img, (x,y),(x+w,y+h), (0,255,0))
        cv2.imwrite(folder + name ,img)

check('gioi_han_toc_do/')
