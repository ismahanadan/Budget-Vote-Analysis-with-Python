import os
import csv

election_csv = '/Users/ismahanadan/Desktop/python-challenge/PyPoll/election_data.csv'

candidates = [] 
candidate_votes = []
# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    row_count = 0
    
    # Read through each row of data after the header to get total vote count
    for row in csv_reader:
        row_count += 1
        candidate_votes.append(row[0])
       # Get list of candidate name

        for candidate in candidates:
            if candidate not in candidates:
                candidate.append(row[2])
        # Get count of votes each candidate received   
        #candidate_votes[candidates] = 0
        #candidate_votes.append(candidates.count(candidates))  
        #candidate_votes[candidates] = candidate_votes[candidates] + 1   

        
        






    print("Election Results")
    print("-----------------------------")     
    print(f'Total Votes: {row_count}')
    print("------------------------------")
    #print(f"candidate") 
    #print(f"")

#To export a text file with the results
with  open("ByPoll_output.txt", "w") as text_file:
    text_file.write(f"Total Votes: {row_count}")  

    text_file.close() 


        

    














    

    
    
   