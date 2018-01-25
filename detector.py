import cv2

sign_id = {
    'dung': '1',
    're_trai': '2',
    're_phai': '3',
    'cam_re_trai': '4',
    'cam_re_phai': '5',
    'mot_chieu': '6',
    'toc_do_toi_da': '7',
    'cac_loai_bien_khac': '8'

}


def predictor(sign_name, bgr_img, size_fluc, n_box):

    gray_img = cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)

    sign_classifier_xml = sign_name + '_cascade.xml'

    sign_cascade = cv2.CascadeClassifier(sign_classifier_xml)

    signs = sign_cascade.detectMultiScale(gray_img, size_fluc, n_box)
    cors = []
    for (x, y, w, h) in signs:
        cors.append((sign_id[sign_name], x, y, x + w, y + h))
        cv2.rectangle(bgr_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    if len(cors) != 0:
        return cors[0]
    else:
        return []
