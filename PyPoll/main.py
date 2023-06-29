import os
import csv

election_csv_path = os.path.join( "Resources", "election_data")

#Lists to store data


#Open CSV file
with open(election_csv_path, newline='') as csvfile:
    #Seperate data by comma ','
    election_reader = csv.reader(csvfile, delimiter=',')

    #Skip the header row
    next(election_reader)
    
    #Create Loop to loop through CSV File
    #for row in election_reader:
    

#The total number of votes cast

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote



#'''Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------'''