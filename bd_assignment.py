# -*- coding: utf-8 -*-
"""
Melissa McDonald  - 6/11/2018
Data Processing For Better Doctor
Loop through each row in match_file.csv to try to find a match in 
source_data.json using NPI(NPI field), Name(First and Last Name fields), and 
Address(street, street_2, city, state, and zip fields).  Report those totals 
as well as number of unique records matched.
"""

import pandas as pd

#create dataframe, df, from match_file data 
df = pd.read_csv('match_file.csv')

#json processing: read in and add each listing's data to lists
l_name=[]
l_npi=[]
l_address=[]

import json
with open('source_data.json') as json_file:
    for line in json_file:
        listing=(json.loads(line))
        #for each listing in the source data, add the full name to l_name, 
        #add npi to l_npi, add full address to l_address
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
total=set()
   
#for each record in match_file, see if the name, npi, and address already 
#exist in the source data 
for row in range(len(df.first_name)):
    if (" ".join([df.first_name[row],df.last_name[row]]).lower()) in l_name:
        names_match.append(row)
        total.add(row)
    if (df.npi[row]) in l_npi:
        npis_match.append(row)
        total.add(row)
    if (" ".join([str(df.street[row]).lower(), 
                  str(df.street_2[row]).lower(), 
                  str(df.city[row]).lower(), 
                  str(df.state[row]).lower(), 
                  str(df.zip[row])[:5]])) in l_address:   
        addresses_match.append(row)
        total.add(row)

#report results (length of each match list, length of total set)
print("Total Matched Documents: {}".format(len(total)))       
print("Matched Documents Using First and Last Name: {}".format(len(names_match)))
print("Matched Documents by NPI: {}".format(len(npis_match)))
print("Matched Documents Using Address: {}".format(len(addresses_match)))   