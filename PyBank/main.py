import os
import numpy as np
import csv

#Path for file 
pybank_csv = os.path.join("PyBank", "Resources", "budget_data.csv") #or just put: "budget_data.csv" in ()

#Open the CSV
csvreader = csv.reader(pybank_csv, delimiter=",")

#Start of file layout
print("Financial Analysis")
print("--------------------------")

#The total number of months included in the dataset (-1 to cut the header line)
total_months = -1
with open(pybank_csv, 'r') as f:
    for l in f:
        total_months = total_months +1
    #referenced from https://www.codevscolor.com/python-count-total-lines-file 
print ("Total Months:", total_months)

#The net total amount of "Profit/Losses" over the entire period

print("Total:$")

#The average of the changes in "Profit/Losses" over the entire period

print("Average Change:$")

#The greatest increase in profits (date and amount) over the entire period

print("Greatest Increase in Profits:")

#The greatest decrease in losses (date and amount) over the entire period

print("Greatest Decrease in Profits:")

#In addition, your final script should both print the analysis to the terminal and export a text file with the results.
pybank_csv = np.genfromtxt('budget_data.csv', delimiter=',', dtype=str)
np.savetxt('finalscript.txt', pybank_csv, delimiter=',', fmt='%s')
# Referenced from:https://stackoverflow.com/questions/51912318/how-to-find-the-right-numpy-savetxt-format