import numpy as np
import cv2

def order_points(pts):
    #初始化一个序列化列表,使第一个入口为左上角,第二个右上角
    # 第三个右下角,最后一个左下角
    rect = np.zeros((4, 2), dtype='float32')

    #左上角会有一个最小的和,右下角最大
    s = pts.sum(axis=1)
    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    #右上角有最小的差值,左下角有最大的差值
    diff = np.diff(pts, axis=1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    return rect

def four_point_transform(image, pts):
    #序列化一个无序的点并解包
    rect = order_points(pts)
    tl, tr, br, bl = rect

    #计算出X轴最大值在 两个上边角和两个下边角之差中选最大值
    widthA = np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2))
    widthB = np.sqrt(((tr[0] - tl[0]) ** 2) + ((tr[1] - tl[1]) ** 2))
    maxWidth = max(int(widthA), int(widthB))

    #计算高
    heightA = np.sqrt(((tr[0] - br[0]) ** 2) + ((tr[1] - br[1]) ** 2))
    heightB = np.sqrt(((tl[0] - bl[0]) ** 2) + ((tl[1] - bl[1]) ** 2))
    maxHeight = max(int(heightA), int(heightB))

    #拿到了新图的宽与高之后,求鸟瞰图
    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0,maxHeight - 1]], dtype='float32')

    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    return warped