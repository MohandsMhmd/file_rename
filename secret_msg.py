
import os

def rename_file():
    #1- get file name
    file_list = os.listdir(r"C:\Users\Mohammad\Python\Secret_msg\prank")
    #print (file_list)
    saved_path = os.getcwd()
    print ("Current Working Dir "+saved_path)
    os.chdir(r"C:\Users\Mohammad\Python\Secret_msg\prank")
    #2- rename files
    for file_name in file_list:
        table = str.maketrans(dict.fromkeys('0123456789'))
        os.rename(file_name, file_name.translate(table))
    os.chdir(saved_path)



rename_file()
