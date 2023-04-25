from pybaseball import statcast
from pybaseball import schedule_and_record
from pybaseball import cache 
import pandas as pd



# Statcast data only goes back to 2015. Remove the advanced (launch_speed, launch_angle, spin_rate, etc if you want to train longer)
# https://pypi.org/project/pybaseball/

cache.enable()

sc = statcast(start_dt="2015-01-01", end_dt="2023-04-18")
sc = sc.loc[:, ["batter", "pitcher", "events", "home_team"]]

#Type, date, batter id, pitcher ID, hit type (HR, BB, etc), batter stance, inning number, pitch nummber, pitcher handidness, home, away,
#launch speed off bat, launch angle vertical, X coord of hit, Y coord of hit, pitch speed based off extension, spin rate of ball
sc = sc[sc["events"].notnull()]

print(len(sc))

sc.to_csv("veryShort.csv", index=False)
