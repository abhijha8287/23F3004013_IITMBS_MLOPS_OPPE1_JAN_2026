import shutil
import os

os.makedirs("data/merged",exist_ok=True)

for folder in ["data/v0","data/v1"]:

    for f in os.listdir(folder):

        shutil.copy(
            os.path.join(folder,f),
            "data/merged"
        )

print("Merged created")
