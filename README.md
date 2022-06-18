# Project Overview
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics. The experience is interactive because depending on a user's input, the answers to the questions on the previous page will change! There are four questions that will change the answers:

1. Would you like to see data for Chicago, New York, or Washington?
2. Would you like to filter the data by month, day, or not at all?
3. (If they chose month) Which month - January, February, March, April, May, or June?
4. (If they chose day) Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?

The answers to the questions above determines the city and timeframe on which data analysis is done. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

# Statistics Computed
The code provides the following information:

1. Popular times of travel (i.e., occurs most often in the start time)  
most common month  
most common day of week  
most common hour of day  

2. Popular stations and trip  
most common start station  
most common end station  
most common trip from start to end (i.e., most frequent combination of start station and end station)  

3. Trip duration  
total travel time  
average travel time  

4. User info  
counts of each user type  
counts of each gender (only available for NYC and Chicago)  
earliest, most recent, most common year of birth (only available for NYC and Chicago)  
