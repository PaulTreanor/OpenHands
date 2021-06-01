import json 
import pandas 
import csv
from os import listdir

fieldnames = []
json_path = 'openpose-output'

# Generate attribute names for keypoints 0-20
def generate_fieldnames():
	fieldnames = ["image_name"]
	i = 0
	while i <= 20:
		fieldnames.extend(["point_" + str(i) + "_x", "point_" + str(i) + "_y", "point_" + str(i) + "_conf"])
		i+=1 
	return fieldnames

def getJsonData(file, path):
	with open(path + "\\" + file, "r") as json_file:
		json_data = json.load(json_file)
		# Images used for dataset only contain one person each
		first_person = json_data['people'][0]
		gesture_data = first_person['hand_right_keypoints_2d']
		gesture_data.insert(0, file[:-5])
		return gesture_data	

def jsonToCsv(fieldnames, json_path):
	with open("gesture_dataset.csv", "a", newline='') as dataset:
		csv_writer = csv.writer(dataset)
		csv_writer.writerow(fieldnames)

		json_files = [f for f in listdir(json_path)]

		for file in json_files:
			gesture_data = getJsonData(file, json_path)
			csv_writer.writerow(gesture_data)

def cleanedDataset():
	with open("gesture_dataset.csv", "r", newline='') as dataset:
		csv_reader = csv.reader(dataset)

		# Create and open new csv file
		with open('cleaned_dataset.csv', 'w', newline='') as cleaned_dataset:
			csv_writer = csv.writer(cleaned_dataset)
			for line in csv_reader:
				clean_line = True
				# Line is not clean if any attributes have empty value ("0")
				for attribute in line:
					if attribute == "0":
						clean_line = False
				# Only write clean lines
				if clean_line == True:
					# Remove confidence measures from coordinates
					del line[3::3]
					csv_writer.writerow(line)


if __name__ == '__main__':
	fieldnames = generate_fieldnames()
	json_path = 'openpose-output'

	# Write json data into csv dataset
	jsonToCsv(fieldnames, json_path)

	# Clean dataset
	cleanedDataset()