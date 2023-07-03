import os
import csv

#Set variable for input file
election_csv_path = os.path.join( "Resources", "election_data.csv")

# Set variable for output file
budget_csv_path = os.path.join("Analysis","Election_Results.txt")

#Lists to store data
Votes = []
Candidate_List = []

#Dictionary to store data
Votes_Per_Candidate = {}

#Set initial value for winner
Winning_Votes = 0 

#Open CSV file
with open(election_csv_path, newline='') as csvfile:
    #Seperate data by comma ','
    election_reader = csv.reader(csvfile, delimiter=',')

    #Skip the header row
    next(election_reader)
    
    #Create Loop to loop through CSV File 
    for row in election_reader:

        #Add Votes
        Votes.append(row[2])
        
        #The total number of votes cast
        Total_Votes = len(Votes)
 
        #Set row 2 to candidate to refer to them by name
        Candidates_Name = row[2]

    #A complete list of candidates who received votes
    #The total number of votes each candidate won
        if Candidates_Name not in Candidate_List:

            #Add names to Candidate List
            Candidate_List.append(Candidates_Name)

            #Start keeping track of candidate's vote
            Votes_Per_Candidate[Candidates_Name] = 1

        else:
            #Add vote to candidate's total vote count
            Votes_Per_Candidate[Candidates_Name] += 1

# Open the output file
with open(budget_csv_path, "w") as textfile:
    #Print total votes to Terminal
    output=( f'Election Results\n'
            f'-------------------------\n'
            f'Total Votes: {Total_Votes}\n'
            f'-------------------------\n')
    
    #Print output to terminal
    print(output)

    #Write output to textfile
    textfile.write(output)

    #Create for statement to find percentage of votes per candidate
    for Candidates_Name in Votes_Per_Candidate:

        #Pull Candidates Name and Total Votes Per Candidate data to then calculate Percentage  
        #Used get function to pull from dictionary created
        Candidate_Total_Votes = Votes_Per_Candidate.get(Candidates_Name)

        #The percentage of votes each candidate won
        Percentage = Candidate_Total_Votes / Total_Votes * 100

        #Print candidate's names, percentages and total votes to terminal
        output2 = (f"{Candidates_Name} : {Percentage:.3f}% ({Candidate_Total_Votes})\n")

        #Print output2 to terminal
        print(output2)

        #Write output2 to textfile
        textfile.write(output2)

        #The winner of the election based on popular vote
        #Create if state to determine the winner 
        if Candidate_Total_Votes > Winning_Votes: 

            #Winning candidate has vote equal to popular vote
            Winning_Votes = Candidate_Total_Votes

            #State Winner by Name
            Winner = Candidates_Name

    #Print progress to terminal
    output3= (f'-------------------------\n'
              f'Winner: {Winner}\n-------------------------')
    
    #Print output3 to terminal
    print(output3)

    #Write output3 to textfile
    textfile.write(output3)