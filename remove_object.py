import cv2
import xml.etree.ElementTree as ET
import numpy as np
from pascal_voc_writer import Writer


def remove_object_from_image(image_path: str, bboxes: list, obj_name: str, output_path: str) -> tuple:
    """
    Removes an object from an image and its corresponding bounding box annotation from an XML file.
    :param image_path: str, the path to the input image.
    :param bboxes: list of lists, the bounding box coordinates in the format [xmin, ymin, xmax, ymax, class_name].
    :param obj_name: str, the class name of the object to be removed.
    :param output_path: str, the path to save the output image.
    :return: tuple of the output image and the updated XML tree.
    """
    # Load the input image
    img = cv2.imread(image_path)

    # Initialize a binary mask for the object to be removed
    mask = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)

    for bbox in bboxes:
        # Extract the coordinates and class name of the current bounding box
        xmin, ymin, xmax, ymax, class_name = bbox

        if class_name == obj_name:
            # Set the mask values to 1 inside the bounding box
            mask[ymin:ymax, xmin:xmax] = 255

            # Inpaint the masked region using a telea algorithm
            img = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

    # Save the output image
    cv2.imwrite(output_path, img)

    # Parse the input XML file
    xml_path = image_path[:-4] + '.xml'
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Remove the bounding box annotation for the object to be removed
    for member in root.findall('object'):
        class_name = member.find('name').text
        if class_name == obj_name:
            root.remove(member)

    # Write the updated XML tree to the output file
    output_xml_path = output_path[:-4] + '.xml'
    tree.write(output_xml_path)

    return img, tree
