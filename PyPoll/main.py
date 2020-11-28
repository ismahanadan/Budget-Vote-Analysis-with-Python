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
    votes =[]
    candidates = [] 
    candidate_votes = []
    # Read through each row of data after the header
    for row in csv_reader:
        row_count += 1
        candidate_name = row[2]
        for candidate in candidate_name:
            if candidate_name not in candidates:
                candidates.append(candidate_name)
        for candidate in candidate_name:
            candidate_votes.append(candidate_name.count(candidate))
            



                
            
        
       
        #print(len(csv_reader))

    print("Election Results")
    print("-----------------------------")     
    print(f'Total Votes: {row_count}')
    print("------------------------------")
    print(candidates) 
    #print(f"[candidates[i]}: {'{: .2%}' .format(row_count[i]/len(candidate_name))} ({row_count[i]})")

     
    #print("Winner: Khan")

        

    














    

    
    
   