import os
import sys
from datetime import datetime

mode = None
folder = os.getcwd()   
file_name = None

 
for arg in sys.argv[1:]:
    arg_lower = arg.lower()
    if arg_lower == 'd':
        mode = 'd'
    elif os.path.exists(arg):   
        if os.path.isdir(arg):
            folder = arg
        elif os.path.isfile(arg):
            file_name = arg

# List items in the folder
items = os.listdir(folder)

# Filter files
if file_name:
    files = [file_name] if os.path.isfile(file_name) else []
else:
    files = [f for f in items if os.path.isfile(os.path.join(folder, f))]

# Output
if not files:
    print("No files found.")
else:
    print("Total Files Found:", len(files))

    if mode != 'd':
        print("\nList of Files:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
    else:
        print("\nDetailed File List (Name | Size | Modified Date):\n")
        for i, file in enumerate(files, start=1):
            file_path = os.path.join(folder, file)
            size = os.path.getsize(file_path)
            modified_time = os.path.getmtime(file_path)
            modified_date = datetime.fromtimestamp(modified_time).strftime("%Y-%m-%d %H:%M:%S")
            print(f"{i}. {file} | {size} bytes | {modified_date}")
