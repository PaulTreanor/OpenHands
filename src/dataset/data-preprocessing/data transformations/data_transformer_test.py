import pytest 
from data_transformer import translate
from data_transformer import enlarge
from data_transformer import rotate
from pytest import ExitCode
# To run all tests remove "-v -m" and the specific marker
# python -m pytest .\data_transformer_tests.py -v -m translations

############################### TRANSLATION UNIT TESTS ###################################


# Creating instance of gesture coordinates from dataset to feed into trans
@pytest.fixture
def test_object():
	test_object = ['palm_108_keypoints', 550.552, 2280.4, 621.377, 2209.57, 678.713, 2125.25, 722.557, 2013.96, 800.128, 1943.13, 638.241, 1990.35, 634.868, 1852.07, 614.632, 1761.01, 587.651, 1673.32, 564.042, 1986.98, 550.552, 1828.46, 543.806, 1720.54, 523.57, 1632.85, 499.962, 1986.98, 496.589, 1835.21, 489.844, 1747.52, 476.353, 1666.57, 439.254, 2003.84, 419.018, 1889.17, 419.018, 1828.46, 419.018, 1757.63]	
	return test_object


@pytest.mark.translations
def test_translation_point_0(test_object):
	translated_coords = translate(test_object)
	x = translated_coords[1::2] 
	y = translated_coords[2::2]
	# Checkig xy cooridates of point 0 have been translated correctly
	assert [x[0], y[0]] == [0,0]

	
@pytest.mark.translations
def test_translation_point_12(test_object):
	translated_coords = translate(test_object)
	x = translated_coords[1::2] 
	y = translated_coords[2::2]
	# Checkig xy cooridates of point 12 have been translated correctly
	assert [x[12], y[12]] == [-26.982, -647.55]

	
@pytest.mark.translations
def test_translation_point_15(test_object):
	translated_coords = translate(test_object)
	x = translated_coords[1::2] 
	y = translated_coords[2::2]
	# Checkig xy cooridates of point 15 have been translated correctly
	assert [x[15], y[15]] == [-60.708, -532.88] 


############################### ENLARGEMENT UNIT TESTS ###################################

# Creating instance of set of a keypoints that have been translated already to feed into enlargement tests
@pytest.fixture
def test_object_2():
	test_object = ['palm_108_keypoints', 0.0, 0.0, 70.825, -70.83, 128.161, -155.15, 172.005, -266.44, 249.576, -337.27, 87.689, -290.05, 84.316, -428.33, 64.08, -519.39, 37.099, -607.08, 13.49, -293.42, 0.0, -451.94, -6.746, -559.86, -26.982, -647.55, -50.59, -293.42, -53.963, -445.19, -60.708, -532.88, -74.199, -613.83, -111.298, -276.56, -131.534, -391.23, -131.534, -451.94, -131.534, -522.77]
	return test_object

@pytest.mark.enlargements
def test_enlargement_point_0(test_object_2):
	englarged_coords = enlarge(test_object_2)
	x = englarged_coords[1::2] 
	y = englarged_coords[2::2]
	# Checkig xy cooridates of point 0 have been enlarged correctly
	assert [x[0], y[0]] == [0,0] 

@pytest.mark.enlargements
def test_enlargement_point_12(test_object_2):
	englarged_coords = enlarge(test_object_2)
	x = englarged_coords[1::2] 
	y = englarged_coords[2::2]
	# Checkig xy cooridates of point 12 have been enlarged correctly
	assert [x[12], y[12]] == [-0.919,-22.046]


@pytest.mark.enlargements
def test_enlargement_point_15(test_object_2):
	englarged_coords = enlarge(test_object_2)
	x = englarged_coords[1::2] 
	y = englarged_coords[2::2]
	# Checkig xy cooridates of point 15 have been enlarged correctly
	assert [x[15], y[15]] == [-2.067, -18.142]		

############################### ROTATION UNIT TESTS ###################################

# Creating instance of translated and enlarged list of gesture keypoint coordinates to feed into rotation tests
@pytest.fixture
def test_object_3():
	test_object = ['palm_108_keypoints', 0.0, 0.0, 2.411228507145167, -2.411398731536776, 4.363225650606873, -5.282062871635336, 5.855889295750152, -9.070917380074244, 8.496784552054532, -11.48231611161102, 2.985361335164879, -9.87471695725317, 2.8705279605852723, -14.582442731598862, 2.1815958028642757, -17.682569351586704, 1.2630309408623868, -20.667964731629908, 0.45926540856178333, -9.989448197197811, 0.0, -15.386242308777788, -0.22966674915921353, -19.060365577272055, -0.9185989068802104, -22.045760957315256, -1.7223303943024924, -9.989448197197811, -1.837163768882099, -15.156439380105287, -2.0667964731629906, -18.141834760148488, -2.526095926603096, -20.89776766030241, -3.789126867465483, -9.415451548691387, -4.47805902518648, -13.319377745858155, -4.47805902518648, -15.386242308777788, -4.47805902518648, -17.797641040314563]
	return test_object

@pytest.mark.rotations
def test_rotation_point_0(test_object_3):
	rotated_coords = rotate(test_object_3)
	x = rotated_coords[1::2] 
	y = rotated_coords[2::2]
	# Checkig xy cooridates of point 0 have been rotated correctly
	assert [x[0], y[0]] == [0,0] 

@pytest.mark.rotations
def test_rotation_point_12(test_object_3):
	rotated_coords = rotate(test_object_3)
	x = rotated_coords[1::2] 
	y = rotated_coords[2::2]
	# Checkig xy cooridates of point 12 have been rotated correctly
	assert [x[12], y[12]] == [1.93, 21.98]


@pytest.mark.rotations
def test_rotation_point_15(test_object_3):
	rotated_coords = rotate(test_object_3)
	x = rotated_coords[1::2] 
	y = rotated_coords[2::2]
	# Checkig xy cooridates of point 15 have been rotated correctly
	assert [x[15], y[15]] ==[2.898, 18.028]