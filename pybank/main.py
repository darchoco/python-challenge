#import needed modules
import os
import csv

#establish variables that will be called in csv loop
rowcount = 0
nettotal = 0
average_change_list = []
largestincrease = 0
greatestdecrease = 0
previoustotal = 0

#set to the initial total in the CSV file... stupid hard coding
currenttotal = 0

largestincreasemonth = 'none'
greatestdecreasemonth = 'none'

#create function to calculate average change after list is created in for statement
def averagechange(numbers):
    length = len(numbers) 
    total = 0
    for num in numbers:
        total += num
    return total/length


#call the specific path for the budget csv file
budgetpath = os.path.join("learnpython","budget_data.csv")

#csv will be called from the path established, establish rows
with open(budgetpath,newline="", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter =",")
    
# skip over the headers
    csvheader = next(csvreader)

    #cycle through the data in the csv
    for row in csvreader:

        #establish previous total as current total before current total change occurs to allow for future calculations 
        previoustotal = currenttotal

        #ignore blank lines for calculation purposes
        if row[0] == None:
            break

        #do initial caculation to append for first round of profits
        elif rowcount == 0:
            currenttotal = row[1]
        
        #establish caculation to pull new total, make the other total
        elif currenttotal != row[1]:
            currenttotal =  row[1]
            average_change_list.append(int(currenttotal) - int(previoustotal))
 
        #calculate the total months by counting the number of rows
        rowcount += 1
        
        #calculate the total by adding with each row, call specific area
        nettotal += int(row[1])

        #caculate the change in total, store to list averagechange, then change total to previous
       
        #establish loop to determine highest profits in a month
        if int(row[1]) > int(largestincrease):
            
            #pull name of current highest
            largestincreasemonth = row[0]

            #updated increase to largest number so far
            largestincrease = row[1]

        #estalbish loop to determine the largest decrease in a month
        if int(row[1]) < int(greatestdecrease):

            #pull name of current lowest month
            greatestdecreasemonth = row[0]

            #updated decrease to lowest number so far
            greatestdecrease = row[1]
        

#print results
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {rowcount}")
print(f"Total: {nettotal}")
print(f"average change: {averagechange(average_change_list)}")
print(f"Greatest Increase in Profits: {largestincreasemonth} ({largestincrease})")
print(f"Greatest Increase in Profits: {greatestdecreasemonth} ({greatestdecrease})")

#create .txt file with the results
output = open('results.txt','w')
output.write(f"Financial Analysis" + '\n')
output.write(f"----------------------------"+ '\n')
output.write(f"Total Months: {rowcount}"+ '\n')
output.write(f"Total: {nettotal}"+ '\n')
output.write(f"average change: {averagechange}"+ '\n')
output.write(f"Greatest Increase in Profits: {largestincreasemonth} ({largestincrease})"+ '\n')
output.write(f"Greatest Increase in Profits: {greatestdecreasemonth} ({greatestdecrease})"+ '\n')