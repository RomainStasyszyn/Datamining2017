#!usr/bin/python3.6

#File making statistics and compute some numbers to know how teams, matches etc there are in the dataset.


#Function that computes the real number of matches played on garbage maps (the last four maps)
def garbage_matches():
    list_of_garbage = {'Default' : 0, 'Tuscan' : 0, 'Season' : 0, 'TBA' : 0}
    for item in array_result:
        if item[0] == 'Default':
            list_of_garbage['Default'] += 1
            #how_many_default += 1
        elif item[0] == 'Tuscan':
            #how_many_tuscan += 1
            list_of_garbage['Tuscan'] += 1
        elif item[0] == 'Season':
            #how_many_season += 1
            list_of_garbage['Season'] += 1
        elif item[0] == 'TBA':
            #how_many_tba += 1
            list_of_garbage['TBA'] += 1
    return list_of_garbage


#How many teams played on useful maps
def how_many_teams(array):
    list_of_teams = []
    for item in array:
        if item[1] not in list_of_teams:
            list_of_teams.append(item[1])
        if item[3] not in list_of_teams:
            list_of_teams.append(item[3])
    return list_of_teams


#Check how many matches for each team
def nb_match_each_team(array):
    list_of_teams = {}
    for item in array:
        if item[1] not in list_of_teams:
            list_of_teams[item[1]] = 1
        else:
            list_of_teams[item[1]] += 1
        if item[3] not in list_of_teams:
            list_of_teams[item[3]] = 1
        else:
            list_of_teams[item[3]] += 1
    return list_of_teams


#Returns the list of teams that 
def decent_number_matches(dictio, number):
    result_decent = []
    for i, v in dictio.items():
        if v > number:
            result_decent.append(i)
    return result_decent


#How many matches on useful maps
def total_matches(dictio):
    total_matches = 0
    for i,v in dictio.items():
        total_matches += v
    return total_matches


#How many matches on useful maps for each team with a decent minimum number of games played
def total_decent_matches(dictio, l):
    total_matches = 0
    for i,v in dictio.items():
        if i in l:
            total_matches += v
    return total_matches
