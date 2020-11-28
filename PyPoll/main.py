import os
import csv

#election_csv = os.path.join('election_data.csv')

election_csv = '/Users/ismahanadan/Desktop/python-challenge/PyPoll/election_data.csv'

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    votes = {'Voter ID': 'row[0]' , 'County': 'row[1]' , 'Candidate': 'row[2]'}
    # Read the header row first 
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    row_count = 0
    votes =[] #row0
    candidates = [] 
    candidate_votes = []
    # Read through each row of data after the header to get total vote count
    for row in csv_reader:
        row_count += 1
        votes = row[0]
        candidate_name = row[2] #row2
        # Get list of candidate name
        for candidate in candidate_name:
            if candidate_name not in candidates:
                candidates.append(candidate_name)
        # Get count of votes each candidate received   
        for candidate in candidate_name:
            candidate_votes.append(candidate_name.count(candidate))     

        
        






                
            
        
       
       

    print("Election Results")
    print("-----------------------------")     
    print(f'Total Votes: {row_count}')
    print("------------------------------")
    print(candidates) 
    print(candidate_votes)

     
    #print("Winner: Khan")

        

    














    

    
    
   