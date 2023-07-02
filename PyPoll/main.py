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
 
        #Set row 2 to candidates to refer to them by name
        Candidates_Name = row[2]

    #A complete list of candidates who received votes
    #The total number of votes each candidate won
        if Candidates_Name not in Candidate_List:

            #Add Candidate List
            Candidate_List.append(Candidates_Name)
        
            #Add candidate names and votes per candidate 
            Votes_Per_Candidate[Candidates_Name] = 1
        else:
            Votes_Per_Candidate[Candidates_Name] += 1
    #Print progress to Terminal
    print1= f'''Election Results
-------------------------
Total Votes: {Total_Votes}
-------------------------\n'''
    print(print1)


    #Create for statement to find percentage of votes per candidate
    for Candidates_Name in Votes_Per_Candidate:

        #Pull Candidates Name and Total Votes per Candidate data to then calculate percentage  
        #Used get function to pull from dictionary created
        Candidate_Total_Votes = Votes_Per_Candidate.get(Candidates_Name)

        #The percentage of votes each candidate won
        Percentage = Candidate_Total_Votes / Total_Votes * 100

        #Print progress to terminal
        print2 = (f"{Candidates_Name} : {Percentage:.2f}% ({Candidate_Total_Votes})")
        print(print2)


    #The winner of the election based on popular vote
    Winner = max(Candidate_List)

    #Print progress to terminal
    print3= '''\n-------------------------
'''
    print4 = f'''Winner: {Winner}\n-------------------------'''
    
    print(print3)
    print(print4)


#  Open the output file
with open(budget_csv_path, "w") as textfile:

    #Write to textfile
    textfile.write(print1)
    textfile.write(print2)
    textfile.write(print3)
    textfile.write(print4)



    
