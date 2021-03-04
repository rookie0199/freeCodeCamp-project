import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv',
                     float_precision='legacy')

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])

    #Get the slope and y-intercept of the line of best fit
    res_1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1_pred = list(range(1880, 2050))
    y1_pred = []
    for i in x1_pred:
        y1_pred.append(res_1.intercept + res_1.slope*i)
    # Create first line of best fit
    ax.plot(x1_pred, y1_pred, color='g')

    # Create second line of best fit
    df_2 = df.loc[df['Year'] > 2000]
    res_2 = linregress(df_2['Year'], df_2['CSIRO Adjusted Sea Level'])
    x2_pred = list(range(2000, 2050))
    y2_pred = []
    for i in x2_pred:
        y2_pred.append(res_2.intercept + res_2.slope*i)
    ax.plot(x2_pred, y2_pred, color='r')
    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()