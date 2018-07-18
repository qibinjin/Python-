from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse, cv2, imutils
#导入必须的包


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required = True,
                help = 'path to the image to be scanned')
args = vars(ap.parse_args())
#外部命令接口

# image = cv2.imread('D:/Code/Python-/scanner/example_01.png')
image = cv2.imread(args['image'])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height=500)
#用opencv读入图片 除以500 的倍数记下来,并重新调整大小

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)
#把图片转换为灰度 方便查找边缘

print('STEP1: edge Detection...')
cv2.imshow('Image', image)
cv2.imshow('Edged', edged)
cv2.waitKey(0)
cv2.destroyAllWindows()
#显示原始图片与边缘查找之后的图


cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if imutils.is_cv2() else cnts[1]# CV2和CV3的表示存储位置不同
cnts = sorted(cnts, key = cv2.contourArea, reverse=True)[:5]
#查找纸的边缘线

for c in cnts:
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.02 * peri, True)


    if len(approx) == 4:
        screenCnt = approx
        break

print('STEP 2: Find contours of paper...')

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow('outline', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#画出带边缘线的图片

warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
#截图纸张内部内容

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = 'gaussian')
warped = (warped > T).astype('uint8') * 255
#将图片按照阈值转换为锐化的白底黑字图 更像扫描的结果

print('STEP 3: Applt perspective transform...')
cv2.imshow('Original', imutils.resize(orig, height=650))
cv2.imshow('Scanned', imutils.resize(warped, height=650))
cv2.waitKey(0)
#显示最终结果