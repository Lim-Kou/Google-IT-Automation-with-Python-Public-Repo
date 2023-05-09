#!/usr/bin/python3

import subprocess
import multiprocessing
import os

"""List the source and destination of the directory to be synchronised. Exclude the backup folder to be synchronised, 
as it is in src directory."""
# For local machine
src = os.getcwd()
dest = os.path.join(os.getcwd(), "backup")
folder_to_exclude = "backup"


# For google qwiklabs.com
# src = os.path.expanduser('~') + r"/data/prod"
# dest = os.path.expanduser('~') + r"/data/prod_backup"
# folder_to_exclude = None

def run(source):
    """Use rsync to synchronise the file/directory in the specified source path to the destination path"""
    # Generate destination path
    destination_path = dest + source[len(src):]
    # Create destination path if not present
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    # synchronise source path to destination path
    subprocess.call(["rsync", "-arq", source, destination_path])
    print("Synchronised {} \n---> {}\n".format(source, destination_path))


def main():
    """Create a process pool and generate a list of source paths to be synchronized, excluding the files and
    directories in the folder_to_exclude. Use rsync to synchronize the files/directory in the generated list."""
    # With multiprocessing, create a process pool.
    pool = multiprocessing.Pool()
    # Create empty list to append the generated file/directory paths.
    file_paths = []
    # Generate the file/directory paths, excluding those that are in the folder_to_exclude (if any) and append them
    # to the list.
    for root, dirs, files in os.walk(src, topdown=True):
        for file in files:
            source_path = os.path.join(root, file)
            if folder_to_exclude is not None and folder_to_exclude not in source_path:
                file_paths.append(source_path)
        for dir in dirs:
            source_path = os.path.join(root, dir)
            if folder_to_exclude is not None and folder_to_exclude not in source_path:
                file_paths.append(source_path)
    # Use pool.map() to process the file paths in parallel.
    pool.map(run, file_paths)
    # close the process pool.
    pool.close()
    # wait for all issued tasks to complete.
    pool.join()


if __name__ == '__main__':
    main()
