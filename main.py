#!usr/bin/python3.6

#File that launchs the program, there is only one main function


#Import of libraries
import pandas as pd
import numpy as np
from sklearn import tree
from sklearn.model_selection import train_test_split
import statistiques as st
import transformation as tr
import models as md



#Main function to do all the operations for the first dataset we study
def data_transformation():
	#The minimum number of matches
	minimum = 200

	#Loading phase of the interesting files
	matches_file = pd.read_csv('matchResults.csv')

	#Transform the pandas Dataframe into a Numpy array for the matches results
	array_result = matches_file.as_matrix(['Map', 'Team 1 ID' , 'Team 1 Score', 'Team 2 ID', 'Team 2 Score'])

	#Delete all the matches played on garbage maps
	array_without_garbage = tr.delete_garbage_maps(array_result)

	#Dictionnary that contains the ID of the team and the number of matches played
	total_match_each_team = st.nb_match_each_team(array_without_garbage)

	#How many team that played a decent number of matches
	list_result = st.decent_number_matches(total_match_each_team, minimum)
	dictionary = tr.numpy_to_dict(array_without_garbage, list_result)

	#Creation of the final array
	new_dic = tr.delete_garbage_dict(dictionary, list_result)
	new_dic = tr.result_encoding(new_dic)
	new_dic = tr.map_encoding(new_dic)
	X = md.X_creation(new_dic)
	y = md.y_creation(new_dic)

	#Final step
	md.best_number_neighbors(X,y)

	print("\nTest for all the matches with K-nearest-neighbors")
	dictionary = tr.result_encoding(dictionary)
	dictionary = tr.map_encoding(dictionary)
	X_1 = md.X_creation(dictionary)
	y_1 = md.y_creation(dictionary)

	#Final step for k-neighbors with more matches(all matches on the eight maps)
	md.best_number_neighbors(X_1,y_1)

	#Test with a decision tree
	md.test_decision_tree(X,y)

	#Test with a random forest
	md.test_random_forest(X,y)

	#Test with a support vector machine
	md.test_svm(X,y)
	


#Execution of the program
data_transformation()
