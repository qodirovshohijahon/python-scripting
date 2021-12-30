import tarfile
import shutil
import sys

shutil.make_archive('tar_folder_name', 'gztar', root_dir='./', base_dir='./')

print("Archived")
with tarfile.open('tar_folder_name.tar.gz', 'r') as tar:
    for name in tar.getnames():
        print(name)