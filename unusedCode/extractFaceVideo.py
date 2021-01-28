# import modules
import cv2
import os
import glob
# set classifier
face_classifier = cv2.CascadeClassifier("./library/classifier/haarcascade_frontalface_default.xml")
# set var
resource_dir = "./resource/for_train/video"
face_dir = "./data/face/image"
# mapping name/id with dir info
resource_dir_nameS_id = glob.glob(resource_dir + "/*") # list of own face folder
# get name and id
for resource_dir_name_id in resource_dir_nameS_id:
    resource_dir_name_id_Only = os.path.basename(resource_dir_name_id)
    resource_dir_name, resource_dir_nameId_format = resource_dir_name_id_Only.split("_")
    resource_dir_nameId, resource_dir_format = resource_dir_nameId_format.split(".")
    # set own face
    face_name = resource_dir_name # face name
    face_name_id = resource_dir_nameId # face id of name
    resource_pathVid = resource_dir_name_id
    vid = cv2.VideoCapture(resource_pathVid)
    face_cnt = 0
    while vid.isOpened():
        ret, frame = vid.read()
        if ret:
            img = frame.copy()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # image to grayscale
            face = face_classifier.detectMultiScale(gray, 1.25, 10) # recognize faces algorithm
        for (x, y, w, h) in face:
        # set ROI of faces
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, str(face_cnt), (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
            face_cnt += 1
            ROI_face = gray[y:y + h, x:x + w]
            ROI_face = cv2.resize(ROI_face, (250, 250))
            face_dir_name = str(face_dir + "/" + face_name + "_" + face_name_id)
        
            if not os.path.exists(face_dir_name):
                os.makedirs(face_dir_name)

            face_pathImg = os.path.join(face_dir_name, str(face_cnt) + ".jpg")
            cv2.imwrite(face_pathImg, ROI_face)
        cv2.imshow("Now saving faces", frame)
        
        if cv2.waitKey(1) > -1:
            break
    vid.release()
    cv2.destroyAllWindows()
