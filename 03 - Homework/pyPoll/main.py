import os
import csv

currentDir =  os.getcwd()
print(currentDir)
file = os.path.join(currentDir, "pyPoll", "Resources","election_data.csv")

# Reads and accomodates the data into list
with open(file, 'r', newline='', encoding='utf8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader, None)
    voter_id = []
    county = []
    candidate = []
    for row in csvreader:
        voter_id.append(row[0])
        county.append(row[1])
        candidate.append(row[2])

# Fill a matrix (election) with the data from file
election = list(zip(voter_id, county, candidate))

# The number of voters and make a unique list of candidates
list_cand = []
tot_num_voters = len(election)
for i in range(tot_num_voters):
    if candidate[i] not in list_cand: list_cand.append(candidate[i])

# The number of voters for each candidate and make a list of them
voters_cand = []
for cand in list_cand:
    num_vot = 0
    for i in range(tot_num_voters):
        if election[i][2] == cand:
            num_vot += 1
    voters_cand.append(num_vot)

# Percentage of voters for each candidate
percent_of_voter = [(i / tot_num_voters) * 100 for i in voters_cand]

# Determines the winner candidate
winner_index = [i for i, perc in enumerate(percent_of_voter) if perc == max(percent_of_voter)]
winner = list_cand[winner_index[0]]

# Shows results to the terminal
print('\nElection Results')
print('-------------------------------')
print(f'Total votes: {tot_num_voters}')
print('-------------------------------')
for k in range(len(list_cand)):
    print(f'{list_cand[k]}: {percent_of_voter[k]: 0.3f}% ({voters_cand[k]})')
print('-------------------------------')
print(f'Winner: {winner}')
print('-------------------------------')

# Write results to a csv file
output_file = os.path.join(currentDir, "pyPoll", "Resources", "results_election.csv")
with open(output_file, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=" ")
    csvwriter.writerow('Election Results')
    csvwriter.writerow('-------------------------------')
    csvwriter.writerow(f'Total votes: {tot_num_voters}')
    csvwriter.writerow('-------------------------------')
    for k in range(len(list_cand)):
        csvwriter.writerow(f'{list_cand[k]}: {percent_of_voter[k]: 0.3f}% ({voters_cand[k]})')
    csvwriter.writerow('-------------------------------')
    csvwriter.writerow(f'Winner: {winner}')
    csvwriter.writerow('-------------------------------')