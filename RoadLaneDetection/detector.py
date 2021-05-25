import cv2
import matplotlib.pylab as plt
import numpy as np

def region_of_interest(image ,vertices):
    mask = np.zeros_like(image)
    # channel_count = image.shape[2]
    match_mask_color = 255
    cv2.fillPoly(mask,vertices,match_mask_color)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image

def draw_the_lines(image , lines):
    img  = np.copy(image)

    blanked_image = np.zeros((img.shape[0],img.shape[1],3),dtype=np.uint8)

    for line in lines:
        for x1,y1,x2,y2 in line:
            cv2.line(blanked_image,(x1,y1),(x2,y2),(0,255,0),3)
    img = cv2.addWeighted(img,0.8,blanked_image,1,0.0)
    return img

# image = cv2.imread("../road2.jpeg")
# image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
# image = cv2.medianBlur(image,5)
def process_video(image):
    height = image.shape[0]
    width = image.shape[1]
    Region_of_interest_vertices = [
        (0,height),
        (width/2,height/2),
         (width ,height)
    ]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 60, 250)
    cropped_image = region_of_interest(canny, np.array(
        [Region_of_interest_vertices], np.int32
    ))
    lines = cv2.HoughLinesP(cropped_image, 4, np.pi /60, 50, np.array([]), 40, 25)
    img_with_line = draw_the_lines(image, lines)
    return img_with_line

cap =cv2.VideoCapture("../road.mp4")
while(cap.isOpened()):

    ret ,frame = cap.read()
    frame = process_video(frame)
    cv2.imshow("frame",frame)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()