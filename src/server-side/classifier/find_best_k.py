import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn import metrics 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
########## To find most accurate value of K for KNN (using library knn) ##############

def knn(k):
	dataframe = pd.read_csv("transformed_dataset.csv")
	x = dataframe.drop(["image_name", "class_name"], axis=1)			# Training KNN on all attributes except image_name and class_name
	y = dataframe.class_name											# Trying to find class_name

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

	classifier = KNeighborsClassifier(n_neighbors=k)
	classifier.fit(x_train, y_train)

	y_predrict = classifier.predict(x_test)

	accuracy = metrics.accuracy_score(y_test, y_predrict)
	print(str(k) + " accuracy: " + str(accuracy))
	return classifier, accuracy

def neuralNetwork():
	dataframe = pd.read_csv("transformed_dataset.csv")
	x = dataframe.drop(["image_name", "class_name"], axis=1)			# Training KNN on all attributes except image_name and class_name
	y = dataframe.class_name											# Trying to find class_name

	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.3, random_state = 1)

	classifier = MLPClassifier(random_state=1, max_iter=300)
	classifier.fit(x_train, y_train)

	y_predrict = classifier.predict(x_test)

	accuracy = metrics.accuracy_score(y_test, y_predrict)
	print( " accuracy: " + str(accuracy))


# Iterate through values of K and run algorithm each time, print results
def find_best_k():
	k = 1
	max_accuracy = 0
	best_k = 0
	while k < 100:
		classifier, accuracy = knn(k)
		if accuracy > max_accuracy:
			max_accuracy = accuracy
			best_k = k
		k +=1
	print(best_k)

if __name__ == "__main__":
	neuralNetwork()

