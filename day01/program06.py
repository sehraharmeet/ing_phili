import os

current_folder = r"F:\CloudMaterial" #os.getcwd()

items = os.listdir(current_folder)

files = [f for f in items if os.path.isfile(os.path.join(current_folder, f))]
# files = []

# for f in items:
#     full_path = os.path.join(current_folder, f)
#     if os.path.isfile(full_path):
#         files.append(f)
        
print("Total Files Found:", len(files))

# print("\nList of Files:")
for i, file in enumerate(files, start=1):
    print(f"{i}. {file}")

for f in files:
    print(f)
