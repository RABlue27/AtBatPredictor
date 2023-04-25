# import the classes from the other file
from playerStats import StatcastBatter, StatcastPitcher

from pybaseball import cache

cache.disable()


# create an instance of the StatcastBatter class with the required parameters
batter_stats = StatcastBatter('2014-01-01', '2014-12-12', 545361)

# call the get_stats() method to retrieve the batter stats
batter_data = batter_stats.get_stats()

# create an instance of the StatcastPitcher class with the required parameters
pitcher_stats = StatcastPitcher('2017-01-01', '2017-12-12', 477132)

# call the get_stats() method to retrieve the pitcher stats
pitcher_data = pitcher_stats.get_stats()

# # print the stats
print("Batter Stats:")
print(batter_data)
print("\nPitcher Stats:")
print(pitcher_data)
