import pytest 
from knn import knn
import confidence_functions
from pytest import ExitCode
# python -m pytest .\conf_function_test.py 

##################### SET UP VALUES FOR TESTS TO USE  ###################

# Creates a list of an instance of nearest neighbours for tests - each neighbour has a distance, a classificiation, and a set of coordinates
@pytest.fixture
def get_neighbours_list():   
	nearest_neighbours = [(31.865089361242973, 'peace', [0.0, 0.0, -3.421, 1.223, -3.219, 2.516, -3.195, 6.53, -1.194, 4.097, 2.619, 10.617, 2.85, 3.758, -2.395, 6.856, -2.039, 3.576, -0.001, 9.999, 0.459, 6.283, -2.904, 4.708, -3.323, 5.117, 0.806, 11.665, -2.339, 6.224, -2.897, 6.047, -0.683, 4.08, 1.754, 11.749, -2.506, 5.955, -2.19, 5.983, -1.233, 5.24]), (24.671191924996247, 'peace', [-0.0, 0.0, -0.956, 1.148, -1.284, 1.708, 0.929, 0.219, 2.65, -1.68, 9.618, 0.793, 5.942, -2.131, 2.323, -2.787, 1.284, -2.541, 9.836, -1.803, 5.219, -3.429, 2.5, -3.333, 0.97, -2.663, 7.623, -3.647, 4.29, -4.48, 2.022, -3.593, 0.697, -3.169, 6.393, -3.839, 4.468, -5.027, 2.295, -3.921, 1.12, -3.511]), (32.16324240495663, 'peace', [-0.0, 0.0, -0.249, 0.902, -0.094, 1.042, 2.303, -1.305, 4.186, -3.551, 6.955, 5.565, 9.169, -1.736, 6.363, -2.997, 4.248, -3.776, 9.946, -1.035, 8.027, -3.75, 5.197, -4.047, 3.525, -3.442, 9.83, -0.436, 7.383, -4.754, 5.151, -4.934, 3.036, -4.306, 9.372, -2.116, 6.699, -5.089, 4.755, -5.433, 2.927, -4.967]), (29.628958098454966, 'peace', [-0.0, 0.0, -2.604, 1.505, -4.559, 3.318, -4.95, 3.68, -4.957, 3.869, 3.36, 3.429, 2.683, 3.875, 2.154, 2.911, 1.345, 1.843, 9.971, 0.755, 4.347, -0.214, 4.173, -0.597, 4.85, -1.044, 10.605, 1.438, 6.701, -2.577, 7.161, -2.276, 4.23, -2.105, 11.073, 1.55, 6.758, -4.084, 6.841, -3.798, 4.42, -4.644]), (28.661883591278503, 'peace', [-0.0, 0.0, -0.973, 2.072, -1.356, 2.657, 1.643, 0.421, 3.804, -2.431, 9.682, 0.176, 8.798, -1.577, 6.323, -2.452, 4.882, -1.905, 9.967, -0.811, 6.926, -3.615, 4.18, -3.178, 2.998, -2.236, 8.59, -2.707, 5.679, -4.296, 3.667, -3.808, 2.329, -2.696, 7.907, -3.492, 4.692, -4.581, 2.906, -4.509, 1.809, -3.488])]
	return nearest_neighbours

# Creates instance of hand gesture A, which is measured against all others in dataset for anomoly detection
@pytest.fixture
def get_A():					
	A = A = [-0.0, 0.0, -3.083, 1.839, -5.395, 4.457, -5.771, 8.398, -4.251, 11.293, -2.659, 10.371, -2.116, 14.151, -1.413, 17.201, -0.734, 19.839, -0.001, 10.0, 0.502, 14.814, 1.013, 18.082, 1.409, 21.15, 2.13, 9.456, 2.537, 14.379, 2.804, 17.044, 2.963, 19.611, 4.133, 8.508, 4.785, 12.385, 4.816, 14.548, 4.442, 16.839]
	return A 

##################### SIMPLE CONFIDENCE FUNCTION TESTS ######################


# Testing if kth nearest neighbours is correctly implemented
def test_KthNN_confidence(get_neighbours_list):
	confidence = confidence_functions.KthNN_confidence(get_neighbours_list)
	assert confidence == 32.16324240495663

# Testing if k nearest neighbours for anomoly detection is correctly implemented
def test_KNN_confidence(get_neighbours_list):
	confidence = confidence_functions.KNN_confidence(get_neighbours_list)
	assert confidence == 29.398073076185863

# Testing if local distance outlier factor is correctly implemented 
def test_conf_ldofs(get_neighbours_list):
	confidence = confidence_functions.local_distance_outlier_factor(get_neighbours_list)
	assert confidence == 8.082030372281343

#################### LOCAL OUTLIER FACTOR ALGORITHM FUNCTION TESTS ##################

def test_ReachableDistance(get_neighbours_list, get_A):
	# A is value of selected hand gesture
	A = get_A
 	# B is one of As nearest neighbour 
	B = get_neighbours_list[0]
	k = 5
	classifier = knn(k)
	r_distance = confidence_functions.rDistance(A, B, classifier, k)
	assert r_distance == 45.454979859196946

def test_local_r_density(get_neighbours_list, get_A):
	nearest_neighbours = get_neighbours_list
	A = get_A
	k = 5	# Number of nearest neighbours A is compared to
	classifier = knn(k)
	local_reachability_distance = confidence_functions.local_r_density(A, nearest_neighbours, classifier, k)
	assert round(local_reachability_distance, 5) == round(0.014146622167822212,5)

