# Brian West 1/15/2025
# I haven't had the opportunity to learn python yet, so this code comes from a tutorial: https://www.geeksforgeeks.org/reading-csv-files-in-python/
# Hopefully I can catch up
import csv
with open('data/Iris.csv', mode = 'r') as file: # open file as read only
    csvFile = csv.reader(file) # create reader object from file
    for lines in csvFile: # iterate through each line and print it
        print(lines)