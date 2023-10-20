# This program is used to merge multiple pdf's

import os
import PyPDF2

file_path = 'C:\\Users\\charc\\Desktop\\Python\\Mini Projects 2\\PDF merger'

pdf_files_list = [
            os.path.join(file_path, 'file 1.pdf'),
            os.path.join(file_path, 'file 2.pdf'),
            os.path.join(file_path, 'file 3.pdf')
                ]

merger = PyPDF2.PdfMerger()

for file in pdf_files_list:
    pdf_file = open(file, 'rb')
    pdf_read = PyPDF2.PdfReader(pdf_file)
    merger.append(pdf_read)
    pdf_file.close()

# Specifying the location of output(merged) file
output_path = os.path.join(file_path, 'merged.pdf')
merger.write(output_path)
merger.close()