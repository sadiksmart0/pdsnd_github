import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['January', 'February', 'March', 'April', 'May', 'June', \
          'July', 'August', 'September', 'October', 'November', \
          'December', 'All']

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', \
        'Saturday', 'Sunday', 'All']
data_switch = True

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #get user input for city (chicago, new york city, washington)
    city = ""
    while city not in CITY_DATA.keys():
        city_input = input(f"\nWhich city would you like to see?\
        \n Available Cities: Chicago, New york city, Washington \n").lower()
        city = city_input

    #get user input for month (all, january, february, ... , june)
    month = ""
    while month not in months:
        month_input = input("What month would you like to view? all, january...\
                            December \n").title()
        month = month_input
        

    #get user input for day of week (all, monday, tuesday, ... sunday)
    day = ""
    while day not in days:
        day_input = input("What day would you like to view? all, Monday...\
        Sunday\n").title()
        day = day_input
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
    df = pd.read_csv(CITY_DATA[city])
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df['Month'] = df['Start Time'].dt.strftime('%B')      
    df["Day of Week"] = df["Start Time"].dt.weekday_name
    df["Hour"] = df["Start Time"].dt.hour
    df["Year"] = df["Start Time"].dt.year
    
    #Check 
    if month != "All" and day != "All":
        df = df[(df["Month"] == month) & (df["Day of Week"] == day)]
    elif month != "All":
        df = df[df["Month"] == month]
    elif day != "All":
        df = df[df["Day of Week"] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #display the most common Year
    print("most common Year: {}".format(df['Year'].value_counts().idxmax()))
    
    #display the least common Year
    print("least common Year: {}".format(df['Year'].value_counts().idxmin()))

    #display the most common month
    print("most common month: {}".format(df['Month'].value_counts().idxmax()))
    
    #display the least common month
    print("least common month: {}".format(df['Month'].value_counts().idxmin()))

    #display the most common day of week
    print("most common day of week: {}".format(df['Day of Week'].value_counts().idxmax()))
    
    #display the least day of week
    print("least common day of week: {}".format(df['Day of Week'].value_counts().idxmin()))

    #display the most common start hour
    print("most common start hour: {}".format(df['Hour'].value_counts().idxmax()))
    
    #display the least common start hour
    print("least common start hour: {}".format(df['Hour'].value_counts().idxmin()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"\nCommonly Used Start Station: {df['Start Station'].value_counts().idxmax()}")


    # TO DO: display most commonly used end station
    print(f"\nCommonly Used End Station: {df['End Station'].value_counts().idxmax()}")

    # TO DO: display most frequent combination of start station and end station trip
    print(f"\nMost frequent combination of start station and end station \
          trip: {df.groupby(['Start Station', 'End Station']).size().idxmax()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"Total Travel time: {df['Trip Duration'].sum()}")

    # TO DO: display mean travel time
    print(f"Average Travel Time: {df['Trip Duration'].mean()}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    #Display counts of user types
    print(df["User Type"].value_counts())
    
    #Display counts of gender and Birth year
    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        print(f"\n {df['Gender'].value_counts()}")

        #Display earliest, most recent, and most common year of birth
        print(f"\nEarliest Birth Year:{df['Birth Year'].min()} \
              \nRecent Birth Year:{df['Birth Year'].max()} \
              \nMost Common Birth Year:{df['Birth Year'].value_counts().idxmax()}")
    elif 'Gender' in df.columns:
        print(f"\n {df['Gender'].value_counts()}")
    elif 'Birth Year' in df.columns:
        print(f"\nEarliest Birth Year:{df['Birth Year'].min()} \
        \nRecent Birth Year:{df['Birth Year'].max()} \
        \nMost Common Birth Year:{df['Birth Year'].value_counts().idxmax()}")
    else:
        print("\nSome stats cannot be shown because their columns do exist in this DataFrame")
        
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df, data_switch):
    count = 0
    while data_switch:
        data_prompt = input("Would you like to view the data? Yes/No\n").title()
        if data_prompt == "Yes" and count < len(df):
            print(df.iloc[count: count+5])
            count += 5
        elif count >= len(df):
            print("You reached the End of File")
        else:
            data_switch = False
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df, data_switch)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
