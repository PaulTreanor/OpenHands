import pytest 
from get_class import getClass
from pytest import ExitCode
import os

# To run all tests remove "-v -m" and the specific marker
# python -m pytest .\get_class_tests.py -v -m marker

# Tests run a variety of images through OpenPose and the classifier testing multiple components together
# The images are not in the machine learning dataset 


############## IN DISTRIBUTION UNIT TESTS ######################

@pytest.mark.inDistribution
def test_peace_classification():
	image_path = os.path.realpath('../server_test/test-images/peace')		# relative path to test images. 
	classification = getClass(image_path)
	assert classification == 'peace'

@pytest.mark.inDistribution
def test_palm_classification():
	image_path = os.path.realpath('../server_test/test-images/palm')	
	classification = getClass(image_path)
	assert classification == 'palm'

@pytest.mark.inDistribution
def test_thumbs_up_classification():
	image_path = os.path.realpath('../server_test/test-images/thumbs-up')	
	classification = getClass(image_path)
	assert classification == 'thumbs_up'

@pytest.mark.inDistribution
def test_alt_peace_classification():
	image_path = os.path.realpath('../server_test/test-images/alt-peace')	
	classification = getClass(image_path)
	assert classification == 'peace'

@pytest.mark.inDistribution
def test_alt_palm_classification():
	image_path = os.path.realpath('../server_test/test-images/alt-palm')	
	classification = getClass(image_path)
	assert classification == 'palm'

@pytest.mark.inDistribution
def test_alt_thumbs_up_classification():
	image_path = os.path.realpath('../server_test/test-images/alt-thumbs-up')	
	classification = getClass(image_path)
	assert classification == 'thumbs_up'
	

############## OUT OF DISTRIBUTION UNIT TESTS ######################

#@pytest.mark.outOfDistribution
@pytest.mark.outOfDistribution
def test_ood_classification():
	image_path = os.path.realpath('../server_test/test-images/ood')	
	classification = getClass(image_path)
	assert classification == 'OOD'

@pytest.mark.outOfDistribution
def test_fuzzy_classification():
	image_path = os.path.realpath('../server_test/test-images/fuzzy')	
	classification = getClass(image_path)
	assert classification == 'OOD'

@pytest.mark.outOfDistribution
def test_no_hand_classification():
	image_path = os.path.realpath('../server_test/test-images/no-hand')	
	classification = getClass(image_path)
	assert classification == 'OOD'

@pytest.mark.outOfDistribution
def test_alt_ood_classification():
	image_path = os.path.realpath('../server_test/test-images/alt-ood')	
	classification = getClass(image_path)
	assert classification == 'OOD'

