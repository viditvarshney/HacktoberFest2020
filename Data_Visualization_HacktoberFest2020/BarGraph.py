Data Visualization with Python Inbuilt Python Pcakages

In this Problem I have used These Packages and Procedure:-

1.) Collected Dataset of Wind Turbine Images and Cleaned and Labelled them.

2.) Calculated their height and width and formed a CSV File.

3.) Imported Libraries:"Pandas-For Forming Data Frame", "Seaborn:-Seaborn is a library that
 uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions", 
 "Matplotlib:-matplotlib. pyplot is a collection of command style functions that make matplotlib work like MATLAB.
 Each pyplot function makes some change to a figure: e.g., creates a figure, creates a plotting area in a figure, 
 plots some lines in a plotting area, decorates the plot with labels".





import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_excel("/content/Training_Images_Data.xlsx")
data.columns

sns.set_style("darkgrid")

sns.countplot(data['No.of dects'],palette="rocket")


data['Width'].fillna(data['Width'].median(),inplace=True)
data['Height'].fillna(data['Height'].median(),inplace=True)

plt.figure(figsize=(10,6))
plt.subplot(2,2,1)
sns.distplot(data['Width'])

plt.subplot(2,2,2)
sns.distplot(data['Height'])

plt.figure(figsize=(10,6))
data['Defect-name'].value_counts().plot.bar()