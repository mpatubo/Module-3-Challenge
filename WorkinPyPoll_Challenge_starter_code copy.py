# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources","election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
print("file that's loading:")
print(file_to_load)
# Initialize a total vote counter.
total_votes = 0
print("initial vote count:")
print(total_votes)

# Candidate Options and candidate votes.
county_options = []
county_votes = {}




# Track the winning candidate, vote count and percentage
highest_county = ""
highest_count = 0
highest_percentage = 0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the county name from each row.
        county_name = row[1]


        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if county_name not in county_options:

            # Add the candidate name to the candidate list.
            county_options.append(county_name)

            # And begin tracking that candidate's voter count.
            county_votes[county_name] = 0

        # Add a vote to that candidate's count
        county_votes[county_name] += 1


# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")


    txt_file.write(election_results)



    # Save the final candidate vote count to the text file.
    for county_name in county_votes:

        # Retrieve vote count and percentage
        votes = county_votes.get(county_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results = (
            f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > highest_count) and (vote_percentage > highest_percentage):
            highest_count = votes
            highest_county = county_name
            highest_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    highest_county_summary = (
        f"-------------------------\n"
        f"Highest Vote Count: {highest_county}\n"
        f"Highest Vote Count: {highest_count:,}\n"
        f"Highest Percentage: {highest_percentage:.1f}%\n"
        f"-------------------------\n")
    print(highest_county_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(highest_county_summary)
