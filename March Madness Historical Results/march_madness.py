import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.dates as mdates

# https://data.world/sports/ncaa-mens-march-madness
file_path = 'sports-ncaa-mens-march-madness/data/ncaa_mens_march_madness_historical_results.csv'
df = pd.read_csv(file_path, delimiter=",", index_col=None, encoding = "ISO-8859-1") # engine='python', encoding='utf-8'
wins_df = df[df['winner']=='Illinois']
losses_df = df[df['loser']=='Illinois']
print(wins_df.index.size)
print(losses_df.index.size)
print(wins_df.head())
list_of_datetimes = pd.to_datetime(wins_df['date'])
dates = mdates.date2num(list_of_datetimes)
values = wins_df['round']
years = mdates.YearLocator()
fig, ax = plt.subplots(1,1)
ax.xaxis.set_major_locator(years)
plt.plot_date(dates, values) #linestyle='solid'
rotation='vertical'
plt.title('University of Illinois NCAA History')
wins_df.to_csv('illini.csv')
#matplotlib.pyplot.show
