# This script contains a function that looks for PDF files and calculates
# their size in a certain directory and all its subdirectories. The function is
# executed in main and the result is printed.

import os

def find_pdf_size(top):
    size_pdf = 0 # size of all PDF files in the top directory and subdirectories
    for root, dirs, files in os.walk(top):
        for name in files:
            if name.lower().endswith(".pdf"):
                size_pdf += os.path.getsize(os.path.join(root, name))
    return size_pdf


result = find_pdf_size(".")

print("The size of all PDF files is {} bytes".format(result))