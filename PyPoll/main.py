import os
import csv

election_csv = '/Users/ismahanadan/Desktop/python-challenge/PyPoll/election_data.csv'

votes = []
candidates = []

# Open and read csv
with open(election_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    # Read the header row first 
    csv_header = next(csv_file)
    #print(f"Header: {csv_header}")
    row_count = 0
    votes = []
    candidates = []
    candidate_votes = []
    # Read through each row of data after the header to get total vote count
    for row in csv_reader:
        row_count += 1
        votes = row[0]
        candidates = row[2]
        candidate_name = row[2]
    #Sort individual candidates in the list of candidates
    for candidate in candidate_name:
        if candidate_name not in candidates:
            candidates.append(candidate_name)
       

        
        






    print("Election Results")

    print("-----------------------------") 
        
    print(f'Total Votes: {row_count}')
    print("------------------------------")
    print(f"candidate_names") 
   

#To export a text file with the results
with  open("ByPoll_output.txt", "w") as text_file:
    text_file.write(f"Total Votes: {row_count}")  

    text_file.close() 


        

    














    

    
    
   