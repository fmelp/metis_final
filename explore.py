import pandas as pd
import numpy as np

# booking data
bookings = pd.read_csv('~/Desktop/final_project/borgo_room_data/bookings_final.csv')
# 2013 actual occupancy and other stats by day
thirteen = pd.read_csv('~/Desktop/final_project/borgo_room_data/2013.csv')
# 2014 actual occupancy and other stats by day
fourteen = pd.read_csv('~/Desktop/final_project/borgo_room_data/2014.csv')
# concat 2013 and 2014
actuals = pd.concat([thirteen, fourteen])

# add occupancy rate
occupancy = actuals['Occupancy']
occupancy_rate = [x/184.0 for x in occupancy]
actuals['Occupancy_rate'] = occupancy_rate

print len(bookings)
# get rid of free bookings
bookings = bookings[bookings.RicaviRoom > 80]
print len(bookings)
print bookings['RicaviRoom'].describe()
print bookings['RicaviRoom'].idxmin()

date = bookings[bookings.date_res == '15/09/14']

print date['DataPrenotazione']

