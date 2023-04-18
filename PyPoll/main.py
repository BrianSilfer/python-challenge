#import os and csv library
import os
import csv
#checks current directory for file assingment
#print(os.getcwd())

#Create file variable to hold file path
file = '/Users/briansilfer/Desktop/git/python-challenge/PyPoll/Resources/election_data.csv'


#opens file 
with open(file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    
    #create row_count variable
    row_count = 0
    #create Variable for vote count
    vote_count = 0
    vote_count_cand1 = 0
    vote_count_cand2 = 0
    vote_count_cand3 = 0
    # create empty list for candidate names
    cand_name = []
    
    #create dictionary with key as empty candidate name list and value as empty total votes
    cand_dict = {"name":[],"votes":[]}
    for row  in csv_reader:
        row_count += 1
        if row[2] not in cand_name:
            cand_name.append(row[2])
            cand_dict["name"].append(row[2])
        
        

        if row[2] == 'Charles Casper Stockham':
            vote_count_cand1 += 1
        elif row[2] == 'Diana DeGette':
            vote_count_cand2 += 1
        elif row[2] == 'Raymon Anthony Doane':
            vote_count_cand3 += 1   

#taking out first entry in dict names
print(cand_dict["name"])
name_list = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
cand_dict["name"] = name_list
print(cand_dict["name"])
#adding cand vote count to dict
cand_dict["votes"] = vote_count_cand1 , vote_count_cand2 , vote_count_cand3

  



row_count=row_count-1
#Print Final Results
print("Election Results")
print("-------------------------------------------------------------")
#print total rows for total ballot count minus 1 for not counting header
print(f"Total votes: {row_count}")
print("-------------------------------------------------------------")
print(f'{cand_dict["name"][0]}: {(round(((cand_dict["votes"][0])/row_count),5)*100)}% ({cand_dict["votes"][0]})')
print(f'{cand_dict["name"][1]}: {(round(((cand_dict["votes"][1])/row_count),5)*100)}% ({cand_dict["votes"][1]})')
print(f'{cand_dict["name"][2]}: {(round(((cand_dict["votes"][2])/row_count),3)*100)}% ({cand_dict["votes"][2]})')
print("-------------------------------------------------------------")
print("Winner: " + cand_dict["name"][1])
print("-------------------------------------------------------------")