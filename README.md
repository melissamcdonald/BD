# BetterDoctor

written in Python 3.6 (I use the Anaconda distribution)
packages: pandas, json

The file assumes that match_file.csv and source_file.json are saved in the same directory as bd_assignment.py.  If not, some adjustment to the filepaths will be necessary in the script.

I decided to load the match_file info into a dataframe so I could store the indices of the matches.  This was useful for finding the number of unique records that had at least one match, and would also be useful to lookup those records later(or eliminate them and only look at the records not matched).

For the source_data, I parsed it and stored full name, npi, and full address in lists to compare with the matched data.  This approach saved a lot of time over looping through the json again and again for each record.

I decided to only use the first 5 characters of the zip code for comparison.  I noticed it wasn't consistent whether the zip had the +4 code in both the match_file and source_data, so I stripped it out and converted them to strings to create the full address. 

Instead of converting the other address information to have correct capitalization (to match the source file), I instead converted all strings to lower in both data sets before comparision.

 