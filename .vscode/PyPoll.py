
#Import the os module to enable creationo file paths across operating systems
import os

csvpath = os.path.join('election_data.csv')


#Import module to read csv files
import csv
#def csv_dict(csvpath, fieldnames):
csv_dict = []

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile)
    for row in csvreader:
        csv_dict.append(row)
        #print(csv_dict)

        

field_names = ['Voter ID', 'County','Candidate']   

#total_votes = lenght of csv_dict
#print(len(csv_dict))

#List of Candidates
#candidate.sort({row[2]})
#print(row[2])

for row in csv_dict:
    













    

    
    
    #Read through each row of data after the header
    #for row in csvreader:
        #print(row)