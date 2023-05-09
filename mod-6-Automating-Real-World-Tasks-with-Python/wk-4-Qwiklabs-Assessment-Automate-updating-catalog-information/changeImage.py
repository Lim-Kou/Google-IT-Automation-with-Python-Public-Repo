#!/usr/bin/env python3

from PIL import Image
import os
import imghdr
import sys


def is_image_file(path):
    """Returns a string describing the image type and None if the file is not an image."""
    return imghdr.what(path)


def output(path):
    """Generate the new filename that ends with jpg."""
    f, e = os.path.splitext(path)
    return f + ".jpeg"


def checker(path):
    """Function that displays the format and size of image files."""
    for filename in os.listdir(path):
        # Phrase path for item
        infile = os.path.join(path, filename)
        # If it is an image file
        if is_image_file(infile):
            # Open the image file
            with Image.open(infile) as img:
                # print format and size of the image
                print(img.format, img.size)
    sys.exit(0)


def main():
    """Function that converts an image file to JPG format and resizes it to 600 x 400 pixels"""
    # Directory path for images
    in_directory = "supplier-data/images"
    out_directory = "supplier-data/images"

    # For checking of items in the output directory and terminate the program thereafter:
    # checker(out_directory)

    # For items in the images in_directory
    for infile in os.listdir(in_directory):
        # Phrase path for item
        infile_loc = os.path.join(in_directory, infile)
        # If it is an image file
        if is_image_file(infile_loc):
            # Get the outfile name
            outfile = output(infile)
            # Open the image file if it is not in jpeg format
            if infile != outfile:
                with Image.open(infile_loc) as img:
                    # For printing image format and size:
                    # print(img.format, img.size)
                    # Convert to RGB mode
                    img = img.convert("RGB")
                    # Resize image to 128x128 pixel and rotate image 90° clockwise
                    out = img.resize((600, 400))
                    # Save outfile to designated directory
                    outfile_loc = os.path.join(out_directory, outfile)
                    out.save(outfile_loc)


if __name__ == '__main__':
    main()
