import pandas as pd
import numpy as np
from datetime import datetime

#NOP_DF = pd.read_csv('la_new_orleans_2020_04_01.csv')

#This limits the data you have to read in, i decided to drop all columns that are 40% NaN values and not extrapolatable
NOP_DF = pd.read_csv('la_new_orleans_2020_04_01.csv', usecols=lambda column: column not in ['search_basis', 'vehicle_model', 'vehicle_year', 'vehicle_color', 'vehicle_make', 'lat', 'lng'])
#print(NOP_DF.head())
#print(NOP_DF.tail())
#this called an err
#print(NOP_DF['date'].dtype())


##making a date time index
NOP_DF.dropna(subset=['date'], inplace=True)

NOP_DF['Date-Time'] = (NOP_DF['date'].str.cat(NOP_DF['time'], sep=' ')).tolist()
NOP_DF['Date-Time'] = pd.to_datetime(NOP_DF['Date-Time'], format="%Y-%m-%d %H:%M:%S")
#print(NOP_DF['Date-Time'].head())
#set the index as a chronological date time
NOP_DF = NOP_DF.set_index(('Date-Time'))

NOP_DF['time'] = pd.to_datetime(NOP_DF['time'], format='%H:%M:%S')


    #datetime.strptime(str(NOP_DF['date'] + ' ' +NOP_DF['time']), "%Y-%m-%d %H:%M:%S")
#print(NOP_DF['time'].head())
#print(str(NOP_DF['date'] + ' ' +NOP_DF['time']))
##Ah work life balance is good
# can pack outcome with the raw_actions taken for some
#Legal Basises: Warrant get this from one of the prints its in raw_actions_taken, it may be able to provide data for search basis
print(NOP_DF.dtypes)
#print(NOP_DF.columns)
#print("\n\n\n")
#print(NOP_DF.loc[0])
#print(NOP_DF.info)
#print(NOP_DF.describe())
#print('\n\n')
#CLEANING NULL VALUES FROM CONTEXTABLE TABLES
# Cleaning the code and NaN vlause for contraband is now False
NOP_DF['contraband_found'].fillna(False, inplace=True)
NOP_DF['contraband_weapons'].fillna(False, inplace=True)
NOP_DF['contraband_drugs'].fillna(False, inplace=True)

#NOP_DF.drop(['search_basis', 'vehicle_model', 'vehicle_year', 'vehicle_color', 'vehicle_make', 'lat', 'lng'], axis=1, inplace=True)

## the outcomes are [citation warning arrest]
## we need the arrest data to compare it
# to the time of day to see if .cor() does anything



first_index = NOP_DF['outcome'].first_valid_index()
print(NOP_DF.loc[first_index])
numbers_vars = NOP_DF.columns[NOP_DF.dtypes != 'object']
object_vars = NOP_DF.columns[NOP_DF.dtypes == 'object']

#This prints the list of columns and their percentage NaN entries
print(NOP_DF[NOP_DF.columns].isnull().sum().sort_values(ascending=False)/len(NOP_DF))

NOP_DF = NOP_DF.dropna(subset=['subject_sex'])

count_Male = (NOP_DF['subject_sex'] == 'male').sum()
count_Female = (NOP_DF['subject_sex'] == 'female').sum()

##assumptions are being made here
print(str((count_Male - count_Female)) + " More men are stopped than women\n")

#this compares the times a search orccurs vs not. it shows
Person_search_gender = pd.crosstab(NOP_DF['subject_sex'], NOP_DF['search_person'], normalize='index')
print(Person_search_gender)
Vehicle_search_gender = pd.crosstab(NOP_DF['subject_sex'], NOP_DF['search_vehicle'], normalize='index')
print(Vehicle_search_gender)

# how often a frisk happens during a search frisk percentage = (frisk.count / frisk.search)
#This will be normalised between 0 - 1 because stats
print((NOP_DF['frisk_performed'] == True).sum())
#print(NOP_DF['search_person'].unique())
print((NOP_DF['search_conducted'] == True).sum())
Frisk_percentage = (NOP_DF['frisk_performed'] == True).sum() / (NOP_DF['search_conducted'] == True).sum()
print(Frisk_percentage)

#trans inclusive? guess no enbies have been stopped driving in New Orleanse
distinct_values = NOP_DF['reason_for_stop'].unique()
print(distinct_values)

#night time stops
Night_Time_Stop = NOP_DF.between_time('22:00:00', '06:00:00').shape[0]
#filtered_df = df.loc[Night_Time_Stop]
print(str(Night_Time_Stop) + " Stops occur at night (10PM-6AM")
#finds the results
#print(NOP_DF.loc[(NOP_DF['outcome'] != 'citation') & (NOP_DF['outcome'].notnull()), ['outcome']])

#This was from chatgpt but was the moment pandas have
# clicked for me.
# I had forgotton the core tennant of python,
# It is all objects all the way down.
#A dataframe is just a a box of objects stacked onto and next to each other.
#you coud really easily write methods
# to unpack objects from df or manipulate the data in someway
#visualisation
distinct_values = NOP_DF['raw_actions_taken'].unique()
#print(distinct_values)

##OKAY THERE IS DEFINATLEY A WAY TO USE THE RAW ACTIONS TO PACK OUT THE DATA TO BE MORE ACCURATE AND INFORMATIVE
##IT WOULD BE SLICING THE RAW TEXT AS IT IS A DICTIONARY BUT THAT IS OUT OF SCOPE
# AND IT IS SUNDAY AND i NEED TO GET MY NAME LEGALLY CHANGED
#getting it

# a_values = NOP_DF.loc[NOP_DF['outcome'].isna(), 'raw_actions_taken'].dropna()
#
#
# b_values = a_values.apply(lambda x: x.split(':'))
#
# # enter sliced values into column B in the corresponding row
# df.loc[a_values.index, 'B'] = b_values.values

##Weird how the search basis is poorly recorded, feel like that is something that would hinder quite a lot of cases. Probabl cause makes sense and couold maybe be imperplated
##however .drop(works)

#print(NOP_DF.loc[0])


# print(numbers_vars)
# print('\n\n')
# print(object_vars)
# print('\n\n')
# print(NOP_DF.loc[first_index])
# print('\n\n')
# print(NOP_DF['lat'].dtypes)
# print('\n\n')
# print(len(NOP_DF))
# print(NOP_DF['contraband_found'].isnull().sum())
# print(NOP_DF['contraband_found'].dtypes)

# print(a['contraband_found'])
# print(a['contraband_found'].isnull().sum())
#print(NOP_DF['contraband_found'].isnull().sum())
#print('\n\n')
#print(NOP_DF.loc[NOP_DF['contraband_found'].notnull(), ['contraband_found']])


