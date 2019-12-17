#import needed modules
import os
import csv

#set needed variables 
percent = "0%"
candidates= {}
row_count = 0
winner = "none"
winnervalue = 0  
winner = "No one"
#function call to allow for percentage calculation on each indvidual candidate
def percentagecalculator(counts):
    if counts ==0:
        return 0
    else:
        percent = counts/row_count *100 

        #converting to string to apply percent sign, rounding to 3 decimals
        return str(round(percent,3)) + "%"

#call the specific path for the budget csv file
election_count_path = os.path.join("learnpython","election_data.csv")

#csv will be called from the path established, establish rows
with open(election_count_path,newline="", encoding="utf8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter =",")
    
# skip over the headers
    csvheader = next(csv_reader)

    #cycle through the data in the csv
    for row in csv_reader:

        #calculate the total number of votes based on all rows counted
        row_count+=1

        #uses dictionary to count for each individual candidate, adds vote if existing 
        
        candidate = row[2]

        if candidate in candidates:
            candidates[candidate] = candidates[candidate]+1

        # creates and adds vote if not existing 
        else:
            candidates[candidate] = 1

    #print for each result in the dictionary

print(f"Election Results")
print(f"--------------------------")
print(f"Total votes: {row_count} ") 
print(f"--------------------------")   

# cycle through dictionary, prit each value while also utilizing percentage calculator fuction
for candidate,count in candidates.items():
    
    print(f"{candidate}: {percentagecalculator(count)} ({str(count)})")

# compares each number of votes, and if holding a larger vote count puts current candidate as winner    
    if count> winnervalue:
        winnervalue = count
        winner = candidate
print(f"--------------------------")
print(f"Winner: {winner}") 
print(f"--------------------------") 


#create .txt file with the results
output = open('electionresults.txt','w')
output.write(f"Election Results"+ '\n')
output.write(f"--------------------------"+ '\n')
output.write(f"Total votes: {row_count} "+ '\n') 
output.write(f"--------------------------"+ '\n')   

# cycle through dictionary, print each value while also utilizing percentage calculator fuction
for candidate,count in candidates.items():
    
    output.write(f"{candidate}: {percentagecalculator(count)} ({str(count)})"+ '\n')

# compares each number of votes, and if holding a larger vote count puts current candidate as winner    
    if count> winnervalue:
        winnervalue = count
        winner = candidate
output.write(f"--------------------------"+ '\n')
output.write(f"Winner: {winner}"+ '\n') 
output.write(f"--------------------------"+ '\n') 