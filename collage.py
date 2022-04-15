# import tkinter as tk
# import tkinter.font as tkFont
# from tkinter import *
# import pathlib
import os
import glob
# import csv
# import itertools
import random
# import json
# import math
# import numpy as np
import shutil
import csv
dictionary_of_elements_def = dict()
def open_file_and_load_settings():
    global dictionary_of_elements_def
    with open('dictionary.csv',encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        dictionary_of_elements_def = dict(reader)
    print (dictionary_of_elements_def)
open_file_and_load_settings()


try:    
    os.mkdir(os.getcwd()+"\\input")
except:
    print ("Exists")
def files_list(directory):

    cwd = os.getcwd()
    path, dirs, files = next( os.walk( cwd + directory ) )
    string = path.split('/', 1)[1]
    for x in range(len(files)):
        files[x] = string+"/"+files[x]
        
    return files
 
print (files_list('/input'))
number_of_files = len(files_list('/input'))
print (str(number_of_files) + ":Number of files")
#number of images do we need in the end
print ("Number of random collages you need, default is 50")
try:
    number_of_images = int(dictionary_of_elements_def.get("number_of_images_to_generate"))
except:
    number_of_images = ''
if number_of_images == '':
    number_of_images = 50
#get the number of columns and rows
print ("Enter the number of columns (width) for combined collages (can be any, 1,3,5 for example, default is 2):")
try:
    number_of_columns = int(dictionary_of_elements_def.get("columns_H"))
except:
    number_of_columns = ''
if number_of_columns == '':
    number_of_columns = 2
print ("Enter the number of rows (height) for combined collages (can be any, default is 2):")
try:
    number_of_rows = int(dictionary_of_elements_def.get("columns_W"))
except:
    number_of_rows = ''
if number_of_rows == '':
    number_of_rows = 2
total_number_of_cells = number_of_rows * number_of_columns
print (str(total_number_of_cells)+":Total number of cells")

#elements
def rewrite_X_format(element):
    height = int(element.split('x')[0])
    width = int(element.split('x')[1])
    print (str(height) + " " + str(width))
    parametershw = []
    parametershw.append(int(height))
    parametershw.append(int(width))
    return parametershw
    

def rewrite_X_format_factor(element):
    height = int(element.split('x')[0])
    width = int(element.split('x')[1])
    print (str(height) + " " + str(width))
    factor = height * width
    return factor

dictionary_of_elements = {}
string = dictionary_of_elements_def.get("elements")
# print (dictionary_of_elements_def)
# print (string)
elements = list(string.split(";"))
print (elements)

counter_for_elements = 0
def pick_elements():
    global total_number_of_cells
    global counter_for_elements
    print ( dictionary_of_elements )
    print (str(total_number_of_cells) + ":Cells left")
    print ("Enter parameters of the collage's element in format 'Height x Width' eg: 1x2, 2x1, 2x2, 3x1, 3x2 etc. If input is empty or 1x1 - all the rest of cells will be filled with smallest 1x1 images")
    try:
        element = str(elements[counter_for_elements])
    except:
        element = ""
    counter_for_elements +=1
    print (counter_for_elements)
    print (element)
    
    if element == "" or element == "1x1":
        dictionary_of_elements["1x1"]= int(total_number_of_cells)
        return
    else:
        print ("What number of " + element + " elements do you need? Default is 1.")
    try:
        number_of_elements = 1
    except:
        number_of_elements = 1
        
    number_to_extract = number_of_elements * rewrite_X_format_factor(element)
    if element in dictionary_of_elements:
        dictionary_of_elements [element] = dictionary_of_elements [element] + number_of_elements
    else :
        dictionary_of_elements [element] = number_of_elements
    total_number_of_cells -= number_to_extract
    if total_number_of_cells == 0:
        return
    elif total_number_of_cells <=0:
        print ("Not enough cells to operate with this number of such elements.(" + str(total_number_of_cells +number_to_extract ) + "<" + str(number_to_extract)+")")
        input()
        exit()
    else:
        pick_elements()
pick_elements()
print (dictionary_of_elements) 
final_dictionary_of_elements = {}
#check for empty values
for key, value in dictionary_of_elements.items():
        if value != 0:
            final_dictionary_of_elements[key] = dictionary_of_elements[key]
print  (final_dictionary_of_elements) 
#total number of elements in collages
total_number_of_elements = 0
for x in final_dictionary_of_elements:
    print (x)
    total_number_of_elements += final_dictionary_of_elements[x]
print (total_number_of_elements)
#check correct number
if total_number_of_elements > number_of_files:
    print ("Not enough images to operate with this nubmer of cells")
    input()
    exit()
else:
    print ("continue")
    
#matrix
# zeros_array_num = np.zeros( (number_of_rows, number_of_columns) )
# zeros_array=zeros_array_num.astype(str)
zeros_array=[]
for x in range(number_of_rows):
    zeros_array.append([])
    for y in range(number_of_columns):
        zeros_array[x].append("0.0")
print (zeros_array)

#method of resizing
print ("What method to apply to images when resizing? print one: CORRECT, RESIZE WITH BORDERS , RESIZE BY HIGHEST, RESIZE BY LOWEST , CROP , DISTORT. Default will be CORRECT")
try:
   method = dictionary_of_elements_def.get("resize_method")
except:
    method = ''
if method == '':
    method = "CORRECT"
    

#get the number of columns and rows
print ("Enter the width of the cell (smallest image, default 100) :")
try:
    cell_width = int(dictionary_of_elements_def.get("cell_W"))
except:
    cell_width = ''
if cell_width == '':
    cell_width = 100
print ("Enter the height of the cell (smallest image, default 100) :")
try:
    cell_height = int(dictionary_of_elements_def.get("cell_H"))
except:
    cell_height = ''
if cell_height == '':
    cell_height = 100
#pick border width (will be neede also for combining images wid different sizes)
print ("Enter the width of the border in px (defaul is 1):")
try:
    border_width = int(dictionary_of_elements_def.get("border_S"))
except:
    border_width = 1
#removing files and temp folder
try:    
    os.mkdir(os.getcwd()+"\\collages")
except:
    print ("Exists")

files = files_list('/collages')
print (os.getcwd())
for f in files:
    print (os.getcwd())
    print (f)
    os.remove(os.getcwd()+"/"+f)
try:    
    shutil.rmtree(os.getcwd()+"/temp")
except:
    print ("No temp to remove")
try:    
    os.mkdir(os.getcwd()+"\\temp")
except:
    print ("Exists")


#assigning some pixel measurments
widht_of_complex_collage = 0
height_of_complex_collage = 0    
def resize(method,cell_width,cell_height,element):

    global size
    global cell_size
    global widht_of_complex_collage
    global height_of_complex_collage
    if element == None:
        size = str(cell_width)+"x"+str(cell_height)
        cell_size = size
        try:    
            os.mkdir(os.getcwd()+"\\temp\\"+size)
        except:
            print ("Exists")
    # if element == none means that the is only simple method an no elements to resize but defaul one same for each image
    else:
        current_cell_height = rewrite_X_format(element)[0]*cell_height + border_width*((rewrite_X_format(element)[0]-1)*2)
        current_cell_width = rewrite_X_format(element)[1]*cell_width + border_width*((rewrite_X_format(element)[1]-1)*2)
        print (current_cell_height,current_cell_width)
        size = str(current_cell_width)+"x"+str(current_cell_height)
        cell_size = str(rewrite_X_format(element)[0])+"x"+str(rewrite_X_format(element)[1])
        
        #calculating size for hard method
        widht_of_complex_collage = number_of_columns * (cell_height + 2*border_width)
        height_of_complex_collage = number_of_rows * (cell_width + 2*border_width)
        #printing
        
        try:    
            os.mkdir(os.getcwd()+"\\temp\\"+cell_size)
        except:
            print ("Exists")
    
    if method == "RESIZE WITH BORDERS":    
        command = "magick input/*.* -resize " + size +" temp/"+cell_size+"/converted_%04d.png"
    elif method == "RESIZE BY LOWEST":
        command = "magick input/*.* -resize " + size +"^< temp/"+cell_size+"/converted_%04d.png"
    elif method == "RESIZE BY HIGHEST":
        command = "magick input/*.* -resize " + size +"^> temp/"+cell_size+"/converted_%04d.png"
    elif method == "CROP":
        command = 'magick input/*.* -gravity center -extent "' + size +'^^" temp/'+cell_size+'/converted_%04d.png'
    # elif method == "RESIZE AND CROP":
        # print ("Resoluton to crop to from resized image: eg 75x100")
        # size2 = #тут нужно найти доп параметры из размера
        # command = 'magick input/*.*  -resize '  + size + '^< -gravity center -extent "' + size +'^^" +repage temp/'+cell_size+'/converted_%04d.png'
        # print (command)
    elif method == "DISTORT":
        command = "magick input/*.* -resize " + size +"! temp/"+cell_size+"/converted_%04d.png"
    elif method =="CORRECT":
        command = "magick input/*.* -resize "+size+"^^ -gravity center -extent " + size +"^^ -gravity center -resize " + size +" +repage temp/"+cell_size+"/converted_%04d.png"
    os.system( command )
    
#do we go for equal collage
if number_of_rows * number_of_columns == total_number_of_elements:
    print ("We a working with equal images")
    
    element = None
    resize(method,cell_width,cell_height,element)
    
    input_files = files_list('/temp/'+ size) 
    print ("Combinations")
    combinations = []
    for x in range(0,number_of_images):
        combinations.append(random.sample(input_files,total_number_of_elements))
    
    counter = 0

        
    for x in combinations:
        
        counter +=1
        to_shuffle = list(x)
        random.shuffle(to_shuffle)
        names = ' '.join([str(v) for v in to_shuffle])
        print (names)
        orientation = str(number_of_rows)+"x"+str(number_of_columns)
        command = "magick montage -tile "+ orientation+ " " +names+' -geometry "1x1+'+str(border_width)+"+"+str(border_width)+"<"+'" collages/collage_'+str(counter)+".png"
        print (command)
        os.system( command )
    os._exit(0)
        #ok, so with 1x1 temporary finished. maybe to add bg colors.
        
#do we go complex collage:
elif number_of_rows * number_of_columns > total_number_of_elements:
    print ("We are dealing with complex thing")
 
elements_to_resize= list(dictionary_of_elements.keys())
print (elements_to_resize)
for element in elements_to_resize:


    resize(method,cell_width,cell_height,element)
    
    
# simple method without rearranging images
counter = 0
def simple_method():

    input_files = files_list('/temp/'+ cell_size) 
    print ("Combinations")
    combinations = []
    for x in range(0,number_of_images):
        combinations.append(random.sample(input_files,total_number_of_elements))
    
    
    
    print ("Addons for names")
    to_decrease_for_names =  dictionary_of_elements.copy()
    print (to_decrease_for_names)
    list_of_addons_to_names = []
    
    def filling_name_addons():
        global counter
        print (to_decrease_for_names.values())
        if all(value == 0 for value in to_decrease_for_names.values()) == True:
            return
        else:
            if list(to_decrease_for_names)[counter] != 0:
                print (list(to_decrease_for_names)[counter])
                element = list(to_decrease_for_names)[counter]
                # element = rewrite_X_format(element)
                print ("Element up")
                print (element)
                
                if to_decrease_for_names[element] !=0:
                    list_of_addons_to_names.append(str(element))
                    to_decrease_for_names[element] -= 1
                    print (to_decrease_for_names[element])
                if to_decrease_for_names[element] == 0:
                    counter +=1
        filling_name_addons()
    filling_name_addons()
    print (list_of_addons_to_names)
    
    print ('What corner to graivitate images by size? Big images will be put to taht corner:')
    print ("1- top left, 2- left bottom, 3 - top right, 4- right bottom")
    print ('Default is 1234- random, but you can print combination 12 or 423 or even 11113 for randomization. Corner will be picked from combination of numbers each time')     
    try:
        code = str(dictionary_of_elements_def.get("corners"))
    except:
        code = "1234"
    if code == "":
        code= "1234"
    code_list = list(code)
    image_counter = 0
    for x in combinations:
        
        counter =0
        to_shuffle = list(x)
        random.shuffle(to_shuffle)
        
        #print (names)
        print ("Addons for names")
        final_list = []
        for y in to_shuffle:
            # print (y)
            name_itself =  y.split('/')
            # print (name_itself)
            y= "temp/"+list_of_addons_to_names[counter]+"/"+str(name_itself[2])
            # print (y)
            final_list.append(y)
            counter +=1
        names = ' '.join([str(v) for v in final_list])
            
        print (names)
        method_of_rotation = str(random.choice(code_list))
        print (code_list)
        print (method_of_rotation)
        
        # postfix =""
        if method_of_rotation == "1":
            print ("1st")
            postfix = " "
        elif method_of_rotation == "2":
            print ("2nd")
            postfix = " -flip "
        elif method_of_rotation == "3":
            print ("3rd")
            postfix = " -flop "
        elif method_of_rotation == "4":
            print ("4th")
            postfix = " -flip -flop "
            
            
        command = "magick " + names + postfix + " -define ashlar:best-fit=true ashlar:collages/out"+str(image_counter)+".png["+str(widht_of_complex_collage) +"x"+ str(height_of_complex_collage) + "+" +str(border_width) + "+" +str(border_width) +"]" 
        command2 = "magick collages/out"+str(image_counter)+".png -gravity North -crop "+str(widht_of_complex_collage) +"x"+ str(height_of_complex_collage) +"+0" + postfix + " collages/out"+str(image_counter)+".png"
        print (command)
        print (command2)
        
        image_counter += 1
        os.system( command )
        os.system( command2 )
    os._exit(0)
    #auto method finished, maybe add colors of borders
    
    
counter = 0  
image_counter = 1
def hard_method():

    
    
    def placing_objects():
        global counter
        global image_counter
        print (zeros_array)
        print (dictionary_of_elements)
        if all(value == 0 for value in dictionary_of_elements.values()) == True:
            return
        else:
            if list(dictionary_of_elements)[counter] != 0:
                element = list(dictionary_of_elements)[counter]
                print(element)
                hw_params = rewrite_X_format(element)
                print (hw_params)
                print("What row to put this "+ element +" element?")
                row_to_put = int(input())
                print("What column to put this "+ element +" element?")
                column_to_put = int(input())
                for x in range (row_to_put-1, row_to_put-1+ hw_params[0]):
                    for y in range (column_to_put-1,column_to_put-1 + hw_params[1]):
                        if zeros_array[x][y] == "0.0":
                            zeros_array[x][y] = str(element)+"n"+str(image_counter)
                            # print (zeros_array)
                        else:
                            print ("It doest fit the shape")
                            placing_objects()
                dictionary_of_elements[element] -= 1
                image_counter +=1
                if dictionary_of_elements[element] == 0:
                    counter +=1

        placing_objects()  
    placing_objects()
    print ("width and height")
    print (widht_of_complex_collage)
    print (height_of_complex_collage)
    print (zeros_array)
    # we create templates to pick later
    # def creating_aligned_images():
        
        # for row in zeros_array:
            # for column in row:

# print ("Arranging method - 1 for simple automatic (default), 2- for manual arranging(deprecated, not working, in progress)")
# try:
    # method = int(input())
# except:
    # method = 1
method = 1
if method == 1:
    simple_method()
elif method == 2:
    hard_method()