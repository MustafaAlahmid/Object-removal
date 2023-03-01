import cv2

import numpy as np 

def remove_object_from_image(image, bboxes: list, obj_name):
    # Create an instance of the inpainting model
    img = cv2.imread(image)

    # Define the mask for the object you want to remove
    mask = np.zeros((img.shape[0],img.shape[1]),dtype=np.uint8) # initialize mask
    
    img_copy = img.copy()
    for bbox in bboxes:

        if bbox[4] == obj_name:
            mask[bbox[1]:bbox[3], bbox[0]:bbox[2]] = 255

            # Perform inpainting
            img_copy = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
        # cv2.imshow('dst', dst)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    return img_copy

    # Remove the bounding box for the removed object
    # bboxes.pop(object_index)
    # return bboxes,dst



