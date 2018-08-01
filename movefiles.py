import os
import glob
import shutil
import datetime

#destination for the different files
dest1 = 'E:\\Bilder'
dest2 = 'E:\\Video'
dest3 = 'C:\\Users\\ukki\\Downloads\\pdf_files'
dest4 = 'C:\\Users\\ukki\\Downloads\\exe_files'

#list of
pics = ['jpg', 'jpeg', 'bmp', 'gif', 'png']
vids = ['webm', 'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'ogg', 'mp4', 'm4p', 'm4v', 'flv']
exe = ['exe']
pdf = ['pdf']

def find_files(args):
    filelist = []
    all_files = glob.glob('C:\\Users\\ukki\\Downloads\\*')
    for file in all_files:
        for match in args:
            if file.endswith(match):
                filelist.append(file)
    return filelist


def move_files(here, there):
    for file in here:
        dest = file.replace('C:\\Users\\ukki\\Downloads', there)
        dest = dest.replace('.', datetime.datetime.fromtimestamp(os.path.getmtime(file)).strftime(("_%Y-%m-%d_%H%M%S.")))
        if os.path.exists(dest):
            dest = dest.replace('.', 'X.')
        shutil.move(file, dest)
        print(dest.replace(there, ''))


pictures_list = find_files(pics)
move_files(pictures_list, dest1)

vid_list = find_files(vids)
move_files(vid_list, dest2)

pdf_files = find_files(pdf)
move_files(pdf_files, dest3)

exe_files = find_files(exe)
move_files(exe_files, dest4)
