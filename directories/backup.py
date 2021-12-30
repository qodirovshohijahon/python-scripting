from genericpath import exists
import os
import shutil
import time
from sh import rsync

def check_dir(os_dir):
    if not os.path.exists(os_dir):
        print(os_dir, "Does not exist")
        exit(1)
        
def ask_for_confirm():
    ans = input("Are you sure you want to continue? (y/n)")
    global con_exit
    if ans == 'y':
        con_exit = 0
        return con_exit
    elif ans == 'n':
        con_exit = 1
        return con_exit
    else:
        print("Answer with yes or no")
        ask_for_confirm()
        
def delete_files(ending):
    for r, d, f in os.walk(backup_dir):
        for files in f:
            if files.endswith("." + ending):
                os.remove(os.path.join(r, files))
                
backup_dir = input("Enter directory to backup\n")

check_dir(backup_dir)

print(backup_dir, "Saved!")

time.sleep(3)

backup_to_dir = input("Enter directory to save backup\n")
check_dir(backup_to_dir)
print("Doing the backup now....")
ask_for_confirm()
if con_exit == 1:
    print("Aborting the backup process!")
    exit(1)
rsync(
        "-auhv", 
        "--progress",
        "--delete", 
        "--exclude=lost+found", 
        "--exclude=/sys", 
        "--exclude=/tmp",
        "--exclude=/proc",
        "--exclude=/mnt",
        "--exclude=/media",
        "--exclude=/dev",
        "--exclude=/backup",
      backup_dir,
      backup_to_dir
)

"""
    - a : Archive
    -u : Update
    -h : Human-readable format
    -v : Verbose
    --delete : Deletes extraneous files from the receiving side
    --exclude : Exclude rules
    --progress : Shows progress
    --human-readable : Human-readable file sizes
    --no-implied-dirs : Do not imply directories
"""
# in simple bash script :
# rsync  -auhv --progress --delete --exclude=lost+found --exclude=backup /home/k8s-user/demo /home/k8s-user/backup 