# import the necessary package
from pybaseball import statcast_batter, statcast_pitcher

# define a class StatcastBatter
class StatcastBatter:
    
    # define the constructor method with the required parameters
    def __init__(self, start, end, playerID):
        self.start = start
        self.end = end
        self.playerID = playerID
        
    # define a method to retrieve the stats and return them
    def get_stats(self):
        stats = statcast_batter(self.start, self.end, self.playerID)
        selected_stats = stats[['iso_value', 'babip_value', 'woba_value']]
        mean = selected_stats.mean()
        return mean.to_numpy()
    
    

class StatcastPitcher:
    
    # define the constructor method with the required parameters
    def __init__(self, start, end, playerID):
        self.start = start
        self.end = end
        self.playerID = playerID
        
    # define a method to retrieve the stats and return them
    def get_stats(self):
        stats = statcast_pitcher(self.start, self.end, self.playerID)
        selected_stats = stats[['iso_value', 'babip_value', 'woba_value']]
        mean = selected_stats.mean()
        return mean.to_numpy()
    
