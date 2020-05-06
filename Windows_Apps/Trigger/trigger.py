from os import system
import sys
import json

# ------------------------------------------------------ #
#----------------- Necessary_Functions() ----------------#
# ------------------------------------------------------ #

def drive_letters():
    drives_list = 'C:\\ProgramData\\Trigger\\drives.txt'
    system('wmic logicaldisk list brief > '+drives_list)
    
    with open(drives_list, encoding="UTF-16 LE") as file:
        data = file.readlines()
    system('del '+drives_list)
    drives = []
    
    for line in data[1:-1]:
        drives.append(line[:-1].split()[0][0])
    
    return drives

def create_fileTreeModel(drive_list):
    fileTreeModel = 'C:\\ProgramData\\Trigger\\FileTreeModel'
    system('mkdir '+fileTreeModel)
    
    for drive in drive_list[1:]:
        system('dir /a /b /s '+drive+':\\ > '+fileTreeModel+'\\'+drive+'_Drive_FileTreeModel.txt')

def generate_list_from_fileTreeData(line_data):
    line_data = line_data[:-1]
    reversed_line = line_data[::-1]
    name_of_key = ""
    
    for c in reversed_line:
        if c == '\\':
            break
        name_of_key += c
    name_of_key = name_of_key[::-1]

    return [name_of_key, line_data]

def create_file_tree_json(drive_list):
    file_tree = {}
    
    for drive in drive_list[1:]:
        with open('C:\\ProgramData\\Trigger\\FileTreeModel\\'+drive+'_Drive_FileTreeModel.txt') as file:
            data = file.readlines()
        
        for line in data:
            list_data = generate_list_from_fileTreeData(line)
            key, value = list_data[0], list_data[1]
            file_tree[key] = value
    
    with open("C:\\ProgramData\\Trigger\\File_Tree_Model.json", "w") as json_file:
        json.dump(file_tree, json_file, indent=4)
    
    system('rmdir /s /q C:\\ProgramData\\Trigger\\FileTreeModel')

def initialize():
    driveList = drive_letters()
    create_fileTreeModel(driveList)
    create_file_tree_json(driveList)

def error():
    print("""
     [Trigger] : [ERROR] --> Something Went Wrong... Please Try Again...
    
        [For Help] : (Type) --> trigger help
    
    """)

def help():
    print("""
      [Trigger] : [HELP] -->

            [Author] : MD. Shifat Hasan
            [Email]  : shifathasangns@gmail.com

        [Syntax] : 

            [For Help] --> trigger help

            [To Update the File-Tree-Model] --> trigger update

            [To Open FILE/FOLDER] --> trigger open FILE/FOLDER_NAME

        [NOTE] : [The File-Name must not contain any white-spaces...]
        [NOTE] : [While typing the File_Name, it must have the file extension...]

    """)

# ------------------------------------------------------ #
#------------------------ Main() ------------------------#
# ------------------------------------------------------ #

system('dir /a /b C:\\ProgramData\\ > trigger_temp.txt')
with open('trigger_temp.txt') as file:
    file_list = file.readlines()
    if "Trigger\n" not in file_list:
        system('mkdir C:\\ProgramData\\Trigger')
system('del trigger_temp.txt')

temp = 'C:\\ProgramData\\Trigger\\trigger_temp.txt'
system('dir /a /b C:\\ProgramData\\Trigger\\ > '+temp)

with open(temp) as file:
    file_list = file.readlines()
system('del '+temp)

if len(sys.argv[1:]) == 0:
    if "File_Tree_Model.json\n" not in file_list:
        print(' [Trigger] : [Creating File-Tree-Model...] --> Please Wait...')
        initialize()
        print("\n\n [Trigger] --> Initilization Successfully Completed...\n\n")
    help()

elif len(sys.argv[1:]) >= 1:
    if sys.argv[1] == "help":
        help()
    
    elif sys.argv[1] == "update":
        print(' [Trigger] : [Updating File-Tree-Model...] --> Please wait & don\'t quit the program...')
        initialize()
        print("\n\n [Trigger] --> Update Successfully Completed...\n\n")
        help()

    elif sys.argv[1] == "open":
        if len(sys.argv[2:]) > 0:
            if "File_Tree_Model.json\n" in file_list:
                file_name = " ".join(sys.argv[2:])
                with open('C:\\ProgramData\\Trigger\\File_Tree_Model.json') as json_file:
                    json_data = json.load(json_file)
                try:
                    print("\n [Trigger] : (Opening) --> "+file_name+"\n")
                    system("start \"\" "+'"'+json_data[file_name]+'"')
                except:
                    print("\n [Trigger] : [ERROR] --> The file "+file_name+" doesn't exist...\n")
                    error()
            else : error()
        else : error()
    else : error()