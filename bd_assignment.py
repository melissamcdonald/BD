# -*- coding: utf-8 -*-
"""
Melissa McDonald  - 6/9/2018
Data Processing For Better Doctor
Loop through each row in match_file.csv to try to find a match in 
source_data.json using NPI(NPI field), Name(First and Last Name fields), and 
Address(street, street_2, city, state, and zip fields).  Report those totals 
as well as number of unique records matched.
"""

import pandas as pd


df = pd.read_csv('match_file.csv')

#def capitalize_each_word(series):
#    return pd.Series([str(x).title() for x in series])

df.zip=pd.Series([str(x)[:5] for x in df.zip])
#df.street=capitalize_each_word(df.street)
#df.street_2=capitalize_each_word(df.street_2)
#df.city=capitalize_each_word(df.city)
#df.state=pd.Series([str(x).upper() for x in df.state])


#json processing: read in and add each listing to data
import json
data = []
with open('source_data.json') as json_file:
    for line in json_file:
        data.append(json.loads(line))


#initialize lists to store source data
l_name=[]
l_npi=[]
l_address=[]
 
#for each listing in the source data, add the full name to l_name, add npi to l_npi, add full address to l_address
for listing in data:
    l_name.append(" ".join([listing['doctor']['first_name'].lower(), 
                            listing['doctor']['last_name'].lower()])) 
    l_npi.append(listing['doctor']['npi'])
    for practice in listing['practices']:
        l_address.append(" ".join([practice['street'].lower(),
                                   practice['street_2'].lower(), 
                                   practice['city'].lower(), 
                                   practice['state'].lower(), 
                                   str(practice['zip'])[:5]]))

#initialize lists to hold indices of records that have a match in the source data
names_match=[]
npis_match=[]
addresses_match=[]
   
#for each record in match_file, see if the name, npi, and address already exist in the source data 
for row in range(len(df.first_name)):
    if (" ".join([df.first_name[row],df.last_name[row]]).lower()) in l_name:
        names_match.append(row)
    if (df.npi[row]) in l_npi:
        npis_match.append(row)
    if (" ".join([str(df.street[row]).lower(), 
                  str(df.street_2[row]).lower(), 
                  str(df.city[row]).lower(), 
                  str(df.state[row]).lower(), 
                  df.zip[row]])) in l_address:   
        addresses_match.append(row)

print("Total Matched Documents: {}".format(len(set(names_match) | set(npis_match) | set(addresses_match))))        
print("Matched Documents Using First and Last Name: {}".format(len(names_match)))
print("Matched Documents by NPI: {}".format(len(npis_match)))
print("Matched Documents Using Address: {}".format(len(addresses_match)))   