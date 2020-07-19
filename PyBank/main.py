'''
Shahzad Ansari 

'''
import pandas as pd

# loading csv into data frame
data = pd.read_csv("Resources/budget_data.csv")

# calculating how many months
months = len(data.Date.unique())

# summing up the profit/losses col to get the total profit
profit = data['Profit/Losses'].sum()

# creating a new column containg the differences of an entry and the next 
data['difference'] = data['Profit/Losses'] - data['Profit/Losses'].shift(1)
# calculate the average difference and the locations of the lowest and highest difference 
avg = data['difference'].mean()
maxInc = data['difference'].argmax()
maxDec = data['difference'].argmin()
 

# oputput results 
print("     Financial Analysis     \n---------------------------")
print("Total Months: " + str(months))
print("Total: " + str(profit) + " $")
print("Average Change: " + str(round(avg,2)) + " $")
print("Greatest Increase in Profits : " + str(data.loc[maxInc,'Date']) + " " + str(round(data.loc[maxInc,'difference'] ,2)) + " $")
print("Greatest Decrease in Profits : " + str(data.loc[maxDec,'Date']) + " " + str(round(data.loc[maxDec,'difference'] ,2)) + " $")

#output to log file 
with open('analysis/bank.txt' ,'w+') as logFile:
	logFile.write("     Financial Analysis     \n---------------------------\n")
	logFile.write("Total Months: " + str(months) + "\n")
	logFile.write("Total: " + str(profit) + " $" + "\n")
	logFile.write("Average Change: " + str(round(avg,2)) + " $"+ "\n")
	logFile.write("Greatest Increase in Profits : " + str(data.loc[maxInc,'Date']) + " " + str(round(data.loc[maxInc,'difference'] ,2)) + " $" + "\n")
	logFile.write("Greatest Decrease in Profits : " + str(data.loc[maxDec,'Date']) + " " + str(round(data.loc[maxDec,'difference'] ,2)) + " $" + "\n")



