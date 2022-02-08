import time
import pandas as pd
import numpy as np
import datetime


MONTH_DATA ={'JANUARY':1,'FEBRUARY':2,'MARCH':3,'APRIL':4,'MAY':5,'JUNE':6,'JULY':7,'AUGUST':8,'SEPTEMBER':9,'OCTOBER':10,'NOVEMBER':11,'DECEMBER':12,'ALL': -1}

CITY_DATA = { 'CHICAGO': 'chicago.csv',
              'NEW YORK CITY': 'new_york_city.csv',
              'WASHINGTON': 'washington.csv' }

DAY_DATA ={'MONDAY':1,'TUESDAY':2,'WEDNESDAY':3,'THURSDAY':4,'FRIDAY':5,'SATURDAY':6,'SUNDAY':0,'ALL':-1}



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
    print("Enter the name of the city --> chicago  ,new york city ,washington")
    while(True):
        city=input().upper()
        if city not in CITY_DATA:
            print("Incorrect Input------------- Please enter any of the :chicago , new york city ,washington")
        else:
            break
            
            
    print("Enter name of the month all, january, february, march, april,may, june, july, august, september, october, november, december")        
    while(True):
        month=input().upper()
        if month in MONTH_DATA:
            break 
        else:
            print("Incorrect input----------- Please enter any of the  :all, january, february, march, april, may, june, july, august, september, october, november, december")
            
    print("Enter name of the day of week all, monday, tuesday, wednesday, thursday, friday, saturday, sunday :")        
    while(True):
        day=input().upper()
        if day in DAY_DATA:
            break 
        else:
            print("Incorrect input:-Please enter any of the : all, monday, tuesday, wednesday, thursday, friday, saturday, sunday ")
            
                  

    # TO DO: get user input for month (all, january, february, ... , june)


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    if month!="ALL":
        df=df.loc[(pd.DatetimeIndex(df['Start Time']).month ==MONTH_DATA[month])]
    if day!="ALL":
        df= df.loc[(pd.DatetimeIndex(df['Start Time']).day == DAY_DATA[day])]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month_count_map={}
    max_month=""
    max_month_count=0              
    for ind in df.index:
        date=datetime.datetime.strptime(df['Start Time'][ind], "%Y-%m-%d %H:%M:%S")
        i=date.strftime("%B")  
        if i in month_count_map:
            month_count_map[i]+=1
            if(max_month_count<month_count_map[i]):      
                max_month=i
                max_month_count=month_count_map[i]
                  
        else:
             month_count_map[i]=1
                  
    print("The Most frequent Month is "+max_month)
    
    # TO DO: display the most common day of week
    day_count_map={}
    max_day=""
    max_day_count=0              
    for ind in df.index:
        date=datetime.datetime.strptime(df['Start Time'][ind],"%Y-%m-%d %H:%M:%S")
        i=date.strftime("%A")  
        if i in day_count_map:
            day_count_map[i]+=1
            if(max_day_count<day_count_map[i]):      
                max_day=i
                max_day_count=day_count_map[i]
                  
        else:
             day_count_map[i]=1
    
    print("The Most frequent day is "+max_day)
    # TO DO: display the most common start hour(00-23)
                  
    hour_count_map={}
    max_hour=""
    max_hour_count=0              
    for ind in df.index:
        date=datetime.datetime.strptime(df['Start Time'][ind],"%Y-%m-%d %H:%M:%S")
        i=date.strftime("%H")
        if i in hour_count_map:
            hour_count_map[i]+=1
            if(max_hour_count<hour_count_map[i]):      
                max_hour=i
                max_hour_count=hour_count_map[i]
                  
        else:
             hour_count_map[i]=1
    
    print("The Most Frequent start hour is "+max_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    startStation_count_map={}
    max_startStation=""
    max_startStation_count=0              
    for ind in df.index:
        i=df['Start Station'][ind]
        if i in startStation_count_map:
            startStation_count_map[i]+=1
            if(max_startStation_count<startStation_count_map[i]):      
                max_startStation=i
                max_startStation_count=startStation_count_map[i]
                  
        else:
             startStation_count_map[i]=1
    
    print("The Most Frequent start station is "+max_startStation)
    
    # TO DO: display most commonly used end station
    endStation_count_map={}
    max_endStation=""
    max_endStation_count=0              
    for ind in df.index:
        i=df['End Station'][ind]
        if i in endStation_count_map:
            endStation_count_map[i]+=1
            if(max_endStation_count<endStation_count_map[i]):      
                max_endStation=i
                max_endStation_count=endStation_count_map[i]
                  
        else:
             endStation_count_map[i]=1
    
    print("The Most Frequent End station is "+max_endStation)
    
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Start_End']=df['Start Station']+"-->"+df['End Station']
    startEndStation_count_map={}
    max_startEndStation=""
    max_startEndStation_count=0              
    for ind in df.index:
        i=df['Start_End'][ind]
        if i in startEndStation_count_map:
            startEndStation_count_map[i]+=1
            if(max_startEndStation_count<startEndStation_count_map[i]):      
                max_startEndStation=i
                max_startEndStation_count=startEndStation_count_map[i]
                  
        else:
             startEndStation_count_map[i]=1
    
    print("The Most Frequent Start-End station is "+max_startEndStation)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    totalTripDuration=df['Trip Duration'].sum()
    print("The total trip duration is "+str(totalTripDuration))

    # TO DO: display mean travel time
    meanTripDuration=df['Trip Duration'].mean()
    print("The mean trip duration time is " +str(meanTripDuration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts=df['User Type'].value_counts()
    print("The counts of the various user type are ")
    print(user_counts)

    # TO DO: Display counts of gender
    try:
        gender_counts=df['Gender'].value_counts()
        print("The counts of  Gender are")
        print(gender_counts)
    except:
        print("The selected city doesn't have any gender information to display")
        

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliestBirthYear=(df['Birth Year'].min())
        recentBirthYear=(df['Birth Year'].max())
        commonBirthYear=df['Birth Year'].value_counts().idxmax()
        print("Earliest birth year is "+str(earliestBirthYear))
        print("Most Recent birth year is "+str(recentBirthYear))
        print("Most frequent birth year is "+str(commonBirthYear))
    except: 
        print("The selected city doesn't have any birth year information to display")
        

  
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def check_input():
    while True:
        response=input().upper()
        if response not in ['YES','NO']:
            print("Incorrect Input-------- Please enter any of - yes or no")
            continue
        else:
            break
    return response         
        
    
def raw_data(df):
    """Displays the raws data."""
    
    print(("Do you like to see the raw data? Enter any of  yes or no.\n"))
    start=0
    end=5
    while True:
        response=check_input()
        if response == "YES" and df.shape[0] >end:
            print(df[start:end:1])
            start=start+5
            end=end+5
            
        elif response == "YES" and df.shape[0] >start:  
            print(df[start::1])
            print("All the available  data has been  displayed. No more data is avaliable to display ")
            return 
        
        if response =="NO":
            return
        print("Do you like to display additional raw data ? Enter any of yes or no.\n")

            
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        if df.empty==True:
            print("The selected city,month, day doesn't have any data avaliable so please select a new  values")
            continue
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
