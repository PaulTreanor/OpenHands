from os import listdir
from pathlib import Path
from os import rename

# Changes all filenames in each gesture folder to class label
# Subfolders inside images folder should be named "palm", "peace", and "thumbs_up"
# Run this program in same folder as images folder 

sub_dirs = [file for file in listdir('images')]

for sub_dir in sub_dirs:
	dir_path = 'images/' + sub_dir

	counter = 1
	for path in Path(dir_path).iterdir():
		if path.is_file():
			file_ext = path.suffix
			new_name = sub_dir + "_" + str(counter) + file_ext

			path.rename(Path(dir_path, new_name))
			counter += 1