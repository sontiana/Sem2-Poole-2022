import pandas as pd
import matplotlib.pyplot as plt # import matlab plotting!

plt.rcParams.update({'font.size': 20, 'figure.figsize': (10, 8)}) # set font and plot size to be larger
movies_df = pd.read_csv("IMDB-Movie-Data.csv", index_col="Title")
movies_df.columns
year = movies_df['Year']
year.head()

movies_df['Year'].plot(kind='hist', title='Release Years');
movies_df.plot(kind='scatter', x='Year', y='Metascore', title='Relationship of Release Years and Metascore');
metascore = movies_df['Metascore']
metascore_mean = metascore.mean()  
metascore_mean