import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# load seaborn default settings
sns.set()

airbus = pd.read_csv('/Users/albertovilla/Documents/OneDrive/projects/aircraft_analysis/airbus.csv', index_col=0)
boeing = pd.read_csv('/Users/albertovilla/Documents/OneDrive/projects/aircraft_analysis/boeing.csv', index_col=0)

airbus_t = airbus.transpose()
airbus_t.plot()

boeing_t = boeing.transpose()
boeing_t.plot()

planes = airbus_t.join(boeing_t)

plt.figure()
planes[['A320', 'B737']].plot()