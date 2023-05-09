#!/usr/bin/env python3

import sys
import subprocess

"""Replace 'jane' with 'jdoe' for filenames specified in text file. Path of text file is specified in argv[1]"""

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

for line in lines:
    old_name = line.strip()
    new_name = old_name.replace("jane", "jdoe")
    subprocess.run(["mv", old_name, new_name])

print("Replaced \"jane\" with \"jdoe\" successfully for \"oldFiles.txt\"")

# Usage for main
# ./changeJane.py oldFiles.txt
