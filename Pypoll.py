# 1. Total number of votes cast
# 2. A complete list of candidates who received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate received
# 5.The winner of the election based on popular vote

# Add dependencies
import os
import csv

# # Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# # Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")

# # Open the election results and read the file.
with open(file_to_load,'r',encoding = 'utf-8') as election_data:

#  # # To do: read and analyze the data here.
 file_reader = csv.reader(election_data)

 #Read and print the header row.
 headers = next(file_reader)
 print(headers)

  # Print each row in the CSV file.
#  for row in file_reader:
#       print(row)




































# import sys
# r= sys.getdefaultencoding()
# print(r)




