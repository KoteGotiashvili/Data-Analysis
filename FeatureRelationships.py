from DataUnderstanding import DataUnderstanding
import matplotlib.pyplot as plt
import re
import pandas as pd
import seaborn as sns

def extract_numeric(value):
    if isinstance(value, str):
        match = re.search(r'\d+(\.\d+)?', value.replace(',', ''))
        if match:
            return float(match.group())
    return float('nan')

df = DataUnderstanding.load_data('./data/coaster_db.csv')
df['Speed'] = df['Speed'].apply(extract_numeric)
df['Height'] = df['Height'].apply(extract_numeric)
# Drop rows with NaN values in 'Speed' or 'Height'
df = df.dropna(subset=['Speed', 'Height'])
# Plot scatter plot
plt.scatter(x=df['Speed'], y=df['Height'])
plt.xlabel('Speed')
plt.ylabel('Height')
plt.title('Speed vs. Height of Coasters')
# plt.show()


ax = sns.scatterplot(x='Speed',
                y='Height',
                hue='Speed',
                data=df)
ax.set_title('Coaster Speed vs. Height')
plt.show()

