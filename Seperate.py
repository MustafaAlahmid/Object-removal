import os
import shutil
import pandas as pd 
import numpy as np
import cv2 


def seperate_images(df, folder_path):
    df = pd.read_csv('train.csv')
    # Define paths where images are located and the new images will be saved
    parent_dir = folder_path
    path_out = 'seperate/'
    path_in = 'images/'


    # Get the list of Classes in the dataset 

    classes = df['name'].unique()

    # make a Dataframe of each class
    # Create a Dir Folder with the name of the class 

    for cls in classes:
        # Create DF of class
        cls_df = df.loc[df['name'] == cls].reset_index()
        # Create DIR and class folders
        directory = parent_dir + path_out + cls 
        path = os.path.join(parent_dir, directory)
        try:
            os.makedirs(path, exist_ok = True)
            print("Directory '%s' created successfully" % directory)
        except OSError as error:
            print("Directory '%s' can not be created" % directory)
        # Copy Images from Main Distination to the folder of Class
        
        for img in cls_df.index:
            filename = cls_df.iloc[img]['image_path']
            source  = parent_dir + path_in + filename
            dest = parent_dir + path_out+'/'+cls+'/'+ filename
            try: 
                
                shutil.copy(source, dest)
    #             print(filename," copied successfully.")
            except:
                print('err with ', source)
                

        print(len(os.listdir(parent_dir + path_out+'/'+cls)),' File has been copied to ',cls )
    path_folders = parent_dir + '/seperate/'
    return path_folders , classes