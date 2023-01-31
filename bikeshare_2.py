import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

def get_filters():
    
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    Cities = ['chicago', 'new york city', 'washington']
    city = input('Please Enter one of the following cities: Chicago - New York City - Washington    ').lower()
    while city not in Cities:       # get user input for city (chicago, new york city, washington)
        print('Invalid input, try again')
        city = input('Please Enter one of the following cities: Chicago - New York City - Washington    ').lower()
        
    month = input('please choose a month to filter by or "all" for no filter    ').lower()
    while month not in months:      # get user input for month (all, january, february, ... , june)
        print('Invalid input, try again     ')
        month = input('please choose a month to filter by or "all" for no filter').lower()
        
    days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input('please choose a day to filter by or "all" for no filter    ').lower()
    while day not in days:          # get user input for day of week (all, monday, tuesday, ... sunday)
        print('Invalid input, try again     ')
        day = input('please choose a day to filter by or "all" for no filter').lower()
    return city, month, day


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
    
    df['day of week'] = df['Start Time'].dt.day_name()
    
    df['hour'] = df['Start Time'].dt.hour
    
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1   
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day of week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month

    popular_month = df['month'].mode()[0]
    print('most common month: ', popular_month)

    # display the most common day of week

    popular_day = df['day of week'].mode()[0]
    print('most common day: ', popular_day)

    # display the most common start hour

    popular_hour = df['hour'].mode()[0]
    print('most common start hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_com_start = df['Start Station'].value_counts().head(1)
    print('most used start station: ', most_com_start)

    # display most commonly used end station
    most_com_end = df['End Station'].value_counts().head(1)
    print('\nmost used end station: ', most_com_end)

    # display most frequent combination of start station and end station trip
    df['Start and End'] = df['Start Station'] + ' and ' + df['End Station']
    most_freq_combo = df['Start and End'].value_counts().head(1)
    print('\nmost used combonation of start and end stations: ', most_freq_combo)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    trip_total_time = df['Trip Duration'].sum()
    print('trip total travel time in (s): ', trip_total_time) 

    # display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print('\ntrip avg travel time in (s): ', trip_mean) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_type = df['User Type'].value_counts()
    print('\ncount of types:\n', count_user_type)


    # Display counts of gender
    
    if 'Gender' in df.columns:
        count_gender = df['Gender'].value_counts()
        print('gender count is:\n', count_gender)
    else:
        print('no Gender available')
    

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_year = df['Birth Year'].min()
        max_year = df['Birth Year'].max()
        median_year = df['Birth Year'].median()
        print('\nearliest year of birth: ', min_year)
        print('\nmost recent year of birth: ', max_year)
        print('\nmost common year of birth: ', median_year)    
    else:
        print('no Birth Year available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def raw_data(df):

    """""
    This function display raw data upon user's request
    """

    print(' Would you like to to see the 5 rows of raw data ')
    response = input()
    x = 0
    
    while response == 'yes':
        print(df.iloc[x:x+5])
        x += 5
        print('Do you want 5 more?')
        response = input()
        
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Udacity is awesome')
            break


if __name__ == "__main__":
	main()
