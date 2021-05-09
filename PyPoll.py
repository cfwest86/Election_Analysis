
# requirements of python script. 

#Total number of votes cast
#A complete list of candidates who received votes
#Total number of votes each candidate received
#Percentage of votes each candidate won
#The winner of the election based on popular vote

#Add our Dependencies 
import csv
import os

#Assign variable for file to load and the path
file_to_load = os.path.join('Resources', 'election_results.csv')
# Create a filename variable to indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize variable for accumulator, total vote counter 
total_votes=0

#Declare new [list] 
candidate_options = []

#Create new empty {Dictionary} to hold candidates and their coresponding vote counts
candidate_votes={}

#Create winning candidate str variable and winning count tracker and set to 0
winning_candidate = ""
winning_count= 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:

    #Read the file object with the csv module reader function
    file_reader= csv.reader(election_data)

    #Ignore header row in the CSV file 
    headers = next(file_reader)
    
    #loop through each row in the CSV 
    for row in file_reader:
        #add to total vote count 
        total_votes += 1

        #Print the candidates name from each row
        candidate_name = row[2]

        #if candidate does not match any exiting candidate...
        if candidate_name not in candidate_options:
            #Add candidate name to the candidate [list]
            candidate_options.append(candidate_name)
            # Begin Tracking that candidates vote count.
            candidate_votes[candidate_name] = 0
         #Add a vote to that candidates count.
        candidate_votes[candidate_name] += 1

    

#1. Iterate through candidate list 
    for candidate_name in candidate_votes:
         #2 retrieve vote count of a candidate 
        votes = candidate_votes[candidate_name]
        #3 calculate percentage of cotes with floating decimal 
        vote_percentage=float(votes)/float(total_votes) * 100
        #4 print candidate name and percentages of vote

        #To do: Print out each candidates name, vote count, and percentage of votes to terminal
        print(f'{candidate_name}:{vote_percentage:.1f}%({votes:,})\n')
        
        #Determine winning vote count and cadidate 
        #1 Determine if the votes are greater than the winning count. 
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        #2 If true set winning_count = votes and winning_percent = vote percentage 
            winning_count= votes
            winning_percentage= vote_percentage
        #3 set the winning_canddiate equal to the candidates name 
            winning_candidate = candidate_name

    winning_candidate_summary= (f'-------------------------\n'
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)




        