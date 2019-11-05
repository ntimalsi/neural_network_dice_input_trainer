
#########IMPORT REQUIRED LIBRARIES########
from __future__ import division
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os 
from itertools import chain
import random 
##############################################
PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
######################################################################
#DEFINE POSITION FOR THE DICE#########################################
def generateposition(generator_number, dice_width = 5, dice_length = 5):
    all_combinations = []
    #array = set()
    #start = 0
    if generator_number == 1:
        for i in range(5):
            for j in range(5):
                row = []
                column = []
                row.extend([i])
                column.extend([j])
                all_combinations.append((row, column))
        
    if generator_number == 2:
        for i in range(3):
            for j in range(3):
                row = []
                column = []
                first_pixel = (i,j)
                second_pixel = (first_pixel[0]+2, first_pixel[1]+2)
                row.extend([first_pixel[0], second_pixel[0]])
                column.extend([first_pixel[1], second_pixel[1]])
                all_combinations.append((row, column))
                      
    if generator_number == 3:
        for i in range(3):
            for j in range(3):
                row = []
                column = []
                first_pixel = (i,j)
                second_pixel = (first_pixel[0]+1, first_pixel[1]+1)
                third_pixel = (first_pixel[0]+2, first_pixel[1]+2)
                row.extend([first_pixel[0], second_pixel[0], third_pixel[0]])
                column.extend([first_pixel[1], second_pixel[1], third_pixel[1]])
                all_combinations.append((row, column))
                      
    if generator_number == 4:
        for i in range(3):
            for j in range(3):
                row = []
                column = []
                first_pixel = (i,j)
                second_pixel = (first_pixel[0], first_pixel[1]+2)
                third_pixel = (first_pixel[0]+2, first_pixel[1])
                forth_pixel = (first_pixel[0]+2, first_pixel[1]+2)
                row.extend([first_pixel[0], second_pixel[0], third_pixel[0], forth_pixel[0]])
                column.extend([first_pixel[1], second_pixel[1], third_pixel[1], forth_pixel[1]])
                all_combinations.append((row, column))
                      
    if generator_number == 5:
        for i in range(3):
            for j in range(3):
                row = []
                column = []
                first_pixel = (i,j)
                second_pixel = (first_pixel[0], first_pixel[1]+2)
                third_pixel = (first_pixel[0]+1, first_pixel[1]+1)
                forth_pixel = (first_pixel[0]+2, first_pixel[1])
                fifth_pixel = (first_pixel[0]+2, first_pixel[1]+2)
                row.extend([first_pixel[0], second_pixel[0], third_pixel[0], forth_pixel[0], fifth_pixel[0]])
                column.extend([first_pixel[1], second_pixel[1], third_pixel[1], forth_pixel[1], fifth_pixel[1]])
                all_combinations.append((row, column))
                      
    if generator_number == 6:
        for i in range(3):
            for j in range(3):
                row = []
                column = []
                first_pixel = (i,j)
                second_pixel = (first_pixel[0], first_pixel[1]+2)
                third_pixel = (first_pixel[0]+1, first_pixel[1])
                forth_pixel = (first_pixel[0]+1, first_pixel[1]+2)
                fifth_pixel = (first_pixel[0]+2, first_pixel[1])
                sixth_pixel = (first_pixel[0]+2, first_pixel[1]+2)
                row.extend([first_pixel[0], second_pixel[0], third_pixel[0], forth_pixel[0], fifth_pixel[0], sixth_pixel[0]])
                column.extend([first_pixel[1], second_pixel[1], third_pixel[1], forth_pixel[1], fifth_pixel[1], sixth_pixel[1]])
                all_combinations.append((row, column))

    return all_combinations
#############################################################################################################
def dice_generator(dice_number):
    all_disc = []
    
    all_combinations = generateposition(dice_number)
    for row , column in all_combinations:
        a = np.ones(shape=(5,5), dtype=float)
        a[row, column] = 0
        all_disc.append(a)
    return all_disc

# An Inplace function to rotate  
# N x N matrix by 90 degrees in 
# anti-clockwise direction 
def image_rotation(mat, shape = 5):
    # rotate the dice by 90 degree 
    # Consider all squares one by one 
    for x in range(0, int(shape/2)): 
        # Consider elements in group    
        # of 4 in current square 
        for y in range(x, shape-x-1): 
            # store current cell in temp variable 
            temp = mat[x][y] 
            # move values from right to top 
            mat[x][y] = mat[y][shape-1-x] 
            # move values from bottom to right 
            mat[y][shape-1-x] = mat[shape-1-x][shape-1-y] 
            # move values from left to bottom 
            mat[shape-1-x][shape-1-y] = mat[shape-1-y][x] 
            # assign temp to left 
            mat[shape-1-y][x] = temp 
    return mat

def dice_append(dice_number, x, y):
    all_dice_face = dice_generator(dice_number)
    all_main_face = []
    for dice_face in all_dice_face:
        main_face = np.zeros(shape = (10,10), dtype=float)
        main_face[x:x+dice_face.shape[0], y:y+dice_face.shape[1]] = dice_face
        all_main_face.append(main_face)
        
        rotated_main_face = np.zeros(shape = (10,10))
        dice_face_90 = image_rotation(dice_face)
        rotated_main_face[x:x+dice_face_90.shape[0], y:y+dice_face_90.shape[1]] = dice_face_90
        all_main_face.append(rotated_main_face)        
    return all_main_face

# all_images = dice_append(1)
# print(len(all_images))
# print(all_images)

def _create_new_folder(local_dir):
    newpath = local_dir
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    return newpath

data_folder = '{}/images'.format(PROJECT_HOME)
_create_new_folder(data_folder) 

def _save_image(image, data_folder, image_count):
    img = Image.fromarray( image )
    image_path = "{}/{}.png".format(data_folder, image_count)
    plt.imshow(np.asarray(img), cmap='gray')
    plt.savefig(image_path)

outcomes=[]
target=[]
diction={1:0.1, 2:0.2, 3:0.3, 4:0.4, 5:0.5, 6:0.6}
xList = [0, 1, 2, 3, 4, 5]
yList = [0, 1, 2, 3, 4, 5]
for i in diction:
    data_folder = '{}/images/{}'.format(PROJECT_HOME, i)
    _create_new_folder(data_folder)
    image_count = 0
    for x in xList:
        for y in yList:
            
            all_main_face = dice_append(i, x, y)
            for image in all_main_face:
                image_count += 1
                
                # _save_image(image, data_folder, image_count)
                image.astype(float).tolist()
                outcomes.append([float(i) for i in list(chain(*image))])
                target.append([diction[i]])
            
combined = list(zip(outcomes, target))
random.shuffle(combined)

outcomes[:], target[:] = zip(*combined)   

# print(outcomes[0])
# print(target)
