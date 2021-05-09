
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

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyize data here

    #Read the file object with the csv module reader function
    file_reader= csv.reader(election_data)

    #Print header row in the CSV file 
    headers = next(file_reader)
    print(headers)


