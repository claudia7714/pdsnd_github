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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Would you like to analyze Chicago, New York City, or Washington? " )
    city = city.lower()
    valid_cities = ['chicago', 'new york city', 'washington']
    while city not in valid_cities:
        city = input("Invalid entry. Please choose between Chicago, New York City, and Washington: " )

    # get user input for month (all, january, february, ... , june)
    month = input("Please enter a month between January and June, or enter 'all': ")
    month = month.lower()
    valid_months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while month not in valid_months:
        month = input("Please enter a month between January and June or enter 'all': ")


    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please enter the day of the week to analyze, or enter 'all': ")
    day = day.lower()
    valid_days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while day not in valid_days:
        day = input("Please enter the day of the week to analyze, or enter 'all': ")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
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
        month = months.index(month)+1
    
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

    # display the most common month
    common_month = df['month'].mode()[0]
    month_dict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June'}
    print("Month: {}".format(month_dict[common_month]))


    # display the most common day of week
    common_week = df['day_of_week'].mode()[0]
    print("Day of Week: {}".format(common_week))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Start Hour: {}".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("Start Station: {}".format(common_start_station))

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("End Station: {}".format(common_end_station))

    # display most frequent combination of start station and end station trip
    df['Station Combinations'] = df['Start Station'] + ' | ' + df['End Station']
    common_station_combo = df['Station Combinations'].mode()[0]
    print("Station Combination: {}".format(common_station_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total Travel Time: {} seconds".format(total_time))


    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Average Travel Time: {} seconds".format(round(mean_time)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)
    print()

    # Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
        print()

        # Display earliest, most recent, and most common year of birth
        earliest_birth = df['Birth Year'].min()
        print("Earliest Birth Year: " + str(int(earliest_birth)))
        
        recent_birth = df['Birth Year'].max()
        print("Most Recent Birth Year: " + str(int(recent_birth)))
        
        common_birth = df['Birth Year'].mode()[0]
        print("Most Common Birth Year: " + str(int(common_birth)))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        df.head().index

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
