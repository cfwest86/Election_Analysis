# Election_Analysis

## Project Overview
The Colorado Board of Elections assigned the following tasks in relation to the election audit of a recent local congressional election.

* Calculate the total number of votes cast
* Determine the percentage and vote count by County
* Identify which county had the largest turnout
* Compile a complete list of candidates who recieved votes
* Calculate the number of votes and percentage of the vote each candidate won
* Determine the winner of the election based on popular vote 

Data was pulled from the provided "election_results.csv" file, code specific to the above requirements was written using Python, analyzis was conducted, and results were displayed both in the terminal and saved to the accompanying txt file "election_analysis" 

## Election Audit Results 
![ELection results print out](https://user-images.githubusercontent.com/81761879/117582244-17dcd780-b0cf-11eb-96f8-e84378fb82db.PNG)

The above results show that:
* 369,711 votes were cast in the election
* County Breakdown:
  * Arapahoe County cast 24,801 votes or 6.7% of the total vote
  * Jefferson County cast 38,855 votes or 10.5% of the total vote
  * Denver County cast 306,055 votes or 82.8% of the vote 
  * Denver had far and away the largest number of votes cast 
* Candidate Breakdown:
  * Raymon Anthony Doane recieved 11,606 votes or 3.1% of the total vote
  * Charles Casper Stockham recieved 85,213 votes or 23% of the vote
  * Diana Degette recieved 272,892 votes or 73.8% of the total vote 
* Winner: Diana Degette was the clear winner of the election 

## Election Audit SUmmary 

Repurposing of the Python code created for this assignment could prove fairly valuable for future elections. For instance, the code could easily be applied to a larger statewide election. As long as election data is provided in a csv file, we can easily change the file_to_load = os.path.join ( ) to what and where the new election data files are named and stored. 

![indexs of county code](https://user-images.githubusercontent.com/81761879/117582821-ea455d80-b0d1-11eb-8aa7-dce88b5514e9.PNG)

Indeed, as shown in the code snippet above, even if these new csv files changed the columns the county and candidate information is stored, we could very easily change the index for each of these variables and achieve the same output as the results of this audit. 

![for loop](https://user-images.githubusercontent.com/81761879/117583009-dfd79380-b0d2-11eb-90fb-80dfa1fabce7.PNG)


Similarly, because we use a for loop to compile total vote counts, as shown above, it would not matter how many counties, votes, or candidates were in the election. Our code would account for all of them. 

Repurposing the code in this way could save the state valuable resources in both time and money in future elections. 







* 
