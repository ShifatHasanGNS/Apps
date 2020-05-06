from os import system
import sys
import json

#-------------------------------------------------------------------#

def drive_letters():
    system('wmic logicaldisk list brief > drives.txt')
    with open('drives.txt', encoding="UTF-16 LE") as file:
        data = file.readlines()
    system('del drives.txt')
    drives = []
    for line in data[1:-2]:
        drives.append(line[:-1].split()[0][0])
    return drives

def create_fileTree(drive_list):
    system('mkdir FileTreeModel')
    for drive in drive_list[1:]:
        system('dir /a /b /s '+drive+':\\ > FileTreeModel\\'+drive+'_Drive_FileTreeModel.txt')

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

def create_fileTree_json(drive_list):
    file_tree = {}
    for drive in drive_list[1:]:
        with open('FileTreeModel\\'+drive+'_Drive_FileTreeModel.txt') as file:
            data = file.readlines()
        for line in data:
            list_data = generate_list_from_fileTreeData(line)
            key, value = list_data[0], list_data[1]
            file_tree[key] = value
    system("whoami > name.txt")
    with open("name.txt") as file:
        name = file.readline()
    system('del name.txt')
    name = name[:-1]
    name = name.replace('\\', '__')
    name = name.replace(' ', '_')
    with open(name+'.json', "w") as json_file:
        json.dump(file_tree, json_file, indent=4)
    system('rmdir /s /q FileTreeModel')

#-------------------------------------------------------------------#

done = True
system('dir /a /b C:\\ProgramData\\ > list.txt')
with open('list.txt') as file:
    file_list = file.readlines()
    if "_DONE_\n" not in file_list:
        driveList = drive_letters()
        create_fileTree(driveList)
        create_fileTree_json(driveList)
        done = False
system('del list.txt')
if not done: system('xcopy /h _DONE_ C:\\ProgramData\\')