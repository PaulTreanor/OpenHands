import pandas as pd 
import csv
from sklearn.neighbors import LocalOutlierFactor
from scipy.spatial import distance
from knn import knn

############ LIBRARY LOF IMPLEMENTATION #############

def library_local_outlier_factor():
	dataframe = pd.read_csv("transformed_dataset.csv")
	training_data = dataframe.drop(["image_name", "class_name"], axis=1)
	lof = LocalOutlierFactor(novelty=True)
	lof.fit(training_data)
	return lof

############# SIMPLE KNN ANOMOLY DETECTION ALGORITHMS #####################

# Find confidence by looking at average distance to nearest neighbours 
def KNN_confidence(nearest_neighbours):
	distances = [item[0] for item in nearest_neighbours]
	avg_dist = sum(distances)/len(distances)
	return avg_dist

def KthNN_confidence(nearest_neighbours):
	distances = [item[0] for item in nearest_neighbours]
	return max(distances)

############# LDoF ALGORITHM #####################

# Local distance outlier factor has max accuracy (90% ood detection) when min_conf = -25
def local_distance_outlier_factor(nearest_neighbours):
	knn_avg = KNN_confidence(nearest_neighbours)
	knn_inner_distances = []
	for item in nearest_neighbours:
		neighbours = [line[0] for line in nearest_neighbours if line != item]
		distances = [distance.euclidean(item[0], line) for line in neighbours]
		knn_inner_distances += distances
	knn_inner_distance_avg = sum(knn_inner_distances)/len(knn_inner_distances)
	ldof = knn_avg/knn_inner_distance_avg
	return ldof

############# LoF ALGORITHM #####################
# Local outlier factor has max accuracy (90% ood detection) when min_conf = -1.3
# local_r_density = Local reachability density 

def rDistance(A, B, classifier, k):
	B_n_neighbours = classifier.get_knn(B[2])
	if len(A) ==3:
		A = A[2]
	k_dist = max([distance.euclidean(B[2], n[2]) for n in B_n_neighbours])
	AB_dist = distance.euclidean(A, B[2])
	r_distance = max(k_dist, AB_dist)
	return r_distance

def local_r_density(A, nearest_neighbours, classifier, k):
	r_distance_list = []
	for B in nearest_neighbours:
		B_r_distance = rDistance(A, B, classifier, k)
		r_distance_list.append(B_r_distance)
	avg_r_distance = sum(r_distance_list)/k
	local_r_density = 1.0/avg_r_distance 
	return local_r_density

# Find confidence based on local outlier factor (LOF) anomoly detection
def local_outlier_factor(A, nearest_neighbours, classifier, k):
	A_local_r_density = local_r_density(A, nearest_neighbours, classifier, k)
	local_r_density_list = []
	for B in nearest_neighbours:
		B_n_neighbours = classifier.get_knn(B[2])	
		B_local_r_density = local_r_density(B, B_n_neighbours, classifier, k)
		local_r_density_list.append(B_local_r_density)
	local_r_density_total = sum(local_r_density_list)
	divisor = A_local_r_density*k
	LOF_value = local_r_density_total/divisor
	LOF_value = -LOF_value
	return LOF_value


