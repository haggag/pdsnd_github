import time
import calendar
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6}
DAYS = {'Sunday', 'Monday', 'Tuesday', 'Wedensday', 'Thursday', 'Friday', 'Saturday'}
PAGE_LENGTH = 5

def get_filters():
    """Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city. Keep trying until one of the values (chicago, new york city, or washington) is chosen.
    valid_cities = ('chicago', 'new york city', 'washington')
    while True:
        city = input('\nWhat city are you interested in? Enter "Chicago",'
                     ' "New York City", or "Washington".\n')
        city = city.strip().lower()
        if city in valid_cities:
            break

    # Get user input for month. Keep trying until one of the values (all, january, february, ... , june) is chosen.
    while True:
        month = input('\nWhat month are you interested in? Enter month name'
                      ' from the set [January to June] or "all" to apply no'
                      ' month filter.\n')
        month = month.strip().lower()
        if month == 'all' or month in MONTHS:
            break


    # Get user input for day of week. Keep trying until one of the values (all, monday, tuesday, ... sunday) is chosen.
    while True:
        day = input('\nWhat day are you interested in? Enter day name from'
                    ' the set [Monday to Saturday] or "all" to apply no day'
                    ' filter.\n')
        day = day.strip().title()
        if day == 'All' or day in DAYS:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load the dataset for the specified city.
    df = pd.read_csv(CITY_DATA[city])

    # Drop first column, it's some unamed column which is not required.
    df = df.drop(df.columns[0], axis=1)

    # Create month and day_of_week columns.
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month.
    if month in MONTHS:
        df = df[df['month'] == MONTHS[month]]

    # Filter by day of week.
    if day in DAYS:
        df = df[df['day_of_week'] == day]

    return df


def monthnum_to_name(month_num):
    """Converts month number (1, 2, ..., 12) to month name (Ex. January, Feberuary, ..., December).

    Args:
        (int) month_num - number of the month to convert
    Returns:
        (str) month name
    """

    return calendar.month_name[month_num]


def time_stats(df):
    """Displays statistics on the most frequent times of travel.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing loaded trip data.
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    print('\nThe most common month is:', monthnum_to_name(df['month'].mode()[0]))
    print('The most common day of week is:', df['day_of_week'].mode()[0])

    start_hours = df['Start Time'].dt.hour
    print('The most common start hour is:', start_hours.mode()[0])

    print_benchmark(start_time)


def station_stats(df):
    """Displays statistics on the most popular stations and trip.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing loaded trip data.
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    print('Most commonly used start station is:', df['Start Station'].mode()[0])
    print('Most commonly used end station is:', df['End Station'].mode()[0])

    # Display most frequent combination of start station and end station trip.
    start_end = df['Start Station'] + '+' + df['End Station']
    stations = start_end.mode()[0].split('+')
    print('Most requent combination of start station and end station trip is:',
          stations[0], 'AND', stations[1])

    print_benchmark(start_time)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration.

    Args:
        (DataFrame) df - Pandas DataFrame containing loaded trip data.
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    print('Total travel time:', round(df['Trip Duration'].sum()), 'seconds')
    print('Mean travel time:', round(df['Trip Duration'].mean()), 'seconds')

    print_benchmark(start_time)


def user_stats(df):
    """Displays statistics on bikeshare users.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing loaded trip data.
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types.
    user_types = df['User Type'].value_counts()
    print('\nCounts by', user_types.to_string())


    # Display counts of gender.
    if 'Gender' in df:
        genders = df['Gender'].value_counts()
        print('\nCounts by', genders.to_string())

    # Display earliest, most recent, and most common year of birth.
    if 'Birth Year' in df:
        min_year = df['Birth Year'].min()
        max_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()[0]

        print('\nEarliest Birth Year:', int(min_year))
        print('Most Recent Birth Year:', int(max_year))
        print('Most Common Birth Year:', int(common_year))

    print_benchmark(start_time)


def print_data(df, start, count=5):
    """Displays 5 lines of data if the user specifies that they would like to.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing loaded trip data.
        (int) start - offset of the first row to display.
        (int) count - number of rows to display.
    Returns:
        (bool) eof - True if the end of the dataframe is reached, False otherwise.
    """

    df_page = df[start:start+count]
    print(df_page.to_string())

    eof = df_page.shape[0] < count

    return eof


def print_benchmark(start_time):
    """Prints the elapsed time in seconds since the given timestamp.

    Args:
        (float) start_time - time when the function started executing.
    """

    print(f'\nThis took {time.time() - start_time} seconds.')
    print('-'*40)



def main():
    """Main function of the program."""

    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df.empty:
            print('\nNo data found for the specified query! Please try again.\n')
        else:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            show_data = input(f'\nWould you like to see {PAGE_LENGTH} lines'
                              ' of raw data? Enter yes or no.\n')
            start = 0
            while True:
                if show_data.lower() == 'no':
                    break

                if show_data.lower() == 'yes':
                    end_reached = print_data(df, start, PAGE_LENGTH)
                    if end_reached:
                        break

                show_data = input('\nWould you like to see the next'
                                  ' {PAGE_LENGTH} lines of raw data? Enter yes or no.\n')
                start += PAGE_LENGTH

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
