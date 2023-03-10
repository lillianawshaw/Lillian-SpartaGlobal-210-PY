import pandas as pd
import numpy as np

#NOP_DF = pd.read_csv('la_new_orleans_2020_04_01.csv')

#This limits the data you have to read in, i decided to drop all columns that are 40% NaN values and not extrapolatable
NOP_DF = pd.read_csv('la_new_orleans_2020_04_01.csv', usecols=lambda column: column not in ['search_basis', 'vehicle_model', 'vehicle_year', 'vehicle_color', 'vehicle_make', 'lat', 'lng'])

##Ah work life balance is good
# can pack outcome with the the raw_actions taken for some
#Legal Basises: Warrant get this from one of the prints its in raw_actions_taken, it may be able to provide data for search basis

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
#print(NOP_DF[NOP_DF.columns].isnull().sum().sort_values(ascending=False)/len(NOP_DF))

#finds the results
print(NOP_DF.loc[(NOP_DF['outcome'] != 'citation') & (NOP_DF['outcome'].notnull()), ['outcome']])

#This was from chatgpt but was the moment pandas have
# clicked for me.
# I had forgotton the core tennant of python,
# It is all objects all the way down.
#A dataframe is just a a box of objects stacked onto and next to each other.
#you coud really easily write methods
# to unpack objects from df or manipulate the data in someway
#visualisation
distinct_values = NOP_DF['raw_actions_taken'].unique()
print(distinct_values)

##Weird how the search basis is poorly recorded, feel like that is something that would hinder quite a lot of cases. Probabl cause makes sense and couold maybe be imperplated
##however .drop(works)

print(NOP_DF.loc[0])


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


