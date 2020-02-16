import cv2 as ocv
img = ocv.imread('./DATA/00-puppy.jpg')
while True:
    ocv.imshow('Puppy',img)
    # ESC key
    if ocv.waitKey(1) & 0xFF == 27:
        break
ocv.destroyAllWindows()