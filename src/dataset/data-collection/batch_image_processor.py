from os import listdir
from os import mkdir
from os import rename

# OpenPose only accepts input as a directory of images, but crashes if there is more than one image in a directory
# Solution is to make a folder for each image and a batch file to run openpose commands on all folders

dataset_path = "C:\\Users\\trean\\Desktop\\College\\4YP\\training-set\\dataset\\images"
save_location = "C:\\Users\\trean\\Desktop\\College\\4YP\\training-set\\dataset\\filed-images"
output_path = "C:\\Users\\trean\\Desktop\\College\\4YP\\training-set\\dataset\\openpose-output"

all_images = [file for file in listdir(dataset_path)]

with open('OpenPoseImageProcessor.bat', 'a') as bat:
	for image in all_images: 
		print(image)  

		# Make directory for image	
		new_image_path = save_location + "\\" + image
		mkdir(new_image_path[:-4])									# Spliced to remove file extension from file name

		# Move file into new directory
		current_path = dataset_path + "\\" + image 
		new_path = new_image_path[:-4] + "\\" + image
		rename(current_path, new_path)

		# Create command in batch file for image
		bat.write('bin\\OpenPoseDemo.exe --image_dir ' + new_image_path[:-4] + ' --hand --net_resolution "-1x320" --write_json ' + output_path + '\n')

	bat.write("PAUSE")