from DataPreparation import DataPreparation
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
import numpy as np
dp = DataPreparation()
df = dp.clean_colums()

#understand duplicates
#print("duplicated in years")
year_intro = df['Year_Introduced'].value_counts()
#print(year_intro)

print("bar plot")
def bar_plot_of_data(df):
    """
    Generates a bar plot of the top 10 most frequent values in the 'Year_Introduced' column of the provided DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the 'Year_Introduced' column.

    Returns:
    None
    """
    # Calculate the top 10 value counts
    counts = df['Year_Introduced'].value_counts()

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.bar(counts.index, counts.values, color='skyblue')
    plt.xlabel('Year Introduced')
    plt.ylabel('Counts')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
def hist_plot_of_speed(df):
    """
    Generates a histogram plot of the 'Speed_mph' column of the provided DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the 'Speed_mph' column.

    Returns:
    None
    """
    # Create the histogram plot
    plt.figure(figsize=(10, 6))
    plt.hist(df['Speed_mph'], bins=20, color='skyblue', edgecolor='black')
    plt.xlabel('Speed (mph)')
    plt.ylabel('Frequency')
    plt.title('Histogram of Speed (mph)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()


def kde_plot_of_speed(df):
    """
    Generates a kernel density estimate (KDE) plot of the 'Speed_mph' column of the provided DataFrame.

    Parameters:
    df (pandas.DataFrame): The input DataFrame containing the 'Speed_mph' column.

    Returns:
    None
    """
    # Calculate the KDE
    speed_data = df['Speed_mph'].dropna()
    kde = gaussian_kde(speed_data)

    # Create the plot
    x_range = np.linspace(speed_data.min(), speed_data.max(), 1000)
    y_values = kde(x_range)

    plt.figure(figsize=(10, 6))
    plt.plot(x_range, y_values, color='blue')
    plt.fill_between(x_range, y_values, color='skyblue', alpha=0.5)
    plt.xlabel('Speed (mph)')
    plt.ylabel('Density')
    plt.title('KDE of Speed (mph)')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

bar_plot_of_data(df)
hist_plot_of_speed(df)
kde_plot_of_speed(df)

