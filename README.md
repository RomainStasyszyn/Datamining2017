# Datamining2017
Projet pour le cours de fouille de données dont le but est d'effectuer des analyses statistiques
afin de prédire le résultat d'un match de Counter-Strike : Global Offensive opposant deux équipes données.

OBJECTIF :
	L'objectif de sera d'analyser les données récupérées sur le site Kaggle afin de dresser des statistiques ainsi que des pronostiques
	en rapport avec les matchs professionnels et semi-professionnels.
	Pour le moment je pense utiliser un ou plusieurs ensembles de données afin d'étendre les possibilités d'analyses.


MATERIEL :
	Pour ce qui est du "matériel" je compte crée un environnement virtuel propre à ce projet avec les packages numpy, scipy, pandas ce
	qui sera déjà une bonne base pour de l'analyse à partir de fichiers au format CSV. De plus je pense que l'utilisation d'un notebook
	de type jupyter permettra une bonne structuration de ce que l'on fait et nous permettra de mélanger harmonieusement code, texte
	descriptif et graphiques.

IDEES :
	---- 06/11/17 ---- 
	Pour le moment il faudrait mettre les données sur le Git (elles ne sont pas trop lourdes en l'occurrence).
	Puis voir ce qu'il y a comme informations dans les fichiers ainsi que vérifier s'il n'y a pas quelques
	différences entre plusieurs fichiers comme par exemple dans le fichier 1 le numéro du compte du joueur
	a pour clef account_key mais dans le deuxième fichier la même information a pour clef acc_k. Dans ce cas 
	il s'agira d'harmoniser les données afin de faciliter le traitement ultérieur.

COMMANDES UTILES :
	conda list : checker l'installation (listes des packages installés)
	conda upgrade --all : mise à jour d'anaconda
	conda install package-name (possibilité de renseigner plusieurs package à la suite) : installation d'un ou des packages
	conda install package-name=X.X (le numéro de la version) : installation d'une version précise d'un package
	conda remove package-name : suppression d'un package
	conda update package-name : mise à jour d'un package
	conda create -n env-name list-of-package : création d'un environnement virtuel avec une liste de package souhaités
	conda create -n env-name python=X.X : création d'un environnement virtuel basé sur une version précise de Python
	conda env export > environment.yaml : exportation de l'environnement courant (activé au moment de l'exportation) dans un fichier partageable
	conda env create -f environment.yaml : création d'un nouvel environnement virtuel à partir d'un fichier yaml
	conda env list : liste tous les environnements virtuels crées
	conda env remove -n env-name : supprimer l'environnement virtuel précisé
	source activate my-env : activation de l'environnement virtuel précisé
	source deactivate : désactiver l'environnement virtuel courant
	conda install jupyter notebook : installer jupyter notebook dans l'environnement courant
	conda install nb_conda : installer le notebook conda pour une meilleure utilisation de tous nos environnements virtuels
	control+C puis y : pour quitter jupyter
	jupyter nbconvert --tohtml notebook.ipynb : permet de convertir le notebook notebook.ipynb en une page HTML

SITES ET DOCUMENTS D'INSPIRATION :
	Udacity - Anaconda.
	Udacity - Jupyter notebooks.
	Udacity - Intro to Data Analysis.
	Udacity - Intro to Descriptive Statistics.
	Udacity - Intro to Inferential Statistics.

