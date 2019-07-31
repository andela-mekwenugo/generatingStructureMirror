"""
There are 2 data sets in this repository. One contains keywords performance data, another one contains ad group data.
You can join the data together on the AdGroupId

"""

# 1: Calculate the effective_bid for each row
# Tip: The effective bid is the CpcBid * device modifier (mobile, tablet, desktop) related to the Device of that row.
# The modifiers are currently formatted as strings, you need to convert them to a factor so you can use them to
# calculate the effective_bid


# 2: Add calender week numbers to the data set and aggregate all data to calender_week_nr, KeywordText, KeywordMatchType, Device level. Sum
#    Cost, Impressions and Clicks
#

# 3: Take the dataset you created in assignment 1. Find the cost of Keyword: kreditvergleich, KeywordMatchType: Exact,
#    Device: Computers and all rows available from february
