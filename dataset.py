import os
import shutil
import kagglehub

# Download latest version
path = kagglehub.dataset_download("mirichoi0218/insurance")

files = os.listdir(path)
print(files)

target_dir = "data"
os.makedirs(target_dir, exist_ok=True)

for file in files:
    shutil.copy(os.path.join(path, file), target_dir)