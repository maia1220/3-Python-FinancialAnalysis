## PyPoll


import os
import csv

# Absolute Path
# csvpath = "/Users/aq/Documents/Classwork/vu-nsh-data-pt-02-2020-u-c/03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv"

# Relative Path
csvpath = os.path.join(os.path.expanduser('~'),"Documents/Classwork/vu-nsh-data-pt-02-2020-u-c", "03-Python/Homework/Instructions/PyPoll/Resources/election_data.csv")

#create a new list to only store the candidates
candidate_list = []

#open the csvfile
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        voteid = row["Voter ID"]
        county = row["County"]
        candidate_list.append(row["Candidate"])

#find the unique candidates and store that in a list
unique_candidate_list = []
for x in candidate_list:
    if x not in unique_candidate_list:
        unique_candidate_list.append(x)

for x in unique_candidate_list:
        print(x)

#find the total number of votes
total_vote = len(candidate_list)

#find the total votes for each unique candidate and store that in a list
unique_votecount = []
for candidate in unique_candidate_list:
    unique_votecount.append(candidate_list.count(candidate)) 

#store both total votes and unique candidates in a list
vote_candidate_list = list(zip(unique_candidate_list, unique_votecount))
#find the candidate with max votes
maxvote = max(vote_candidate_list, key=lambda x:x[1])
winner = maxvote[0]

#find the percentage of votes for each candidate
c1percent = "{:.3%}".format(vote_candidate_list[0][1]/total_vote)
c2percent = "{:.3%}".format(vote_candidate_list[1][1]/total_vote)
c3percent = "{:.3%}".format(vote_candidate_list[2][1]/total_vote)
c4percent = "{:.3%}".format(vote_candidate_list[3][1]/total_vote)

# Summary Table
# Absolute Path
# outputpath = "/Users/aq/Documents/Classwork/vu-nsh-data-pt-02-2020-u-c/03-Python/Homework/Instructions/PyPoll/Resources/output.txt"
# Relative Path
outputpath = os.path.join(os.path.expanduser('~'),"Documents/Homework/03-Python-Challenge", "PyPoll","output.txt")

#export the summary table to a text file
with open(outputpath, "a") as f:

    print("Election Results \n-------------------------", file =f)
    print(f'Total Votes: {total_vote}\n-------------------------', file =f)
    print(f'{vote_candidate_list[0][0]}: {c1percent} ({vote_candidate_list[0][1]})', file =f)
    print(f'{vote_candidate_list[1][0]}: {c2percent} ({vote_candidate_list[1][1]})', file =f)
    print(f'{vote_candidate_list[2][0]}: {c3percent} ({vote_candidate_list[2][1]})', file =f)
    print(f'{vote_candidate_list[3][0]}: {c4percent} ({vote_candidate_list[3][1]})', file =f)
    print("-------------------------", file =f)
    print(f'Winner: {winner}', file =f)
    print("-------------------------", file =f)
