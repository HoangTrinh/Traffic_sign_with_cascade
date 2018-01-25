import matplotlib.pyplot as plt
import cv2

sign_id = {
    'dung': 1,
    're_trai': 2,
    're_phai': 3,
    'cam_re_trai': 4,
    'cam_re_phai': 5,
    'mot_chieu': 6,
    'toc_do_toi_da': 7,
    'cac_loai_bien_khac': 8

}

def predictor(sign_name, frame):
    # CHANGE
    bgr_img = cv2.imread(frame)
    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

    # CHANGE
    sign_classifier_xml = sign_name + '_cascade.xml'

    sign_cascade = cv2.CascadeClassifier(sign_classifier_xml)


    signs = sign_cascade.detectMultiScale(gray_img, 1.25, 3)
    list = []
    for (x,y,w,h) in signs:
        list.append([x,y,x+w, y+h, sign_id[sign_name]])
        cv2.rectangle(bgr_img,(x,y),(x+w,y+h),(255,0,0),2)

    plt.axis('off')
    plt.title('Detection result')
    plt.imshow(cv2.cvtColor(bgr_img, cv2.COLOR_BGR2RGB))
    plt.show()
    return list

print(predictor('cam_re_trai', '00202_1.jpg'))