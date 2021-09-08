import time
import pandas as pd
import numpy as np

# bikeshare.py sample code and udacity quiz answers were used to help create the code in this file.

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }

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
    user_input = True
    while user_input == True:
        city = input('Enter the city you would like to examine (chicago, new york city, washington) ').title()
        if city == "Chicago" or city == 'New York City' or city == 'Washington':
            user_input = False
        else:
            print('That\'s not a valid city, please try again')


    # TO DO: get user input for month (all, january, february, ... , june)
    user_input = True
    while user_input == True:
        month = input('Enter the month you would like to examine (January, February, March, April, May, June or All for all available, 3 letter months also work) ').title()
        if month == 'January' or month == 'February' or month == 'March' or month == 'April' or month == 'May' or month == 'June' or  month == 'Jan' or month == 'Feb' or month == 'Mar' or month == 'Apr' or month == 'May' or month == 'Jun' or month == 'All':
            user_input = False
        else:
            print('That\'s not a valid month, please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    user_input = True
    while user_input == True:
        day = input('Enter the day of the week you would like to examine (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all for all days) ').title()
        if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday' or day == 'Sunday' or day == 'Mon' or day == 'Tues' or day == 'Wed' or day == 'Thurs' or day == 'Fri' or day == 'Sat' or day == 'Sun' or day == 'All':
            user_input = False
        else:
            print('That\'s not a valid day of the week, please try again')

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
    if month != 'All':
        # use the index of the months list to get the corresponding int
        if len(month) == 3:
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
            month = months.index(month) + 1
        else:
            months = ['January', 'February', 'March', 'April', 'May', 'June']
            month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        if len(day) < 6:
            days = {'Mon': 'Monday', 'Tues': 'Tuesday', 'Wed': 'Wednesday', 'Thurs': 'Thursday', 'Fri': 'Friday', 'Sat': 'Saturday', 'Sun': 'Sunday'}
            day = days[day]
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel.

    Args: df - dataframe"""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0] #median()
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('The most popular month was {}'.format(months[popular_month-1]))
    # TO DO: display the most common day of week
    popular_week = df['day_of_week'].mode()[0] #median()
    print('The most popular day of the week was {}'.format(popular_week))
    # TO DO: display the most common start hour
    df['Start Time'] = df['Start Time'].astype('datetime64[ns]')

    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

    # find the most common hour (from 0 to 23)
    popular_hour = df['hour'].median()
    am_pm = 'am'
    am_pm_time = 12
    #format it into am/pm time
    if popular_hour > 12:
        am_pm = 'pm'
        am_pm_time = popular_hour - 12
    elif popular_hour == 0:
        am_pm_time = 12
    else:
        am_pm_time = popular_hour

    print('The most popular hour of the day was {:0.0f} hours or {:0.0f}{}'.format(popular_hour, am_pm_time, am_pm))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.

    Args: df - dataframe"""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_station_start = df['Start Station'].mode()[0] #median()
    print('The most popular start station was {}'.format(popular_station_start))
    # TO DO: display most commonly used end station
    popular_station_end = df['End Station'].mode()[0] #median()
    print('The most popular end station was {}'.format(popular_station_end))

    # TO DO: display most frequent combination of start station and end station trip
    popular_station_combo = (df['Start Station']+' end at '+df['End Station']).mode()[0] #median()
    print('The most popular combination of stations was start at {}'.format(popular_station_combo))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args: df - dataframe"""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = (df['Trip Duration']).sum() #median()
    total_time_mins = total_time//60
    total_time_hours = 0
    #separate into hours, minutes and seconds
    if total_time_mins >=60:
        total_time_hours = total_time_mins//60
        total_time_mins = total_time_mins%60
    total_time_secs = total_time%60
    print('The total user travel time for the period selected was {} seconds or {} hours, {} minutes and {} seconds'.format(total_time, total_time_hours, total_time_mins, total_time_secs))

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    mean_time_mins = mean_travel_time//60
    mean_time_hours = 0
    #separate into hours, minutes and seconds
    if mean_time_mins >=60:
        mean_time_hours = mean_time_mins//60
        mean_time_mins = mean_time_mins%60
    mean_time_secs = mean_travel_time%60
    print('The mean travel time was {:0.2f} seconds or {} hours, {:0.0f} minutes and {:0.0f} seconds'.format(mean_travel_time, mean_time_hours, mean_time_mins, mean_time_secs))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.

    Args: df - dataframe"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        user_type = pd.DataFrame((df['User Type']).value_counts()) #median()
        print('The count per user type is: \n{}'.format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = pd.DataFrame((df['Gender']).value_counts()) #median()
        print('The count per gender is: \n{}'.format(gender))


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year_min = df['Birth Year'].min()
        birth_year_max = df['Birth Year'].max()
        birth_year_mode = df['Birth Year'].mode()[0]
        print('The earliest birth year was {:0.0f}, the most recent birth year was {:0.0f} and the most commonth birth year was {:0.0f}'.format(birth_year_min, birth_year_max, birth_year_mode))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data_display(df):
    """Displays the raw data on bikeshare users.

    Args: df - dataframe"""
    start_row = 0
    end_row = 5
    while True:
        df_five = df[start_row:end_row]
        print(df_five)
        raw_data = input('\nWould you like to see more of the raw data? Enter yes or no (Y/N).\n')
        if raw_data.lower() != 'y' and raw_data.lower() != 'yes' :
            break
        else:
            start_row = end_row
            end_row += 5

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        raw_data = input('\nWould you like to see the raw data? Enter yes or no (Y/N).\n')
        if raw_data.lower() == 'y' or raw_data.lower() == 'yes':
            if len(df.index)>0:
                raw_data_display(df)

        restart = input('\nWould you like to restart? Enter yes or no (Y/N).\n')
        if restart.lower() != 'y' and restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
