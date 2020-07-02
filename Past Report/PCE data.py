import numpy as np
import pandas as pd

PCE_data = pd.read_html('C://Users//CT//Documents//data-science-for-good-kiva-crowdfunding//PCE data.html')
PCE_data = PCE_data[0]

print(PCE_data.shape)

# Made a copy of the data: 
GEEdata = PCE_data.copy()

# Reference rows:
print('')
print(GEEdata.iloc[0,0])
print(GEEdata.iloc[18,0])
print(GEEdata.iloc[49,0])
print(GEEdata.iloc[76,0])
print(GEEdata.iloc[87,0])
print(GEEdata.iloc[132,0])
print(GEEdata.iloc[140,0])

# Make a regional column for the data
GEEdata.loc[:, 'region'] = 0
GEEdata['region'].iloc[1:18] = 'East Asia and Pacific'
GEEdata['region'].iloc[19:49] = 'Europe and Central Asia'
GEEdata['region'].iloc[50:76] = 'Latin America and the Caribbean'
GEEdata['region'].iloc[77:87] = 'Middle East and North Africa'
GEEdata['region'].iloc[88:132] = 'Other High Income'
GEEdata['region'].iloc[133:140] = 'South Asia'
GEEdata['region'].iloc[141:186] = 'Sub-Saharan Africa'

# Delete header rows
GEEdata = GEEdata.drop(labels=[0,18,49,76,87,132,140], axis=0)

print('')
print(GEEdata.iloc[0,0]) # should not have East Asia and Pacific
print(GEEdata.iloc[18,0]) # should not have Europe and Central Asia
print(GEEdata.iloc[49,0]) # should not have Latin America and the Caribbean
print(GEEdata.iloc[76,0]) # should not have Middle East and North Africa
print(GEEdata.iloc[87,0]) # should not have Other high Income
print(GEEdata.iloc[132,0]) # should not have South Asia
print(GEEdata.iloc[140,0]) # should not have Sub-Saharan Africa

print('')
print(GEEdata.shape)

# Convert any 'n/a' strings to NaN values
GEEdata = GEEdata.replace('n/a', np.nan)

# Convert any numeric data stored as a string into a decimal
print('')
print(GEEdata.dtypes)

GEEdata['1960'] = GEEdata['1960'].astype('float64')
GEEdata['1961'] = GEEdata['1961'].astype('float64')
GEEdata['1962'] = GEEdata['1962'].astype('float64')
GEEdata['1963'] = GEEdata['1963'].astype('float64')
GEEdata['1964'] = GEEdata['1964'].astype('float64')
GEEdata['1965'] = GEEdata['1965'].astype('float64')
GEEdata['1966'] = GEEdata['1966'].astype('float64')
GEEdata['1967'] = GEEdata['1967'].astype('float64')
GEEdata['1968'] = GEEdata['1968'].astype('float64')

print('')
print(GEEdata.dtypes)

# Convert any NaN values to 'N/A' strings 
#GEEdata = GEEdata.replace(np.nan, 'N/A')

# Export this data as CSV
GEEdata.to_csv('C://Users//CT//Documents//PCE data.csv', index=False)
