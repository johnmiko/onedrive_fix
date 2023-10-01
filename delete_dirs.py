# find_and_delete_git_directories(root_directory)
dirs = []
with open("git_dirs.txt", "r") as file:
    for line in file:
        dirs.append(line.strip().replace("\n", ""))
import shutil

i = 1
total = len(dirs)
for folder in dirs:
    i += 1
    pct = (i * 100 / total)
    # print(f"{i} /{total}: {pct}%")
    folder = folder.replace("\\\\", "\\").replace("\\", "/")
    try:
        shutil.rmtree(folder)
        print(f"Deleted {folder}")
    except Exception as e:
        pass
        # print(f"Failed to delete {folder}: {str(e)}")
