import pandas as pd
from datetime import datetime
from sklearn.preprocessing import scale
import csv


df = pd.read_csv('output_allyear_3_clean.csv')
df.columns = ['i','hack_license','pickup_datetime','dk','dk','dk','pickup_latitude','pickup_longitude','dropoff_latitude','dropoff_longitude','fare_amount','trip']
df['pickup_datetime'] = pd.to_datetime( df['pickup_datetime'] )
df['hour'] = df['pickup_datetime'].dt.hour
df['dow'] = df['pickup_datetime'].dt.dayofweek
df['morning'] = (df['hour'] >=5) & (df['hour'] <11)
df['afternoon'] = (df['hour'] >=11) & (df['hour'] <16)
df['rush'] = (df['hour'] >=16) & (df['hour'] <20)
df['evening'] = df['hour'] >=20 & df['hour'] <5
df['weekend'] = df['dow'] >=4

groups = pd.DataFrame(index = [ 'Morning_Wkday', 'Morning_Weeknd', 'Afternoon_Wkday', 'Afternoon_Weeknd','Rush_Wkday', 'Rush_Weeknd','Evening_Wkday', 'Evening_Weeknd',], columns = ['Mean','Std'])
flag_drivers = []
for i in range(0,24358):
	small_df = df[df['trip']==i]

	Morning_Wkday = small_df[(small_df['morning']==1) & (small_df['weekend'] ==0)][['hack_license','fare_amount']]
	if len(Morning_Wkday) > 30:
		Morning_Wkday['score'] = scale(Morning_Wkday['fare_amount'])
		flag_drivers += Morning_Wkday[Morning_Wkday['score'] >= 3]['hack_license'].tolist()
	Morning_Weeknd = small_df[(small_df['morning']==1) & (small_df['weekend'] ==1)][['hack_license','fare_amount']]
	if len(Morning_Weeknd) > 30:
		Morning_Weeknd['score'] = scale(Morning_Weeknd['fare_amount'])
		flag_drivers += Morning_Weeknd[Morning_Weeknd['score'] >= 3]['hack_license'].tolist()
	
	Afternoon_Wkday = small_df[(small_df['afternoon']==1) & (small_df['weekend'] ==0)][['hack_license','fare_amount']]
	if len(Afternoon_Wkday) > 30:
		Afternoon_Wkday['score'] = scale(Afternoon_Wkday['fare_amount'])
		flag_drivers += Afternoon_Wkday[Afternoon_Wkday['score'] >= 3]['hack_license'].tolist()
	Afternoon_Weeknd = small_df[(small_df['afternoon']==1) & (small_df['weekend'] ==1)][['hack_license','fare_amount']]
	if len(Afternoon_Weeknd) > 30:
		Afternoon_Weeknd['score'] = scale(Afternoon_Weeknd['fare_amount'])
		flag_drivers += Afternoon_Weeknd[Afternoon_Weeknd['score'] >= 3]['hack_license'].tolist()

	Rush_Wkday = small_df[(small_df['rush']==1) & (small_df['weekend'] ==0)][['hack_license','fare_amount']]
	if len(Rush_Wkday) > 30:
		Rush_Wkday['score'] = scale(Rush_Wkday['fare_amount'])
		flag_drivers += Rush_Wkday[Rush_Wkday['score'] >= 3]['hack_license'].tolist()
	Rush_Weeknd = small_df[(small_df['rush']==1) & (small_df['weekend'] ==1)][['hack_license','fare_amount']]
	if len(Rush_Weeknd) > 30:
		Rush_Weeknd['score'] = scale(Rush_Weeknd['fare_amount'])
		flag_drivers += Rush_Weeknd[Rush_Weeknd['score'] >= 3]['hack_license'].tolist()

	Evening_Weekday = small_df[(small_df['evening']==1) & (small_df['weekend'] ==0)][['hack_license','fare_amount']]
	if len(Evening_Weekday) > 30:
		Evening_Weekday['score'] = scale(Evening_Weekday['fare_amount'])
		flag_drivers += Evening_Weekday[Evening_Weekday['score'] >= 3]['hack_license'].tolist()
	Evening_Weeknd = small_df[(small_df['evening']==1) & (small_df['weekend'] ==1)][['hack_license','fare_amount']]
	if len(Evening_Weeknd) > 30:
		Evening_Weeknd['score'] = scale(Evening_Weeknd['fare_amount'])
		flag_drivers += Evening_Weeknd[Evening_Weeknd['score'] >= 3]['hack_license'].tolist()

with open('flag_drivers.csv','w') as csvfile:
	flag_drivers = set(flag_drivers)
	flag_drivers = list(flag_drivers)
	wr = csv.writer(csvfile)
	wr.writerow(flag_drivers)
