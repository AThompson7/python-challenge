import os
import csv
import statistics

poll_csv = os.path.join("Resources", "election_data.csv")

idcount = 0
idlist = []
candidates = []
charles_votes = 0
diana_votes = 0
raymon_votes = 0


with open(poll_csv, encoding = "utf-8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    csv_header = next(csv_reader)

    for row in csv_reader:
        idcount += 1
        idlist.append(row[0])
        candidates.append(row[2])

        if row[2] == "Charles Casper Stockham":
            charles_votes += 1
        elif row[2] == "Diana DeGette":
            diana_votes += 1
        elif row[2] == "Raymon Anthony Doane":
            raymon_votes += 1
        
charles_votes_percent = charles_votes / len(candidates)
diana_votes_percent = diana_votes / len(candidates)
raymon_votes_percent = raymon_votes / len(candidates)

print("Election Results")
print("------------------------")
print(f'Total Votes: {len(candidates)}')
print("------------------------")
print(f'Charles Casper Stockham: {charles_votes_percent:.3%} ({charles_votes})')
print(f'Diana Degette: {diana_votes_percent:.3%} ({diana_votes})')
print(f'Raymon Anthony Doane: {raymon_votes_percent:.3%} ({raymon_votes})')
print("------------------------")
print(f'Winner: {statistics.mode(candidates)}')
print("------------------------")

output_path = os.path.join("analysis", "Election Results.txt")
with open(output_path, "w") as file:
    file.write("Election Results" "\n")
    file.write("--------------------------------" "\n")
    file.write(f'Total Votes: {len(candidates)}')
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f'Charles Casper Stockham: {charles_votes_percent:.3%} ({charles_votes})')
    file.write("\n")
    file.write(f'Diana Degette: {diana_votes_percent:.3%} ({diana_votes})')
    file.write("\n")
    file.write(f'Raymon Anthony Doane: {raymon_votes_percent:.3%} ({raymon_votes})')
    file.write("\n")
    file.write("------------------------")
    file.write("\n")
    file.write(f'Winner: {statistics.mode(candidates)}')
    file.write("\n")
    file.write("------------------------")

