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
    print(f"Header: {csv_header}")
    row_count = 0
    candidate = str('row2')

    # Read through each row of data after the header
    for row in csv_reader:
        row_count += 1
       
        #print(len(csv_reader))
         
    print(f'Number of votes: {row_count}')
#List of Candidates
        candidate.sort({row[2]})
    print(row[2])



    













    

    
    
    #Read through each row of data after the header
    #for row in csvreader:
        #print(row)