# Necessary imports
import cv2
import dlib
import numpy as np
import os
import imutils
import sys

## set directories
os.chdir('C:\\Users\\dw\github_repository\\Facial-mask-overlay-with-OpenCV-Dlib\\')
imagename='faceExtracted.PNG'
path = './image/'+imagename

#Initialize color [color_type] = (Blue, Green, Red)
color_blue = (254,207,110)
color_cyan = (255,200,0)
color_black = (0, 0, 0)

choice1 = 2 # black color
choice2 = 1 # fmask_my


# Loading the image and resizing, converting it to grayscale
img= cv2.imread(path)
img = imutils.resize(img, width = 500)
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Initialize dlib's face detector
detector = dlib.get_frontal_face_detector()

faces = detector(gray, 1)

# 추출 얼굴 수
print(faces)
print("Number of faces detected: ", len(faces))

# 68 face landmarks를 사용한다.
p = "shape_predictor_68_face_landmarks.dat"
# Initialize dlib's shape predictor
predictor = dlib.shape_predictor(p)

# Get the shape using the predictor
# 얼굴 랜드마킹 한다. 중요 함수는 dlib.shape_predictor(p)
# 얼굴을 확인한 다음 랜드마킹할 곳을 확인
for face in faces:
    landmarks = predictor(gray, face)

    # for n in range(0,68):
    #     x = landmarks.part(n).x
    #     y = landmarks.part(n).y
    #     img_landmark = cv2.circle(img, (x, y), 4, (0, 0, 255), -1)

    points = []
    for i in range(1, 16):
        point = [landmarks.part(i).x, landmarks.part(i).y]
        points.append(point)
    # print(points)

    # Coordinates for the additional point for wide, medium coverage mask - in sequence
    mask_c = [((landmarks.part(29).x), (landmarks.part(29).y))] # 굳이 추가할 필요는 없다 
    mask_my= [((landmarks.part(15).x), (landmarks.part(15).y))]

    fmask_basic= points
    fmask_c = points + mask_c
    fmask_my= points + mask_my
    print(f"fmask")
    # 여기에 마스크를 빈 공간에 마스크를 넣고 돌려야한다.

    # Using Python OpenCV – cv2.polylines() method to draw mask outline for [mask_type]:
    # fmask_c = wide, medium coverage mask,
    # fmask_my = 내 마스크
    fmask_basic = np.array(fmask_basic, dtype=np.int32)
    fmask_c = np.array(fmask_c, dtype=np.int32)
    fmask_my = np.array(fmask_my, dtype=np.int32)
    mask_type = {0: fmask_basic, 1: fmask_c, 2: fmask_my}
    #mask_type[choice2]

    print(mask_type[choice2])
    # change parameter [mask_type] and color_type for various combination
    img2 = cv2.polylines(img, [mask_type[choice2]], True, choice1, thickness=2, lineType=cv2.LINE_8)

    # Using Python OpenCV – cv2.fillPoly() method to fill mask
    # change parameter [mask_type] and color_type for various combination
    img3 = cv2.fillPoly(img2, [mask_type[choice2]], choice1, lineType=cv2.LINE_AA)

# cv2.imshow("image with mask outline", img2)
cv2.imshow("image with mask", img3)

#Save the output file for testing
outputNameofImage = "output/imagetest.jpg"
print("Saving output image to", outputNameofImage)
cv2.imwrite(outputNameofImage, img3)

cv2.waitKey(0)
cv2.destroyAllWindows()