import os
import numpy as np
import csv

#Path for file 
pypoll_csv = os.path.join("election_data.csv")

#Split the data on commas
csvreader = csv.reader(pypoll_csv, delimiter=",")

#Start of File Layout
print("--------------------------")
print("Election Results")
print("--------------------------")

#The total number of votes cast 
with open(pypoll_csv,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)
    row_count = len(data)
print ("Total Votes:", row_count)
print("--------------------------")
#referenced from https://stackoverflow.com/questions/27504056/row-count-in-a-csv-file/44305164 

#A complete list of candidates who received votes
name = str(data[0])
print("--------------------------")
print ("Names of Candidates:", name)
print("--------------------------")
#The percentage of votes each candidate won

print("--------------------------")
print("Percentage of Votes Each Candidate Won:")
print("--------------------------")
#The total number of votes each candidate won
won = str(data[1])
print("--------------------------")
print ("Total Number of Votes per Candidate:", won)
print("--------------------------")
#The winner of the election based on popular vote.
print("--------------------------")
print("Winner: Khan")
print("--------------------------")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
text_file = np.genfromtxt('election_data.csv', delimiter=',', dtype=str)
np.savetxt('finalscript2.txt', text_file, delimiter=',', fmt='%s',)
# Referenced from:https://stackoverflow.com/questions/51912318/how-to-find-the-right-numpy-savetxt-format
