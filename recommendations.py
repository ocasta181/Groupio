# group.io
# MIT Big Data Hackathon
# group.io is a group recommendation system
# We are:
# 		Andrin Foster
# 		Benjamin Chen
# 		Catherine Liu
# 		Demetri Sampas 
# 		Jonathan Barronville
# 		Prakash Manghwani
#
# 
# Code is borrowed heaily from http://edc.tversu.ru/elib/inf/0251.pdf

from math import sqrt
import json

with open(
	os.path.join('.', 'data', 'yelp-filtered.50.json')) as json_dump:
		yelpDict = json_dump.read()

# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2, 'Snakes on a Plane': 3,
 'Just My Luck': 3, 'Superman Returns': 3, 'You, Me and Dupree': 2,
 'The Night Listener': 3, 'Neverland': 4},
'Gene Seymour': {'Lady in the Water': 3, 'Snakes on a Plane': 3,
 'Just My Luck': 1, 'Superman Returns': 5, 'The Night Listener': 3,
 'You, Me and Dupree': 3, 'Up': 5},
'Michael Phillips': {'Lady in the Water': 2, 'Snakes on a Plane': 3,
 'Superman Returns': 3, 'The Night Listener': 4, 'The Grand Budhapest Hotel': 4},
'Claudia Puig': {'Snakes on a Plane': 3, 'Just My Luck': 3, 'The Night Listener': 4, 
'Superman Returns': 4, 'You, Me and Dupree': 2, 'Dumb and Dumber': 2},
'Mick LaSalle': {'Lady in the Water': 3, 'Snakes on a Plane': 4,
 'Just My Luck': 2, 'Superman Returns': 3, 'The Night Listener': 3,
 'You, Me and Dupree': 2, 'Night At the Museum': 3},
'Jack Matthews': {'Lady in the Water': 3, 'Snakes on a Plane': 4,
 'The Night Listener': 3, 'Superman Returns': 5, 'You, Me and Dupree': 3, 'The Shawshank Redemption': 3},
'Toby': {'Snakes on a Plane':4,'You, Me and Dupree':1,'Superman Returns':4}}

group1 = {'Lisa Rose', 'Mick LaSalle', 'Toby'}


group2  = {"J-LDiDOvAp5PiE5PZx56Bg", "HeIv2xpid8OSu_YqFs8inw", "8Uq8gSxmvm6g5VBlEuSEUQ"}


# Returns the Pearson correlation coefficient for p1 and p2
def sim_pearson(prefs,p1,p2):
	# Get the list of mutually rated items
	si={}
	for item in prefs[p1]:
		if item in prefs[p2]: si[item]=1

	# Find the number of elements
	n=len(si)

	# if they are no ratings in common, return 0
	if n==0: return 0

	# Add up all the preferences
	sum1=sum([prefs[p1][it] for it in si])
	sum2=sum([prefs[p2][it] for it in si])

	# Sum up the squares
	sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
	sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

	# Sum up the products
	pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])

	# Calculate Pearson score
	num=pSum-(sum1*sum2/n)
	den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
	if den==0: return 0

	r=num/den

	return r

def transformPrefs(prefs): 
	result={}
	for person in prefs:
		for item in prefs[person]:
			result.setdefault(item,{})
			# Flip item and person
			result[item][person]=prefs[person][item]


	return result

# Returns the best matches for person from the prefs dictionary.
# Number of results and similarity function are optional params.
def topMatches(prefs,person,n=5,similarity=sim_pearson):
	scores=[(similarity(prefs,person,other),other) for other in prefs if other!=person]
	# Sort the list so the highest scores appear at the top
	scores.sort( )
	scores.reverse( )
	return scores[0:n]


def getRecommendedItems(prefs,itemMatch,user):
	userRatings=prefs[user]
	scores={}
	totalSim={}
	# Loop over items rated by this user
	for (item,rating) in userRatings.items( ):
		# Loop over items similar to this one
		for (similarity,item2) in itemMatch[item]:
			# Ignore if this user has already rated this item
			if item2 in userRatings: continue

			# Weighted sum of rating times similarity
			scores.setdefault(item2,0)
			scores[item2]+=similarity*rating

			# Sum of all the similarities
			totalSim.setdefault(item2,0)
			totalSim[item2]+=similarity

	# Divide each total score by total weighting to get an average
	rankings=[(score/totalSim[item],item) for item,score in scores.items( )]

	# Return the rankings from highest to lowest
	rankings.sort( )
	rankings.reverse( )

	return rankings



def calculateSimilarItems(prefs,n=10):
	# Create a dictionary of items showing which other items they
	# are most similar to.
	result={}
	# Invert the preference matrix to be item-centric
	itemPrefs=transformPrefs(prefs)
	c=0
	for item in itemPrefs:
		# Status updates for large datasets
		c+=1
		if c%100==0: print "%d / %d" % (c,len(itemPrefs))
		# Find the most similar items to this one
		scores=topMatches(itemPrefs,item,n=n,similarity=sim_pearson)
		result[item]=scores

	return result

def groupSimilarItems(group, dictionary):
	weightedRec={}
	for person in group:
		for score, movieName in getRecommendedItems(dictionary,itemsim,person):
			if movieName in weightedRec.keys():
				weightedRec[movieName] += score 
			else:
				weightedRec[movieName] = score
	
	return weightedRec

def getHighestRecommendation(recommendations):
	highest = 0
	index = 0
	for rec in recommendations.keys():
		if recommendations[rec] > highest:
			highest = recommendations[rec]
			index = rec
	return index



# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		# don't compare me to myself
		if other==person: continue
		sim=similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim<=0: continue
		for item in prefs[other]:
			# only score movies I haven't seen yet
			if item not in prefs[person] or prefs[person][item]==0:
				# Similarity * Score
				totals.setdefault(item,0)
				totals[item]+=prefs[other][item]*sim
				# Sum of similarities
				simSums.setdefault(item,0)
				simSums[item]+=sim



	# Create the normalized list
	rankings=[(total/simSums[item],item) for item,total in totals.items( )]

	# Return the sorted list
	rankings.sort( )
	rankings.reverse()
	return rankings


# Gets recommendations for a person by using a weighted average
# of every other user's rankings
def getRecommendations(prefs,person,similarity=sim_pearson):
	totals={}
	simSums={}
	for other in prefs:
		# don't compare me to myself
		if other==person: continue
		sim=similarity(prefs,person,other)

		# ignore scores of zero or lower
		if sim<=0: continue
		for item in prefs[other]:
			# only score movies I haven't seen yet
			#if item not in prefs[person] or prefs[person][item]==0:
			# Similarity * Score
			totals.setdefault(item,0)
			totals[item]+=prefs[other][item]*sim
			# Sum of similarities
			simSums.setdefault(item,0)
			simSums[item]+=sim



	# Create the normalized list
	rankings=[(total/simSums[item],item) for item,total in totals.items( )]

	# Return the sorted list
	rankings.sort( )
	rankings.reverse()
	return rankings


def getGroupRecommendations(group, dictionary):
	weightedRec={}
	for person in group:
		for score, movieName in getRecommendations(dictionary, person):
			if movieName in weightedRec.keys():
				weightedRec[movieName] += score 
			else:
				weightedRec[movieName] = score
	
	return weightedRec



##itemsim = calculateSimilarItems(critics)
##print itemsim
#similarItems = groupSimilarItems(group2)

#output = getHighestRecommendation(similarItems)



### Get A Final Answer with Yelp ####################
#rec = getGroupRecommendations(group2, yelpDict)		#
#output = getHighestRecommendation(rec)				#
#print output										#
#####################################################

### Get A Final Answer with Yelp ####################
rec = getGroupRecommendations(group1, critics)		#
output = getHighestRecommendation(rec)				#
print output										#
#####################################################










