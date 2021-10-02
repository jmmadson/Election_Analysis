

# Election_Analysis

## Project Overview
Colorado Board of Elections employees Tom and Seth have given me the following tasks to complete an audit of a recent local congressional election: 

1. The total number of votes cast
2. The complete list of candidates who received votes
3. The percentage of votes each candidate won
4. The total number of votes each candidate won
5. The winner of the election based on popular vote
6. The total number of votes and percentage of vote per county
7. The largest county participating

## Resources
To complete the analysis used the following resources: 
* Data Source: election_results.csv which contained the Ballot ID, County and Candidate name for three counties
* Software: Python 3.6.1 and Visual Studio Code 1.38.1: We used these software resources to extract, calculate and present our analysis results. 

## Election-Audit Results: 
The analysis of the election shows that: 

* There were 369,711 votes total
* There were three candidates: 
	* Charles Casper Stockham
	* Diana DeGette
	* Raymon Anthony Doane

To get the list of candidates, we iterated over all of the rows to find the unique candidates in this race. The code below shows how we isolated them and put them into a list we could reference later. 

* The candidate results were:
	* Charles Casper Stockham received 23.0% of the vote and 85,214 votes. 
	* Diana DeGette received 73.8% of the vote and 272,892 votes.
	* Raymon Anthony Doane received 3.1% of the vote and 11,606 votes. 
* The winner of the election was Diana DeGette who received 73.8% of the vote and 272,892 votes.

To calculate the winner, we wrote an if statement to determine which candidate had the most votes and highest percentage of votes, making them the winner. The code below shows how we did that. 

* The county results were: 
	* Jefferson County: 23.0% of the vote with 85,213 votes
	* Denver County: 82.8% of the vote with 306,055 votes
	* Arapahoe County: 6.7% of the vote with 11,606 votes

To calculate the percentages per county, similar to how we calculated percentages per candidate, we took the total county votes, divided by the total number of votes and multiplied it by 100 to get the percent, as demonstrated in the code screenshot below. 

* The county with the most votes was Denver county. 

## Election-Audit Summary: 

We have written this Python Script to create an efficient, effective method to audit election results. By utilizing this script, we were able to read, calculate and present the information needed for over 369,000 votes, in a matter of seconds. Using a script like this would help make election audits faster and more accurate. A few simple modifications would be required to repurpose this script for any type of election. 

### National Election Script Adaptation
For a National Election, such as a presidential election, this script could be modified by changing the county specific information to state specific information. First, a new data set would need to be provided and the file that we are looking at, swapped out. The local election results "election_results.csv" in this current election, would be modified to the new data file name. See the screenshot below where we would change that. 

Additionally to adapt this script for a National Election, we'd want to change county information to stat information. The screenshots below reference the places in the script where county could be changed to state. We would need to modify the list and dictionary we created, as well as the variables we set specifically for the county. The calculations would be the same, but instead of using and analyzing counties, we'd be analyzing states. 

### Mayoral or Other Local Election Script Adaptation
For an even more local election, such as a mayoral race in a city, the script could be modified to report just the results for the race in the city. As with the National Election mentioned above, or any other election, we'd need to modify the data file in our script to pull from the new data file. In addition, we could remove all of the variables, lists, and references to county as for a local election in a single city, we'd need a simpler script just to tally the total number of votes, candidates, and their votes & percentages of votes received to determine the winner. 
