import time 
from knn import knn
import confidence_functions

# Measure the performance of algorithms for optimisations

def knn_profile(gesture_data, k):
	start = time.perf_counter()				# Start timer 
	classifier = knn(k)
	nearest_neighbours = classifier.predict(gesture_data)   # Find nearest neighbours 
	stop = time.perf_counter()				# Stop timer 
	execution_time = stop-start 
	return execution_time

def Local_distance_outlier_factor_profile(nn):
	start = time.perf_counter()											# Start timer 
	local_distance_outlier_factor = confidence_functions.local_distance_outlier_factor(nn)			# Run local distance outlier factor algorithm
	stop = time.perf_counter()											# Stop timer 
	execution_time = stop-start 
	return execution_time


def Local_outlier_factor_profile(A, nn, k):
	classifier = knn(k)																# Set up KNN instance before timer starts to reduce noise
	start = time.perf_counter()														# Start timer 
	local_outlier_factor = confidence_functions.local_outlier_factor(A, nn, classifier, k)		# Run local outlier factor algorithm
	stop = time.perf_counter()														# Start timer 
	execution_time = stop-start 
	return execution_time

def avg_performance(gesture_data, A, nn, k):
	knn_times = [knn_profile(gesture_data,k ) for x in range(5)]
	avg_knn_time = sum(knn_times)/len(knn_times)
	print("Average KNN execution time while k =", k, ": ", avg_knn_time)

	ldof_times = [Local_distance_outlier_factor_profile(nn) for x in range(5)]
	avg_ldof_time = sum(ldof_times)/len(ldof_times)
	print("Average LdoF execution time while K =", k, ": ", avg_ldof_time)

	lof_times = [Local_outlier_factor_profile(A, nn, k) for x in range(5)]
	avg_lof_time = sum(lof_times)/len(lof_times)
	print("Average LoF execution time while K =", k, ": ", avg_lof_time)


if __name__ == '__main__':
	# Dummy data 
	gesture_data = ['0', '0', '-3.083', '1.839', '-5.395', '4.457', '-5.771', '8.398', '-4.251', '11.293', '-2.659', '10.371', '-2.116', '14.151', '-1.413', '17.201', '-0.734', '19.839', '-0.001', '10.0', '0.502', '14.814', '1.013', '18.082', '1.409', '21.15', '2.13', '9.456', '2.537', '14.379', '2.804', '17.044', '2.963', '19.611', '4.133', '8.508', '4.785', '12.385', '4.816', '14.548', '4.442', '16.839']
	nn = [(31.865089361242973, 'peace', [0.0, 0.0, -3.421, 1.223, -3.219, 2.516, -3.195, 6.53, -1.194, 4.097, 2.619, 10.617, 2.85, 3.758, -2.395, 6.856, -2.039, 3.576, -0.001, 9.999, 0.459, 6.283, -2.904, 4.708, -3.323, 5.117, 0.806, 11.665, -2.339, 6.224, -2.897, 6.047, -0.683, 4.08, 1.754, 11.749, -2.506, 5.955, -2.19, 5.983, -1.233, 5.24]), (24.671191924996247, 'peace', [-0.0, 0.0, -0.956, 1.148, -1.284, 1.708, 0.929, 0.219, 2.65, -1.68, 9.618, 0.793, 5.942, -2.131, 2.323, -2.787, 1.284, -2.541, 9.836, -1.803, 5.219, -3.429, 2.5, -3.333, 0.97, -2.663, 7.623, -3.647, 4.29, -4.48, 2.022, -3.593, 0.697, -3.169, 6.393, -3.839, 4.468, -5.027, 2.295, -3.921, 1.12, -3.511]), (32.16324240495663, 'peace', [-0.0, 0.0, -0.249, 0.902, -0.094, 1.042, 2.303, -1.305, 4.186, -3.551, 6.955, 5.565, 9.169, -1.736, 6.363, -2.997, 4.248, -3.776, 9.946, -1.035, 8.027, -3.75, 5.197, -4.047, 3.525, -3.442, 9.83, -0.436, 7.383, -4.754, 5.151, -4.934, 3.036, -4.306, 9.372, -2.116, 6.699, -5.089, 4.755, -5.433, 2.927, -4.967]), (29.628958098454966, 'peace', [-0.0, 0.0, -2.604, 1.505, -4.559, 3.318, -4.95, 3.68, -4.957, 3.869, 3.36, 3.429, 2.683, 3.875, 2.154, 2.911, 1.345, 1.843, 9.971, 0.755, 4.347, -0.214, 4.173, -0.597, 4.85, -1.044, 10.605, 1.438, 6.701, -2.577, 7.161, -2.276, 4.23, -2.105, 11.073, 1.55, 6.758, -4.084, 6.841, -3.798, 4.42, -4.644]), (28.661883591278503, 'peace', [-0.0, 0.0, -0.973, 2.072, -1.356, 2.657, 1.643, 0.421, 3.804, -2.431, 9.682, 0.176, 8.798, -1.577, 6.323, -2.452, 4.882, -1.905, 9.967, -0.811, 6.926, -3.615, 4.18, -3.178, 2.998, -2.236, 8.59, -2.707, 5.679, -4.296, 3.667, -3.808, 2.329, -2.696, 7.907, -3.492, 4.692, -4.581, 2.906, -4.509, 1.809, -3.488])]
	A = [float(item) for item in gesture_data] 
	k = 5  # Number of nearest neighbours used in KNN

	avg_performance(gesture_data, A, nn, k)

