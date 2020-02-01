import cv2


# read a image in coloured
img=cv2.imread('IMG_20190516_133811.jpg',1)

# read a inage in gray scale or black n white

img_1=cv2.imread('IMG_20190516_133811.jpg',0)

print('type of image readed by opencv\n\n',type(img))

print(img.shape)

# cv2.imshow('my own image',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

resi_img=cv2.resize(img,(int(img.shape[0]/4),int(img.shape[1]/4)))
cv2.imshow('my image',resi_img)
cv2.waitKey(0)
cv2.destroyAllWindows()