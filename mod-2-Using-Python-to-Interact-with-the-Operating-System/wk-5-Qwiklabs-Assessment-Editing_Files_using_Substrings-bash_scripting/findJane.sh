#!/bin/bash

# Create oldFiles.txt
> oldFiles.txt

# Find all entries that contains jane
files=$(grep " jane " data/list.txt | cut -d ' ' -f 3)

for file in ${files}
do
  if test -e $file; then echo $file >> oldFiles.txt; else true; fi
done

