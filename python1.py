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
