from transform import four_point_transform
import numpy as np
import argparse, cv2

#做成可以在外部用命令调用的方式
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', help = 'path to the image file')
ap.add_argument('-c', '--coords', help = 'comma seperated list of source points')
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
pts = np.array(eval(args['coords']), dtype='float32')

warped = four_point_transform(image, pts)

cv2.imshow('original', image)
cv2.imshow('warped', warped)
cv2.waitKey(0)