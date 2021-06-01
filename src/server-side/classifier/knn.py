import pandas as pd 
import csv
from scipy.spatial import distance

class knn:
	def __init__(self, k=5):
		self.k = k     # Number of nearest neighbours from gesture returned 
		try:
			self.dataframe = pd.read_csv("transformed_dataset.csv")
		except FileNotFoundError:
			self.dataframe = pd.read_csv("src/server-side/classifier/transformed_dataset.csv")

	

	def get_knn(self, gesture_data):
		# nearest_neighbours is list of k nearest neighbours tuples in the form (distance, class_name, feature_coordinates)
		nearest_neighbuors = []
		
		for line in self.dataframe.itertuples():
			file_name = line[0]
			class_name = line[-1]
			features = line[2:-1]
			features = [float(item) for item in features]
			gesture_data = [float(item) for item in gesture_data]
				
			dist = distance.euclidean(features, gesture_data)
			if len(nearest_neighbuors) < self.k:
				nearest_neighbuors.append((dist, class_name, features))
			else:
				distance_list = [item[0] for item in nearest_neighbuors]
				min_index = distance_list.index(max(distance_list))
				if nearest_neighbuors[min_index][0] > dist:	
					nearest_neighbuors[min_index] = (dist, class_name, features)
		return nearest_neighbuors


	def predict(self, gesture_data):	
		# List of k nearest neighbours in the form (distance, classification)
		nearest_neighbuors = self.get_knn(gesture_data[0])
		# Get most common class name
		class_list = [item[1] for item in nearest_neighbuors]
		classification = max(set(class_list), key=class_list.count)
		return classification, nearest_neighbuors



if __name__ == '__main__':
	# Dummy hand keypoint data for testing class
	gesture_data = ['0', '0', '-3.083', '1.839', '-5.395', '4.457', '-5.771', '8.398', '-4.251', '11.293', '-2.659', '10.371', '-2.116', '14.151', '-1.413', '17.201', '-0.734', '19.839', '-0.001', '10.0', '0.502', '14.814', '1.013', '18.082', '1.409', '21.15', '2.13', '9.456', '2.537', '14.379', '2.804', '17.044', '2.963', '19.611', '4.133', '8.508', '4.785', '12.385', '4.816', '14.548', '4.442', '16.839']
	classifier = knn()
	classification, nearest_neighbuors = (classifier.predict(gesture_data))
	print(classification)
	