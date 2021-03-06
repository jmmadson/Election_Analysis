# The data we need to retrieve
# 1. The total number of votes cast
# 2. The complete list of candidates who recieved votes
# 3. The percentage og votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

import csv
import os
  
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []

#Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:

# To do: read and analyze the data here
# Read the file object with the reader function. 
    file_reader = csv.reader(election_data)

# Read the header row
    headers = next(file_reader)

# Print each row in the CSV file. 
    for row in file_reader:

# Count the votes
        total_votes += 1

# Print the name from each row
        candidate_name = row [2]

# Search for unique candidate names
        if candidate_name not in candidate_options:

# Add Candidate Name to Candidate Options List
            candidate_options.append(candidate_name)

# Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

# Track votes for candidates
        candidate_votes[candidate_name] += 1

# Save the results to our text file. 
with open(file_to_save, "w") as txt_file:

   # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    # Save the final vote count to the text file.
    txt_file.write(election_results)

    # Print candidates votes
    #print(candidate_votes)

    # Iterate through the candidates
    for candidate_name in candidate_votes:

    # Retrieve the votes of the candidate from the dictionary
        votes = candidate_votes[candidate_name]

    # Calculate the percentage of the vote count
        vote_percentage = float(votes) / float(total_votes) * 100

    # Print each candidate and the percentage of votes using f-string formatting
        candidate_results = f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n"

    # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)

    #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # 1. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


    #  To do: print out the winning candidate, vote count and percentage to

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    
    # Save the winning candidate's name to the text file.
    txt_file.write(winning_candidate_summary)