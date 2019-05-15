#! python

#a script that builds a dictionary of NFL teams, then adds teams.

#build a dictionary
nfl_teams = {'Atlanta':'Falcons', 'Baltimore':'Ravens', 'Chicago':'Bears'}
print(nfl_teams)

#add two teams
nfl_teams['Dallas']='Cowboys'
nfl_teams['Las Vegas']='Raiders'
print(nfl_teams)

#remove a team
del nfl_teams['Las Vegas']
print('Oops, we jumped the gun on that last one! Correcting...')
print(nfl_teams)

#use keys to print some team names
print('Low ratings alert! '+str(nfl_teams['Atlanta'])+' at ' + str(nfl_teams['Baltimore']) + '!')

#Challenge 1
#print out the team names only using .keys()
print('The team names only: ' + str(nfl_teams.keys()))

#Challenge 2
#add the Houston Oilers to the list of teams, print, update to Houston Texans, print
nfl_teams['Houston'] = 'Oilers'
print(nfl_teams)

