import os
path = os.path.join("..", "3_file_writer", "file_for_delete")
print(path)

try:
    os.remove(path)

except:
    print("File already deleted")