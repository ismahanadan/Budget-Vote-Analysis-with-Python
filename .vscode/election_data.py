
#Import the os module to enable creationo file paths across operating systems
import os

csvpath = os.path.join('election_data.csv')


#Import module to read csv files
import csv


with open(csvpath, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    
    
    #Read through each row of data after the header
    for row in csvreader:
        print(Votes)
       





   






        

            




