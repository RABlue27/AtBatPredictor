from pybaseball import statcast
from pybaseball import schedule_and_record
from pybaseball import cache 
import pandas as pd



# Statcast data only goes back to 2015. Remove the advanced (launch_speed, launch_angle, spin_rate, etc if you want to train longer)
# https://pypi.org/project/pybaseball/

# cache.enable()

sc = statcast(start_dt="2015-01-01", end_dt="2023-04-18")
sc = sc.loc[:, ["pitch_type", "game_date", "batter", "pitcher", "events", "stand", "inning", "pitch_number", 
                "p_throws", "home_team", "away_team", "launch_speed", "launch_angle","effective_speed", "release_spin_rate"]]

# "hit_distance_sc", "launch_speed",E
                # "launch_angle",
sc = sc[sc["events"].notnull()]

print(len(sc))

sc.to_csv("test_csv.csv", index=False)
