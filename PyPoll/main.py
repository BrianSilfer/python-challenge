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
    # Read the header row first 
    csv_header = next(csv_file)

    #create row_count variable
    row_count = 0
    #create Variable for vote count starts at 1 because first vote is considered 1 not 0
    vote_count = 1
    vote_count_cand1 = 1
    vote_count_cand2 = 1
    vote_count_cand3 = 1
    # create empty list for candidate names
    cand_name = []
    #create votes list for Winner calculation
    vote_list=[]
    #create dictionary with key as empty candidate name list and value as empty total votes
    cand_dict = {"name":[],"votes":[]}
    for row  in csv_reader:
        row_count += 1
        if row[2] not in cand_name:
            cand_name.append(row[2])
            cand_dict["name"].append(row[2])
        
        elif row[2] == cand_name[0]:
            vote_count_cand1 += 1
                    
        elif row[2] == cand_name[1]:
            vote_count_cand2 += 1
            
        elif row[2] == cand_name[2]:
            vote_count_cand3 += 1 
             
vote_list = [vote_count_cand1,vote_count_cand2,vote_count_cand3]    
 
cand_dict["votes"] = vote_list        
#taking out first entry in dict names
name_list = ['Charles Casper Stockham', 'Diana DeGette', 'Raymon Anthony Doane']
cand_dict["name"] = name_list
#adding cand vote count to dict



#Print Final Results
print("Election Results")
print("-------------------------------------------------------------")
#print total rows for total ballot count minus 1 for not counting header
print(f"Total votes: {row_count}")
print("-------------------------------------------------------------")
print(f'{cand_dict["name"][0]}: {(round(((cand_dict["votes"][0])/row_count),5)*100)}% ({cand_dict["votes"][0]})')
print(f'{cand_dict["name"][1]}: {(round(((cand_dict["votes"][1])/row_count),5)*100)}% ({cand_dict["votes"][1]})')
print(f'{cand_dict["name"][2]}: {(round(((cand_dict["votes"][2])/row_count),5)*100)}% ({cand_dict["votes"][2]})')
print("-------------------------------------------------------------")
print("Winner: " + cand_dict["name"][vote_list.index(max(vote_list))])
print("-------------------------------------------------------------")


# save the output file path
output_file_2= '/Users/briansilfer/Desktop/git/python-challenge/PyPoll/analysis/pypoll_analysis.txt'
#writing output lines to be joined by \n
lines = (f'Election Results\n'
        '---------------------------------------','\n'
        'Total votes: 369711''\n',
        'Charles Casper Stockham: 23.049% (85213)''\n',
        'Diana DeGette: 73.812% (272892)''\n',
        'Raymon Anthony Doane: 3.1390000000000002% (11606)''\n',
        '---------------------------------------','\n'
        'Winner: Diana DeGette','\n'
        '---------------------------------------',)

#Writing text file to output path
with open(output_file_2,'w') as file:
    file.write('\n'.join(lines))
    

