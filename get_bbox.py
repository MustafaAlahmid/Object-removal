import xml.etree.ElementTree as ET

def get_bboxes_from_voc_xml(xml_file: str):
    # parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    bboxes = []
    # Iterate over all object elements
    for obj in root.iter('object'):
        # Extract the bounding box coordinates
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        label = obj.find('name').text
        bboxes.append([xmin, ymin, xmax, ymax, label])

    return bboxes