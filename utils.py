import cv2
import os 
import pandas as  pd 


def get_bboxes_df(df, rem_class):
    
    return df.loc[df['class'] != rem_class]

def get_bboxes_pascal():
    pass

def get_image(path_to_image, bbox):
    img = cv2.imread(path_to_image)
