import tkinter as tk
import tkinter.font as tkFont
import csv, os, shutil
root = tk.Tk()


number_of_images_to_download = tk.StringVar(root, value='default text')
temp_var_radio =str()
#download
def GButton_143_command():
    update_dictionary()
    print("command")
    os.system("main.py")
#cut collages
def GButton_122_command():
    print("command")
    update_dictionary()
    os.system("collage.exe")

#del images in input
def GButton_690_command():
    update_dictionary()
    
    
    os.system("main.exe")
    folder = os.getcwd()+"/input"
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
            

    # copy files to input
    if dictionary_of_elements["searching_by_keywords_or_by_images"] == "keywords":
        temp_list_keywords = list(str(dictionary_of_elements.get("keywords")).replace('"','quotsign').split(";"))
        
    if dictionary_of_elements["searching_by_keywords_or_by_images"] == "images":
        temp_list_keywords = []
        length = os.listdir(os.getcwd()+"\\reverse_search")
        # print (length)
        for x in range(0,int(len(length))):
            temp_list_keywords.append("reversed_image_search "+ str(x))
        print(temp_list_keywords)

    dest=os.getcwd()+"\\input\\"
    for x in temp_list_keywords:
        #x = x.replace('"', 'quotsign')
        print (x)
        src = os.getcwd()+"\\photos\\"+str(x)

        src_files = os.listdir(src)
        for file_name in src_files:
            full_file_name = os.path.join(src, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, dest)
    # create colalges            
    os.system("collage.exe")
    # save
def GButton_826_command():
    print("command")
    update_dictionary()
    
    # my
def GButton_808_command():
    print("command")
    file = "dictionary.csv"
    load(file)
    # default
def GButton_710_command():
    print("command")
    file = "dictionary_default.csv"
    load(file)

def GRadio_18_command():
    print("command")
    global temp_var_radio
    temp_var_radio = "CORRECT"

def GRadio_721_command():
    print("command")
    global temp_var_radio
    temp_var_radio = "RESIZE WITH BORDERS"


def GRadio_236_command():
    print("command")
    global temp_var_radio
    temp_var_radio = "RESIZE BY HIGHEST"

def GRadio_704_command():
    print("command")
    global temp_var_radio
    temp_var_radio = "RESIZE BY LOWEST"

def GRadio_553_command():
    print("command")
    global temp_var_radio
    temp_var_radio = "CROP"


def GRadio_219_command():
    print("command")
    global temp_var_radio
    temp_var_radio = "DISTORT"


def GCheckBox_81_command():
    print("command")


def GCheckBox_525_command():
    print("command")


def GCheckBox_549_command():
    print("command")


def GCheckBox_413_command():
    print("command")
#kostyl
def GCheckBox_414_command():
    print("command")
           
def create_file():
    with open('dictionary.csv', 'w') as f:
        for key in dictionary_of_elements.keys():
            f.write("%s,%s\n" % (key, dictionary_of_elements[key]))
dictionary_of_elements = dict() 

def update_dictionary():
    dictionary_of_elements["number_of_images_to_download"]=str(GLineEdit_591.get())
    dictionary_of_elements["number_of_images_to_generate"]=str(GLineEdit_526.get())
    dictionary_of_elements["keywords"]=str(GLineEdit_735.get())
    #replace quotation
    dictionary_of_elements["keywords"]= dictionary_of_elements["keywords"].replace("'", "\'")
    dictionary_of_elements["keywords"]= dictionary_of_elements["keywords"].replace('"', 'quotsign')
    
    dictionary_of_elements["download_size_MinW"]=str(GLineEdit_767.get())
    dictionary_of_elements["download_size_MinH"]=str(GLineEdit_635.get())
    dictionary_of_elements["download_size_MaxW"]=str(GLineEdit_313.get())
    dictionary_of_elements["download_size_MaxH"]=str(GLineEdit_602.get())
    dictionary_of_elements["border_S"]=str(GLineEdit_377.get())
    dictionary_of_elements["cell_W"]=str(GLineEdit_132.get())
    dictionary_of_elements["cell_H"]=str(GLineEdit_29.get())
    dictionary_of_elements["elements"]=str(GLineEdit_34.get())
    dictionary_of_elements["columns_H"]=str(GLineEdit_916.get())
    dictionary_of_elements["columns_W"]=str(GLineEdit_816.get())
    
    # corners
    temp_var =str()
    print (c1.get())
    print (c2.get())
    print (c3.get())
    print (c4.get())
    if c1.get()== True:
        temp_var+="1"
    if c2.get()== True:
        temp_var+="2"
    if c3.get()== True:
        temp_var+="3"
    if c4.get()== True:
        temp_var+="4"
    print (temp_var)
    
    
    dictionary_of_elements["corners"]=temp_var
    
    
    # more checkbuton
    temp_var_for_input_type = str()
    if input_images_as_source.get()== True:
        dictionary_of_elements["searching_by_keywords_or_by_images"] = "images"
    else:
        dictionary_of_elements["searching_by_keywords_or_by_images"] = "keywords"
    # radio
    
    dictionary_of_elements["resize_method"]=temp_var_radio
    print (dictionary_of_elements)
    create_file()


    
    

def load(file):
    with open(str(file),encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        dictionary_of_elements = dict(reader)
    print (dictionary_of_elements)
    global temp_var_radio
    GLineEdit_591.delete(0, 1000)
    GLineEdit_735.delete(0, 1000)
    GLineEdit_767.delete(0, 1000)
    GLineEdit_635.delete(0, 1000)
    GLineEdit_313.delete(0, 1000)
    GLineEdit_602.delete(0, 1000)
    GLineEdit_377.delete(0, 1000)
    GLineEdit_132.delete(0, 1000)
    GLineEdit_29.delete(0, 1000)
    GLineEdit_34.delete(0, 1000)
    GLineEdit_916.delete(0, 1000)
    GLineEdit_816.delete(0, 1000)
    GLineEdit_526.delete(0, 1000)
    
    temp_list = list(dictionary_of_elements.get("corners"))
    
    if '4' in temp_list:
        GCheckBox_413.select()
    else:
        GCheckBox_413.deselect()
    if '3' in temp_list:
        GCheckBox_549.select()
    else:
        GCheckBox_549.deselect()
    if '2' in temp_list:
        GCheckBox_525.select()
    else:
        GCheckBox_525.deselect()
    if '1' in temp_list:
        GCheckBox_81.select()
    else:
        GCheckBox_81.deselect()
    
    if dictionary_of_elements.get("searching_by_keywords_or_by_images")== "images":
        GCheckBox_414.select()
    else:
        GCheckBox_414.deselect()
        
    for x in dictionary_of_elements:
        x = x
    
    GLineEdit_591.insert(0, dictionary_of_elements.get("number_of_images_to_download"))
    GLineEdit_735.insert(0, dictionary_of_elements.get("keywords").replace('quotsign', '"'))
    GLineEdit_767.insert(0, dictionary_of_elements.get("download_size_MinW"))
    GLineEdit_635.insert(0, dictionary_of_elements.get("download_size_MinH"))
    GLineEdit_313.insert(0, dictionary_of_elements.get("download_size_MaxW"))
    GLineEdit_602.insert(0, dictionary_of_elements.get("download_size_MaxH"))
    GLineEdit_377.insert(0, dictionary_of_elements.get("border_S"))
    GLineEdit_132.insert(0, dictionary_of_elements.get("cell_W"))
    GLineEdit_29.insert(0, dictionary_of_elements.get("cell_H"))
    GLineEdit_34.insert(0, dictionary_of_elements.get("elements"))
    GLineEdit_916.insert(0, dictionary_of_elements.get("columns_H"))
    GLineEdit_816.insert(0, dictionary_of_elements.get("columns_W"))
    GLineEdit_526.insert(0, dictionary_of_elements.get("number_of_images_to_generate"))
    
    if dictionary_of_elements.get("resize_method")== "CORRECT": 
        GRadio_18.select()
        temp_var_radio = "CORRECT"
    elif dictionary_of_elements.get("resize_method")== "RESIZE WITH BORDERS": 
        GRadio_721.select()
        temp_var_radio = "RESIZE WITH BORDERS"
    elif dictionary_of_elements.get("resize_method")== "RESIZE BY LOWEST": 
        GRadio_704.select()
        temp_var_radio = "RESIZE BY LOWEST"
    elif dictionary_of_elements.get("resize_method")== "RESIZE BY HIGHEST": 
        GRadio_236.select()
        temp_var_radio = "RESIZE BY HIGHEST"
    elif dictionary_of_elements.get("resize_method")== "CROP": 
        GRadio_553.select() 
        temp_var_radio = "CROP"
    elif dictionary_of_elements.get("resize_method")== "DISTORT": 
        GRadio_219.select()
        temp_var_radio = "DISTORT"
    print ("loaded")
    
        
 



#setting title
root.title("Collage cutter 1999")
#setting window size
width=600
height=500
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

GButton_143=tk.Button(root)
GButton_143["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_143["font"] = ft
GButton_143["fg"] = "#000000"
GButton_143["justify"] = "center"
GButton_143["text"] = "Downloading"
GButton_143.place(x=480,y=370,width=111,height=49)
GButton_143["command"] = GButton_143_command

GButton_122=tk.Button(root)
GButton_122["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_122["font"] = ft
GButton_122["fg"] = "#000000"
GButton_122["justify"] = "center"
GButton_122["text"] = "Creating collages"
GButton_122.place(x=370,y=420,width=107,height=40)
GButton_122["command"] = GButton_122_command

GButton_690=tk.Button(root)
GButton_690["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_690["font"] = ft
GButton_690["fg"] = "#000000"
GButton_690["justify"] = "center"
GButton_690["text"] = "Do both"
GButton_690.place(x=480,y=420,width=111,height=41)
GButton_690["command"] = GButton_690_command

GButton_826=tk.Button(root)
GButton_826["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_826["font"] = ft
GButton_826["fg"] = "#000000"
GButton_826["justify"] = "center"
GButton_826["text"] = "Save data"
GButton_826.place(x=20,y=460,width=70,height=25)
GButton_826["command"] = GButton_826_command

GButton_808=tk.Button(root)
GButton_808["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_808["font"] = ft
GButton_808["fg"] = "#000000"
GButton_808["justify"] = "center"
GButton_808["text"] = "Load"
GButton_808.place(x=20,y=430,width=70,height=25)
GButton_808["command"] = GButton_808_command

GButton_710=tk.Button(root)
GButton_710["bg"] = "#efefef"
ft = tkFont.Font(family='Times',size=10)
GButton_710["font"] = ft
GButton_710["fg"] = "#000000"
GButton_710["justify"] = "center"
GButton_710["text"] = "Default"
GButton_710.place(x=20,y=400,width=70,height=25)
GButton_710["command"] = GButton_710_command


GLineEdit_526=tk.Entry(root)
GLineEdit_526["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_526["font"] = ft
GLineEdit_526["fg"] = "#333333"
GLineEdit_526["justify"] = "center"
GLineEdit_526["text"] = "number_of_images_to_generate"
GLineEdit_526.place(x=130,y=10,width=70,height=25)

GLabel_0=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_0["font"] = ft
GLabel_0["fg"] = "#333333"
GLabel_0["justify"] = "center"
GLabel_0["text"] = "Number of\nImages to generate"
GLabel_0.place(x=10,y=10,width=117,height=30)

GLineEdit_816=tk.Entry(root)
GLineEdit_816["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_816["font"] = ft
GLineEdit_816["fg"] = "#333333"
GLineEdit_816["justify"] = "center"
GLineEdit_816["text"] = "columns_W"
GLineEdit_816.place(x=140,y=50,width=50,height=25)

GLabel_561=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_561["font"] = ft
GLabel_561["fg"] = "#333333"
GLabel_561["justify"] = "center"
GLabel_561["text"] = "Columns W H\nin cells"
GLabel_561.place(x=30,y=45,width=100,height=30)


GLineEdit_916=tk.Entry(root)
GLineEdit_916["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_916["font"] = ft
GLineEdit_916["fg"] = "#333333"
GLineEdit_916["justify"] = "center"
GLineEdit_916["text"] = "columns_H"
GLineEdit_916.place(x=190,y=50,width=50,height=25)

GLineEdit_34=tk.Entry(root)
GLineEdit_34["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_34["font"] = ft
GLineEdit_34["fg"] = "#333333"
GLineEdit_34["justify"] = "center"
GLineEdit_34["text"] = "elements"
GLineEdit_34.place(x=10,y=120,width=213,height=37)

# radio

GLabel_197=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_197["font"] = ft
GLabel_197["fg"] = "#333333"
GLabel_197["justify"] = "center"
GLabel_197["text"] = "Resize\nmethod"
GLabel_197.place(x=10,y=160,width=70,height=25)

GRadio_18=tk.Radiobutton(root)
ft = tkFont.Font(family='Times',size=10)
GRadio_18["font"] = ft
GRadio_18["fg"] = "#333333"
GRadio_18["justify"] = "center"
GRadio_18["text"] = "CORRECT"
GRadio_18.place(x=80,y=160,width=85,height=25)
GRadio_18["value"] = "CORRECT"
GRadio_18["command"] = GRadio_18_command

GRadio_721=tk.Radiobutton(root)
ft = tkFont.Font(family='Times',size=10)
GRadio_721["font"] = ft
GRadio_721["fg"] = "#333333"
GRadio_721["justify"] = "center"
GRadio_721["text"] = "WITH\nBORDERS"
GRadio_721.place(x=160,y=160,width=85,height=30)
GRadio_721["value"] = "RESIZE WITH BORDERS"
GRadio_721["command"] = GRadio_721_command


GRadio_236=tk.Radiobutton(root)
ft = tkFont.Font(family='Times',size=10)
GRadio_236["font"] = ft
GRadio_236["fg"] = "#333333"
GRadio_236["justify"] = "center"
GRadio_236["text"] = "BY\nHIGHEST"
GRadio_236.place(x=240,y=160,width=85,height=25)
GRadio_236["value"] = "RESIZE BY HIGHEST"
GRadio_236["command"] = GRadio_236_command

GRadio_704=tk.Radiobutton(root)
ft = tkFont.Font(family='Times',size=10)
GRadio_704["font"] = ft
GRadio_704["fg"] = "#333333"
GRadio_704["justify"] = "center"
GRadio_704["text"] = "BY\nLOWEST"
GRadio_704.place(x=320,y=160,width=85,height=25)
GRadio_704["value"] = "RESIZE BY LOWEST"
GRadio_704["command"] = GRadio_704_command

GRadio_553=tk.Radiobutton(root)
ft = tkFont.Font(family='Times',size=10)
GRadio_553["font"] = ft
GRadio_553["fg"] = "#333333"
GRadio_553["justify"] = "center"
GRadio_553["text"] = "CROP"
GRadio_553.place(x=410,y=160,width=85,height=25)
GRadio_553["value"] = "CROP"
GRadio_553["command"] = GRadio_553_command

GRadio_219=tk.Radiobutton(root)
ft = tkFont.Font(family='Times',size=10)
GRadio_219["font"] = ft
GRadio_219["fg"] = "#333333"
GRadio_219["justify"] = "center"
GRadio_219["text"] = "DISTORT"
GRadio_219.place(x=480,y=160,width=85,height=25)
GRadio_219["value"] = "DISTORT"
GRadio_219["command"] = GRadio_219_command

GLabel_681=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_681["font"] = ft
GLabel_681["fg"] = "#333333"
GLabel_681["justify"] = "center"
GLabel_681["text"] = "Cell H W"
GLabel_681.place(x=10,y=200,width=100,height=25)

GLineEdit_29=tk.Entry(root)
GLineEdit_29["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_29["font"] = ft
GLineEdit_29["fg"] = "#333333"
GLineEdit_29["justify"] = "center"
GLineEdit_29["text"] = "cell_H"
GLineEdit_29.place(x=110,y=200,width=70,height=25)

GLineEdit_132=tk.Entry(root)
GLineEdit_132["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_132["font"] = ft
GLineEdit_132["fg"] = "#333333"
GLineEdit_132["justify"] = "center"
GLineEdit_132["text"] = "cell_W"
GLineEdit_132.place(x=180,y=200,width=70,height=25)

GLabel_293=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_293["font"] = ft
GLabel_293["fg"] = "#333333"
GLabel_293["justify"] = "center"
GLabel_293["text"] = "Borders"
GLabel_293.place(x=250,y=200,width=70,height=25)

GLineEdit_377=tk.Entry(root)
GLineEdit_377["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_377["font"] = ft
GLineEdit_377["fg"] = "#333333"
GLineEdit_377["justify"] = "center"
GLineEdit_377["text"] = "border_S"
GLineEdit_377.place(x=310,y=200,width=70,height=25)

GLabel_71=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_71["font"] = ft
GLabel_71["fg"] = "#333333"
GLabel_71["justify"] = "center"
GLabel_71["text"] = "Corners to gravitate images"
GLabel_71.place(x=20,y=240,width=173,height=30)

# 4 checkboxes + input checkbox

c1=tk.BooleanVar()
c2=tk.BooleanVar()
c3=tk.BooleanVar()
c4=tk.BooleanVar()

input_images_as_source=tk.BooleanVar()


GCheckBox_81=tk.Checkbutton(root,variable=c1,)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_81["font"] = ft
GCheckBox_81["fg"] = "#333333"
GCheckBox_81["justify"] = "center"
GCheckBox_81["text"] = "Top left"
GCheckBox_81.place(x=20,y=270,width=70,height=25)
GCheckBox_81["offvalue"] = "0"
GCheckBox_81["onvalue"] = "1"
GCheckBox_81["command"] = GCheckBox_81_command

GCheckBox_525=tk.Checkbutton(root,variable=c2,)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_525["font"] = ft
GCheckBox_525["fg"] = "#333333"
GCheckBox_525["justify"] = "center"
GCheckBox_525["text"] = "Bottom left"
GCheckBox_525.place(x=20,y=300,width=94,height=30)
GCheckBox_525["offvalue"] = "0"
GCheckBox_525["onvalue"] = "1"
GCheckBox_525["command"] = GCheckBox_525_command

GCheckBox_549=tk.Checkbutton(root,variable=c3,)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_549["font"] = ft
GCheckBox_549["fg"] = "#333333"
GCheckBox_549["justify"] = "center"
GCheckBox_549["text"] = "Top right"
GCheckBox_549.place(x=110,y=270,width=70,height=25)
GCheckBox_549["offvalue"] = "0"
GCheckBox_549["onvalue"] = "1"
GCheckBox_549["command"] = GCheckBox_549_command

GCheckBox_413=tk.Checkbutton(root,variable=c4,)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_413["font"] = ft
GCheckBox_413["fg"] = "#333333"
GCheckBox_413["justify"] = "center"
GCheckBox_413["text"] = "Bottom right"
GCheckBox_413.place(x=110,y=300,width=87,height=30)
GCheckBox_413["offvalue"] = "0"
GCheckBox_413["onvalue"] = "1"
GCheckBox_413["command"] = GCheckBox_413_command

GCheckBox_414=tk.Checkbutton(root,variable=input_images_as_source,)
ft = tkFont.Font(family='Times',size=10)
GCheckBox_414["font"] = ft
GCheckBox_414["fg"] = "#333333"
GCheckBox_414["justify"] = "center"
GCheckBox_414["text"] = "Use images in folder \n'reverse_search' as input instead"
GCheckBox_414.place(x=380,y=190,width=217,height=40)
GCheckBox_414["offvalue"] = "0"
GCheckBox_414["onvalue"] = "1"
GCheckBox_414["command"] = GCheckBox_414_command

GLineEdit_602=tk.Entry(root)
GLineEdit_602["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_602["font"] = ft
GLineEdit_602["fg"] = "#333333"
GLineEdit_602["justify"] = "center"
GLineEdit_602["text"] = "Max_H"
GLineEdit_602.place(x=390,y=100,width=70,height=25)

GLineEdit_313=tk.Entry(root)
GLineEdit_313["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_313["font"] = ft
GLineEdit_313["fg"] = "#333333"
GLineEdit_313["justify"] = "center"
GLineEdit_313["text"] = "Max_W"
GLineEdit_313.place(x=460,y=100,width=70,height=25)

GLabel_800=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_800["font"] = ft
GLabel_800["fg"] = "#333333"
GLabel_800["justify"] = "center"
GLabel_800["text"] = "Max H W"
GLabel_800.place(x=320,y=100,width=70,height=25)

GLabel_198=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_198["font"] = ft
GLabel_198["fg"] = "#333333"
GLabel_198["justify"] = "center"
GLabel_198["text"] = "Min H W"
GLabel_198.place(x=320,y=70,width=70,height=25)

GLineEdit_635=tk.Entry(root)
GLineEdit_635["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_635["font"] = ft
GLineEdit_635["fg"] = "#333333"
GLineEdit_635["justify"] = "center"
GLineEdit_635["text"] = "Min_H"
GLineEdit_635.place(x=390,y=70,width=70,height=25)

GLineEdit_767=tk.Entry(root)
GLineEdit_767["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_767["font"] = ft
GLineEdit_767["fg"] = "#333333"
GLineEdit_767["justify"] = "center"
GLineEdit_767["text"] = "Min_W"
GLineEdit_767.place(x=460,y=70,width=70,height=25)

GLineEdit_735=tk.Entry(root)
GLineEdit_735["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_735["font"] = ft
GLineEdit_735["fg"] = "#333333"
GLineEdit_735["justify"] = "center"
GLineEdit_735["text"] = "keywords"
GLineEdit_735.place(x=260,y=30,width=326,height=39)

GLabel_525=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_525["font"] = ft
GLabel_525["fg"] = "#333333"
GLabel_525["justify"] = "center"
GLabel_525["text"] = "Keywords to download, with ; as divider. Use - to exclude word,\n double quotation for exact citation search on page with image"
GLabel_525.place(x=230,y=0,width=400,height=30)

GLabel_688=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_688["font"] = ft
GLabel_688["fg"] = "#333333"
GLabel_688["justify"] = "center"
GLabel_688["text"] = "Number of images to download per input"
GLabel_688.place(x=220,y=130,width=297,height=30)


GLineEdit_591=tk.Entry(root)
GLineEdit_591["borderwidth"] = "1px"
ft = tkFont.Font(family='Times',size=10)
GLineEdit_591["font"] = ft
GLineEdit_591["fg"] = "#333333"
GLineEdit_591["justify"] = "center"
GLineEdit_591["text"] = "number_of_images_to_download"
GLineEdit_591.place(x=510,y=130,width=70,height=25)

GLabel_346=tk.Label(root)
ft = tkFont.Font(family='Times',size=10)
GLabel_346["font"] = ft
GLabel_346["fg"] = "#333333"
GLabel_346["justify"] = "center"
GLabel_346["text"] = "Elements to use in the collage:\n(non-distrubuted cells will be count as 1x1)"
GLabel_346.place(x=10,y=80,width=230,height=38)    

load("dictionary.csv")
if __name__ == "__main__":
    
    root.mainloop()
