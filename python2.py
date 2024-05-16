from matplotlib import pyplot as plt
import seaborn as sb
df = sb.load_dataset('tips')
sb.set(style='whitegrid')
# Boxplot
sb.boxplot(data = df, x = 'day', y = 'tip')
import pandas as pd

# Replace 'C:/Users/USER/Desktop/athlete_events.csv' with the actual absolute path to your file
athlete_events = pd.read_csv(r'C:\Users\USER\Desktop\athlete_events.csv')

# Now you can work with the DataFrame 'athlete_events'
print(athlete_events.head())  # Display the first few rows of the DataFrame
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
selected_sports = ["Basketball", "Gymnastics", "Swimming", "Athletics", "Boxing", "Wrestling"]
sport_age = athlete_events[(athlete_events['Year'] >= 1960) & (athlete_events['Year'] <= 2000) & athlete_events['Sport'].isin(selected_sports)]

sport_age['Year'] = pd.to_numeric(sport_age['Year'])
sport_age['Age'] = pd.to_numeric(sport_age['Age'], errors='coerce')

sport_medians = sport_age.groupby('Sport')['Age'].median().sort_values().index

plt.figure(figsize=(12, 8))
sns.boxplot(data=sport_age, x='Sport', y='Age', order=sport_medians, palette='dark') # Changed palette to 'deep'
plt.xticks(ha='center', fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Sport', fontsize=14)
plt.ylabel('Age', fontsize=14)
plt.title('Distribution of Age by Sport (1960-2000)', fontsize=16)

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# Assuming you have loaded the dataset into a pandas DataFrame named athlete_events

filtered_dat = athlete_events[athlete_events['Year'] >= 1990]
filtered_dat = filtered_dat[['Year', 'Season', 'Sport']].drop_duplicates()

# Counting the number of sports participated by year and season
sports_count = filtered_dat.groupby(['Year', 'Season']).size().reset_index(name='count')

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Plotting for Summer season
summer_data = sports_count[sports_count['Season'] == 'Summer']
axs[0].bar(summer_data['Year'], summer_data['count'], color='#FFA500', alpha=0.7)
axs[0].set_xlabel('Year')
axs[0].set_ylabel('Number of Sports')
axs[0].set_title('Number of Sports Participated in Summer Season')
axs[0].grid(True, linestyle='--', alpha=0.7)

# Adding text labels for Summer
for i, count in enumerate(summer_data['count']):
    axs[0].text(summer_data['Year'].iloc[i], count, str(count), ha='center', va='bottom')

# Plotting for Winter season
winter_data = sports_count[sports_count['Season'] == 'Winter']
axs[1].bar(winter_data['Year'], winter_data['count'], color='#4682B4', alpha=0.7)
axs[1].set_xlabel('Year')
axs[1].set_ylabel('Number of Sports')
axs[1].set_title('Number of Sports Participated in Winter Season')
axs[1].grid(True, linestyle='--', alpha=0.7)

# Adding text labels for Winter
for i, count in enumerate(winter_data['count']):
    axs[1].text(winter_data['Year'].iloc[i], count, str(count), ha='center', va='bottom')

plt.tight_layout()
plt.show()