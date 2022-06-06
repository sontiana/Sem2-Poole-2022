import numpy as np
from numpy import random
import pandas as pd
import matplotlib.pyplot as plt # import matlab plotting!
plt.rcParams.update({'font.size': 15, 'figure.figsize': (8, 5)}) # set font and plot size to be larger

print("Average Area of US States")
states_df = pd.read_csv("state-areas.csv", index_col="state")
states_df.columns
states_df['area (sq. mi)'].plot(kind='hist', title='Area')

print("Average Heights of US Presidents")
heights_df = pd.read_csv("president_heights.csv", index_col="name")
heights_df.columns
heights_df['height(cm)'].plot(kind="box");