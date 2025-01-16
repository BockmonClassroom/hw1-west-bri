# I haven't had the opportunity to learn python yet, so this code comes from a tutorial: https://www.geeksforgeeks.org/reading-csv-files-in-python/
# Hopefully I can catch up
import csv
with open('data/Iris.csv', mode = 'r') as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)