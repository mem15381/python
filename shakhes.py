import pandas as pd
import jdatetime 
df = pd.read_csv('dollor.csv')
for i in range(len(df)):
#	print(len(df.iloc[i].jDate))
	if len(df.iloc[i].jDate) == 9:
		df["jDate"] = df.iloc[i].jDate[:8] + '0' + df.iloc[i].jDate[8]
df.to_csv("dollar.csv")
	   #jdate1 = df.iloc[i].jDate[:8] + '0' + df.iloc[i].jDate[9]
#	df["date1"] = pd.to_datetime(df["date"])
#df["jdate1"] = jdatetime.datetime.now()
#df["jdate1"] = jdatetime.date.fromgregorian(date=df["jDate"])
#df["jdate1"] = jdatetime.datetime.now().strftime("%y %m %d")
#print(df.head())
#print(df.to_string())