import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    monthlist = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    dayslist = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
    name = input('Please provide your name: ')
    city = input('Choose a city (chicago, new york city, washington): ').lower()
    
    while city not in cities:
        city = input('Incorrect input! Choose a city (chicago, new york city, washington): ').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Please choose the month you want to filter by (From Jan. to Jun.) or type \'all\' if you want all months: ' ).lower()
    
    while month not in monthlist:
        month = input('Incorrect input! Please choose the month you want to filter by (From Jan. to Jun.) or type \'all\' if you want all months: ').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Please choose the day you want to filter by or type \'all\' if you want all days: ' ).lower()
    
    while day not in dayslist:
        day = input('Incorrect input! Please choose the day you want to filter by or type \'all\' if you want all days: ').lower()

    print('-'*40)
    return city, month, day, name


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0] # find the most common month
    print('Popular month: ', popular_month) 

    # TO DO: display the most common day
    popular_day = df['day_of_week'].mode()[0] # find the most common day
    print('Popular day: ', popular_day)
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour # extract hour from Start Time to create an hour column
    popular_hour = df['hour'].mode()[0] # find the most common hour
    print('Popular hour: ', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0] # find the most common start station
    print('Popular start station: ', popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0] # find the most common end station
    print('Popular end station: ', popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + "-" + df['End Station'] # create a combination of start station and end station trip
    popular_trip = df['trip'].mode()[0] # find the most common combination
    print('Popular combination: ', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum() # sum all durations
    print('Total travel time: ', total_time)

    # TO DO: display mean travel time
    mean_travel_time= df['Trip Duration'].mean() # calculate mean for all durations
    print('Average travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: ', user_types)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender = df['Gender'].value_counts()
        print('Counts of gender: ', gender)
    
        # TO DO: Display earliest, most recent, and most common year of birth
        earliest_year_of_birth = df['Birth Year'].min() # calculate earliest year of birth
        print('Earliest year of birth: ', earliest_year_of_birth)
    
        most_recent_year_of_birth = df['Birth Year'].max() # calculate most recent year of birth
        print('Most recent year of birth: ', most_recent_year_of_birth)
    
        most_common_year_of_birth = df['Birth Year'].mode() # calculate most common year of birth
        print('Most common year of birth: ', most_common_year_of_birth)
        
        # Display number of users under 18
        today = pd.to_datetime('today') # extract today's date
        year = today.year # extract the current year
        
        df['age'] = year - df['Birth Year'] # calculate the age of each user and create new column
    
        less_than_eighteen = len(df[df['age'] < 18]) # number of users under 18
        print('Users under 18: ', less_than_eighteen)
        
        more_than_eighteen = len(df[df['age'] >= 18]) # number of users above or equal 18
        print('Users above 18: ', more_than_eighteen)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df): # define new function task the user whether he wants to see 5 rows of data
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
    start_loc = 0 # first row of data
    end_loc = 5   # fifth row of data
    
    while view_data != 'no':
        print(df.iloc[start_loc:end_loc]) # show user 5 consecutive rows of data
        start_loc += 5 # adding 5 to the start row
        end_loc += 5   # adding 5 to the end row
        view_display = input('Do you wish to continue?: ').lower()
        if view_display.lower() != 'yes':
            break

def main():
    while True:
        city, month, day, name = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Thanks ' + name + '!')
            break


if __name__ == "__main__":
	main()
