import pandas as pd
from pybaseball import schedule_and_record
import calendar
import datetime

data = pd.read_csv("test_csv.csv")
data['game_date'] = pd.to_datetime(data['game_date'])

def month_to_short(month):
    
    # Parse the month string and extract the month number
    month = datetime.datetime.strptime(month, "%B").month
    
    # Create a datetime object for the first day of the month
    date = datetime.date(2023, month, 1)
    
    # Use strftime to format the month as a three-letter abbreviation
    month_abr = date.strftime("%b")
    
    # Return the abbreviation
    return month_abr

counter = 0
schedule_cache = {}
length = len(data)

for i, row in data.iterrows():

    game_date = row["game_date"]
    home_team = row["home_team"]
    
    # Map team abbreviations to full names
    if home_team == "CWS":
        home_team = "CHW"
    if home_team == "AZ":
        home_team = "ARI"
    if home_team == "WSH":
        home_team = "WSN"
        
    year = game_date.year
    month = month_to_short(calendar.month_name[game_date.month])
    day = game_date.day
    
    # Check if we already have the schedule and record for this team and year
    if (home_team, year) not in schedule_cache:
        schedule_cache[(home_team, year)] = schedule_and_record(year, home_team)
    
    # Get the schedule and record for this team and year
    d = schedule_cache[(home_team, year)]
    
    dm = month + " " + str(day)
    
    # Filter the schedule and record for the specified date
    d = d.loc[d.Date.str.contains(dm), :]
    
    # Get the value of the "D/N" column from the first row of `d`
    # Get the value of the "D/N" column from the first row of `d`, or set it to "N" if not found
    try:
        dn_value = d.loc[d.index[0], "D/N"]
    except (KeyError, IndexError):
        dn_value = "N"
    
    # Append the "D/N" value to a new column in the current row of `data`
    data.loc[i, "D/N"] = dn_value

  

data.to_csv("updated_csv.csv", index=False)