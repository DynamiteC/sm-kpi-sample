import csv
import random
import datetime

# Define the number of rows of data to generate
NUM_ROWS = 365

# Define the header row for the CSV file
header = ['date', 'impressions', 'reach', 'clicks', 'click_through_rate', 'mentions_in_dm', 'mentions_in_groups',
          'audience_age', 'audience_gender']

# Define the Instagram account to generate data for
username = 'my_instagram_username'

# Define the range of impressions for the Instagram account
impressions_range = (5000, 50000)

# Define the range of reach for the Instagram account
reach_range = (3000, 30000)

# Define the range of clicks for the Instagram account
clicks_range = (100, 1000)

# Define the range of mentions in DM for the Instagram account
mentions_in_dm_range = (50, 500)

# Define the range of mentions in groups for the Instagram account
mentions_in_groups_range = (100, 1000)

# Define the distribution of audience age for the Instagram account
audience_age_distribution = {'13-17': 0.1, '18-24': 0.3, '25-34': 0.4, '35-44': 0.15, '45+': 0.05}

# Define the distribution of audience gender for the Instagram account
audience_gender_distribution = {'male': 0.4, 'female': 0.6}

# Generate the data for each row
data = []
current_date = datetime.date(2022, 1, 1)
for i in range(NUM_ROWS):
    # Calculate the number of impressions and reach based on the previous day's value
    if i == 0:
        impressions = random.randint(*impressions_range)
        reach = random.randint(*reach_range)
    else:
        previous_impressions = data[i - 1][1]
        previous_reach = data[i - 1][2]
        impressions = int(previous_impressions * random.uniform(0.9, 1.1))
        reach = int(previous_reach * random.uniform(0.9, 1.1))
        impressions = min(max(impressions, impressions_range[0]), impressions_range[1])
        reach = min(max(reach, reach_range[0]), reach_range[1])

    # Calculate the number of clicks based on the impressions and reach
    clicks = int((impressions + reach) * random.uniform(0.01, 0.05))
    clicks = min(max(clicks, clicks_range[0]), clicks_range[1])

    # Calculate the click-through rate
    click_through_rate = clicks / (impressions + reach)

    # Calculate the number of mentions in DM and groups
    mentions_in_dm = int(impressions * random.uniform(0.001, 0.005))
    mentions_in_groups = int(impressions * random.uniform(0.002, 0.01))

    # Calculate the audience demographics
    audience_age = \
    random.choices(list(audience_age_distribution.keys()), weights=list(audience_age_distribution.values()))[0]
    audience_gender = \
    random.choices(list(audience_gender_distribution.keys()), weights=list(audience_gender_distribution.values()))[0]

    # Add the row to the data list
    data.append(
        [current_date.isoformat(), impressions, reach, clicks, click_through_rate, mentions_in_dm, mentions_in_groups,
         audience_age, audience_gender])

    # Increment the date for the next row
    current_date += datetime.timedelta(days=1)

# Save the data to a CSV file
with open('instagram_other_kpi_sample_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
