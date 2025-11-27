import os
import shutil

for root, dirs, files in os.walk('.'):
    for d in dirs:
        if d == '__pycache__':
            path = os.path.join(root, d)
            print(f"Deleting: {path}")
            shutil.rmtree(path)
            print(f"Deleted: {path}")