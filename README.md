

# Election Analysis

## Project Overview
Colorado Board of Elections employees, Tom and Seth, have given me the following tasks to complete as an audit of a recent local congressional election: 

1. The total number of votes cast
2. The complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote
6. The total number of votes and percentage of vote per county
7. The largest county participating

In addition to this Analysis (README.md - Deliverable 3), there were two other deliverables: 

1. Printing the results of the election to the terminal https://github.com/jmmadson/Election_Analysis/blob/main/Resources/Deliverable1_TerminalOutput.png
2. Writing the election results to a separate txt file https://github.com/jmmadson/Election_Analysis/blob/main/analysis/election_analysis.txt

## Resources
To complete the analysis, I used the following resources: 
* Data Source: election_results.csv which contained the Ballot ID, County and Candidate Names for three counties in Colorado
* Software: Python 3.6.1 and Visual Studio Code 1.38.1: I used these software resources to extract, calculate and present my analysis results. 

## Election Audit Results: 
The analysis of the election shows that: 

* There were 369,711 votes total
* There were three candidates in this election: 
	* Charles Casper Stockham
	* Diana DeGette
	* Raymon Anthony Doane

To get the list of candidates, we iterated over all of the rows in the CSV file to find the unique candidates in this race. The code below shows how we isolated them and kept count of their votes.

![Candidate Iteration](https://github.com/jmmadson/Election_Analysis/blob/main/Resources/Iterate_Candidates.png)

* The candidate results were:
	* Charles Casper Stockham received 23.0% of the vote with 85,214 votes. 
	* Diana DeGette received 73.8% of the vote with 272,892 votes.
	* Raymon Anthony Doane received 3.1% of the vote with 11,606 votes. 
* The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 votes.

To calculate the winner, we wrote an if statement to determine which candidate had the most votes and highest percentage of votes, making them the winner. The following code snippet shows that in action. 

![Winner Calculation](https://github.com/jmmadson/Election_Analysis/blob/main/Resources/Determine_Winner.png)

* The county results were: 
	* Jefferson County had 23.0% of the vote with 85,213 votes
	* Denver County had 82.8% of the vote with 306,055 votes
	* Arapahoe County had 6.7% of the vote with 11,606 votes

To calculate the percentages per county, similar to how we calculated percentages per candidate, we took the total county votes, divided by the total number of votes and multiplied it by 100 to get the percent, as demonstrated in the code screenshot below. 

![County Calculation](https://github.com/jmmadson/Election_Analysis/blob/main/Resources/county_calculation.png)

* The county with the most votes was Denver county. 

## Election Audit Summary: 

We have written this Python Script to create an efficient, effective method to audit election results. By utilizing this script, we were able to read, calculate and present the information needed for over 369,000 votes, in a matter of seconds. Using a script like this would help make election audits faster and more accurate. A few simple modifications would be required to repurpose this script for any type of election. 

### National Election Script Adaptation
For a National Election, such as a Presidential Election, this script could be modified by updating the data file and changing the county specific information to state specific information. First, a new data set would need to be provided and the file that we are looking at, swapped out. The local election results file "election_results.csv" in this current election, would be modified to the new data file name. The screenshot below shows where we would change that. 

![File Change](https://github.com/jmmadson/Election_Analysis/blob/main/Resources/File_Change.png)

Additionally to adapt this script for a National Election, we'd want to change county information to state information. The screenshots below reference the places in the script where county could be changed to state. We would need to modify the list and dictionary we created, as well as the variables we set specifically for the county. The calculations would be the same, but instead of using and analyzing counties, we'd be analyzing states. 

![County Changes](https://github.com/jmmadson/Election_Analysis/blob/main/Resources/county_references.png)

### Mayoral or Other Local Election Script Adaptation
For an even more local election, such as a mayoral race in a city, the script could be modified to report just the results for the race in the city. As with the National Election mentioned above, or any other election, we'd need to modify the data file in our script to pull from the new data file. In addition, we could remove all of the variables, lists, and references to county as for a local election in a single city, we'd need a simpler script just to tally the total number of votes, candidates, and their votes & percentages of votes received to determine the winner. 

### Additional Adaptation
These modifications, while small, make this script a versitle tool for quickly analyzing any type of election. Additional modifications could be made based on what information is important in an election, such as tracking Democratic or Republican party votes or District specific voting results as examples. Provided that information is available in the data file, the opportunities for repurposing this script are open ended. 
