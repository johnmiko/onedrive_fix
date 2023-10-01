"""
need to delete all the version control files
"""
from datetime import datetime

folder = "D:/Users/johnm/OneDrive/"

# jpgFilenamesList = glob.glob(f"{folder}", recursive=True)
import os


def find_git_directories(root_dir):
    git_dirs = []
    deleting = ["git", "node_modules", "venv"]
    for foldername, subfolders, filenames in os.walk(root_dir):
        for dd in deleting:
            if dd in subfolders:
                git_dirs.append(os.path.join(foldername, dd))

    return git_dirs


# Replace 'root_directory' with the directory where you want to start your search
root_directory = folder
print(datetime.now())
git_directories = find_git_directories(root_directory)
with open("git_dirs2.txt", "w") as f:
    f.write("\n".join(git_directories))
