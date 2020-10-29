import os
import numpy as np
import csv

#Path for file 
pypoll_csv = os.path.join("..", "Resources", "election_data.csv") #or just put: "election_data.csv" in ()

#Split the data on commas
csvreader = csv.reader(pypoll_csv, delimiter=",")

#Start of File Layout
print("Election Results")
print("--------------------------")

#The total number of votes cast 
total_votes = -1
with open(pypoll_csv, 'r') as f:
    for l in f:
        total_votes = total_votes +1
print ("Total Votes:", total_votes)
print("--------------------------")
#referenced from https://www.codevscolor.com/python-count-total-lines-file 

#A complete list of candidates who received votes

#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote.
print("--------------------------")
print("Winner:")
print("--------------------------")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
text_file = np.genfromtxt('election_data.csv', delimiter=',', dtype=str)
np.savetxt('finalscript2.txt', text_file, delimiter=',', fmt='%s',)
# Referenced from:https://stackoverflow.com/questions/51912318/how-to-find-the-right-numpy-savetxt-format
