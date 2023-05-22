import re


def get_file_type(filename):
    # Split the filename and extension
    file_parts = filename.split('.')
    if len(file_parts) > 1:
        extension = file_parts[-1].lower()

        # Check the file extension and return the corresponding file type and software
        if extension == 'txt':
            return 'Text Document', 'Notepad'
        elif extension == 'docx':
            return 'Word Document', 'MS Word'
        elif extension == 'xlsx':
            return 'Excel Spreadsheet', 'MS Excel'
        elif extension == 'jpg' or extension == 'jpeg' or extension == 'png':
            return 'Image File', 'Image Viewer'
        elif extension == 'pdf':
            return 'PDF Document', 'Adobe Acrobat Reader'

    # If the file extension is not recognized or there is no extension, return None
    return None, Nonejjjjm

# Main program
filename = input("Enter a file name: ")
file_type, software = get_file_type(filename)

if file_type and software:
    print(filename, "is a", file_type, "and can be opened using", software)
else:
    print("Invalid file or unsupported file type.")
