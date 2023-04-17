from pybaseball import statcast
from pybaseball import schedule_and_record
import pandas as pd

# game_date = '2023-04-16'
# team_code = 'TOR'
# year = 2023

# # Get the team's schedule and record for the season
# schedule = schedule_and_record(2023, team_code)
# schedule["Date"] = pd.to_datetime(schedule["Date"], format="%A, %b %d").dt.strftime("%m-%d")

sc = statcast(start_dt="2023-04-16", end_dt="2023-04-16")
sc = sc.loc[:, ["pitch_type", "game_date", "batter", "pitcher", "events", "stand",
                "p_throws", "home_team", "away_team", "hit_distance_sc", "launch_speed",
                "launch_angle"]]
sc = sc[sc["events"].notnull()]
sc.to_csv("test_csv.csv", index=False)