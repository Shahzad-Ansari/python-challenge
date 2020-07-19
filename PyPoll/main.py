import pandas as pd

#Loading csv into data frame
data = pd.read_csv("Resources/election_data.csv")

# finding how many voters they are 
voterCount = data['Voter ID'].count()

# find the values count for each canidate 
voterDist = data['Candidate'].value_counts()

# find the value count for each candidate in a normalized percentage 
voterDistPercent = data['Candidate'].value_counts(normalize = True)*100

# casting each the name , the count and the percentage to lists 
voterDistPercent = voterDistPercent.tolist()
voterDistNames = voterDist.index.tolist()
voterDistCount = voterDist.tolist()

#mergning into one list of 3 tuples 
voterDistList = [(voterDistNames[i], voterDistCount[i], 
	round(voterDistPercent[i])) for i in range(0, len(voterDistNames))]

#The winner will be the one with the most occurences in the data set, use mode
winner = data['Candidate'].mode().iloc[0]

#output values 
print("Election Results")
print("----------------")
print("Total Votes:" + str(voterCount))
print("----------------")
#string formating of the list of tuples 
for tup in voterDistList:print(f'{tup[0]}: {tup[2]}% ({tup[1]})')
print("----------------")
print("Winner:" + str(winner))
print("----------------")

#log to file 
with open('analysis/poll.txt' ,'w+') as logFile:
	logFile.write("Election Results")
	logFile.write("\n----------------\n")
	logFile.write("Total Votes:" + str(voterCount))
	logFile.write("\n----------------\n")	
	for tup in voterDistList:logFile.write(f'{tup[0]}: {tup[2]}% ({tup[1]})')
	logFile.write("\n----------------\n")
	logFile.write("Winner:" + str(winner))
	logFile.write("\n----------------\n")




