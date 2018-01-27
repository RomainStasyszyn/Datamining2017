#!usr/bin/python3.6

#File that creates the model making prediction for matches


import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC



#Creation of X set
def X_creation(dictio):
	index = 0
	X = np.empty((len(dictio), 10))
	X_list = [[v[0], v[1], v[2], v[3], v[4], v[5], v[6], v[7], v[9], v[11]] for i,v in dictio.items()]
	for item in X_list:
		X[index] = item
		index += 1
	X = X.astype(int)
	return X


#Creation of y set
def y_creation(dictio):
	index = 0
	y = np.empty((len(dictio), 1))
	y_list = [v[10] for i,v in dictio.items()]
	for item in y_list:
		y[index] = item
		index += 1
	y = y.astype(int)
	return np.ravel(y)


#Search the best value for number of neighbors
def best_number_neighbors(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	skf = StratifiedKFold(n_splits=5)
	best_k = 0
	best_score = 0
	for k in range(1, 21, 1):
		score_sum = 0.0
		for train_index, test_index in skf.split(X_train, y_train):
			X_subtrain, X_subtest = X[train_index], X[test_index]
			y_subtrain, y_subtest = y[train_index], y[test_index]
			neighbors_k5 = KNeighborsClassifier(n_neighbors=k, weights='distance')
			neighbors_k5.fit(X_train, y_train)
			score = neighbors_k5.score(X_subtest, y_subtest)
		score_sum += score
		score_sum /= 5
		print("With K =", k, "the score is", score)
		if score_sum > best_score:
			best_score = score_sum
			best_k = k
	#Score
	print("Best :", best_k)
	prediction = neighbors_k5.predict(X_test)
	neighbors_k5 = KNeighborsClassifier(n_neighbors=k, weights='distance')
	neighbors_k5.fit(X_train, y_train)
	print("Score : {:2.1f}%".format(accuracy_score(y_test, prediction) * 100))


#Try the decision tree model for making prediction
def test_decision_tree(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	decision_tree = tree.DecisionTreeClassifier()
	decision_tree.fit(X_train, y_train)
	print("\nTest with a decision tree, the score is : {:2.1f}%".format(decision_tree.score(X_test, y_test) * 100))


#Try the random forest model for making prediction
def test_random_forest(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	random_forest = RandomForestClassifier(n_estimators=500, n_jobs=-1)
	random_forest.fit(X_train, y_train)
	print("\nTest with a random forest, the score is : {:2.1f}%".format(random_forest.score(X_test, y_test) * 100))


#Try the support vector machine model for making prediction
def test_svm(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)
	support_vector = SVC()
	support_vector.fit(X_train, y_train)
	print("\nTest with support vector machine, the score is : {:2.1f}%\n".format(support_vector.score(X_test, y_test) * 100))

