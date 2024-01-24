# Bikeshare

Bikeshare is a simple script that analyzes the Bikeshare dataset and displays valuable statistics.

## Dependencies

This project has the following requirements:
* Python 3.6 or higher
* Pandas
* Bikeshare dataset (see the dataset section)

## Installation

Clone the GitHub repository and execute the main script:

```
$ git clone https://github.com/haggag/pdsnd_github.git
$ cd pdsnd_github
$ python ./bikeshare.py
```

## Usage

The Bikeshare program works by executing the `bikeshare.py` script. It then interactively asks the user for the required filters. Finally, the statistics are computed and displayed on the terminal.

## Statistics Computed

The following descriptive statistics are displayed:

1. Popular times of travel (i.e., occurs most often at the start time)
    * Most common month.
    * Most common day of the week.
    * Most common hour of the day.
2. Popular stations and trip
    * Most common start station.
    * Most common end station.
    * Most common trip from start to end (i.e., most frequent combination of start and end stations).
3. Trip duration
    * Total travel time.
    * Average travel time.
4. User info
    * Counts of each user type.
    * Counts of each gender (only available for NYC and Chicago).
    * Earliest, most recent, most common birth year (only available for NYC and Chicago).

## License 

The Bikeshare program is distributed under the MIT license.
