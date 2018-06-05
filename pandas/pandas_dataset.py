import pandas as pd


def read_from_csv(csv_file):
    return pd.read_csv(csv_file, encoding='utf-8')

adgroups_csvfile = read_from_csv('data_sets/adgroups.csv')
keywords_csvfile = read_from_csv('data_sets/keywords.csv')


def combined_data():
    # Merge adgroups and keywords csv
    merge_two_csv_files = pd.merge(adgroups_csvfile, keywords_csvfile, on='AdGroupId')
    filename = 'data_sets/new_data.csv'
    # save to a new csv called new_data
    return merge_two_csv_files.to_csv(filename)


def assignment_1():
    # read from new_data csv
    df = read_from_csv('data_sets/new_data.csv')
    # convert Device string element to a factor
    device = pd.factorize(df['Device'])[0]
    # calculate effective bid (cpcbid * Device modifier)
    effective_bid = df['CpcBid'] * device
    # add the effective bid to data frame
    df['effective_bid'] = effective_bid
    # write into asignment 1 csv
    df.to_csv('data_sets/assignment1.csv')


def assignment_2():
    # read from new_data csv
    df = read_from_csv('data_sets/new_data.csv')
    # convert the Date to Date Time
    new_date = pd.to_datetime(df['Date'])
    # get the week number for each column
    week_number = new_date.dt.week
    # Add new_week as a new data set to the data frame
    df['week_number'] = week_number
    # group dataframe by week_number, KeywordText, KeywordMatchType and Device
    group_data = df.groupby(["week_number", "KeywordText", "KeywordMatchType", "Device"], as_index=False).count()
    # get cost, impressions and click data
    cost_data = group_data["Cost"]
    impressions_data = group_data["Impressions"]
    click_data = group_data["Clicks"]
    # add up cost, impressions and click data
    sum_of_cost_impressions_clicks = cost_data + impressions_data + click_data
    # save sum as a new data set
    group_data['sum_of_cost_impressions_clicks'] = sum_of_cost_impressions_clicks
    # output group_Data df to a csv called assignment_2.csv
    group_data.to_csv('data_sets/assignment2.csv')


def assignment_3():
    # read from assignment_1 csv
    df = read_from_csv('data_sets/assignment1.csv')
    # convert the Date to Date Time
    format_date = pd.to_datetime(df['Date'])
    # Get all data in February
    february_data = df.loc[(format_date.dt.month_name() == 'February') == 1]
    # Get Device with satisfactory data
    satisfactory_data = february_data.loc[(february_data['Device'] == 'Computers') & (february_data['KeywordText'] == 'kreditvergleich') & (february_data['KeywordMatchType'] == 'Exact') == 1]
    # Find cost of satisfactory data and return it
    cost_of_satisfactory_data = satisfactory_data['Cost']
    return cost_of_satisfactory_data

if __name__ == '__main__':
    print("Starting assignment 1")
    assignment_1()
    print("Starting assignment 2")
    assignment_2()
    print("Starting assignment 3")
    print(assignment_3())
