import cv2
from matplotlib import pyplot as plt

img = cv2.imread("data/butterfly.jpg")
cv2.imshow("frame", img)

print(len(img.ravel()))

plt.hist(img.ravel(),256,(0,256))
plt.show()
cv2.waitKey(0)



cv2.destroyAllWindows()