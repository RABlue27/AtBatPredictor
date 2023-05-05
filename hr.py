import pandas as pd
import matplotlib.pyplot as plt
from pybaseball import statcast

# Fetch the data using statcast function
data = statcast(start_dt='2022-01-01', end_dt='2022-12-31')
print(data)

# Calculate HR/FB for each player
data['hr_per_fb'] = data['hr'] / data['fly_ball']

# Calculate the league HR/FB rate
league_hr_per_fb = data['hr_per_fb'].mean()

# Create a new DataFrame with year and league HR/FB rate
df = pd.DataFrame({'Year': range(2003, 2023),
                   'HR/FB': [league_hr_per_fb]*20})

# Plot the chart
plt.plot(df['Year'], df['HR/FB'])
plt.title('League HR/FB Rate from 2003 to 2022')
plt.xlabel('Year')
plt.ylabel('HR/FB Rate')
plt.show()
