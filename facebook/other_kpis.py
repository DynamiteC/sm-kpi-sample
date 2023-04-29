import csv
import random
import datetime
import math

# Define the number of days of data to generate
NUM_DAYS = 730

# Define the header row for the CSV file
header = ['date', 'page_views', 'click_through_rate', 'conversions', 'conversion_rate', 'age', 'gender', 'location']

# Define the Facebook page to generate data for
page_id = 'my_facebook_page_id'

# Define the range of page views for the Facebook page
page_views_range = (1000, 100000)

# Define the average click-through rate for the Facebook page
click_through_rate_range = (0.01, 0.05)

# Define the average conversion rate for the Facebook page
conversion_rate_range = (0.005, 0.02)

# Define the target demographic for the Facebook page
age_range = (18, 65)
gender_options = ['male', 'female']
location_options = ['US', 'Canada', 'UK', 'Australia']

# Generate the data for each day
data = []
current_date = datetime.date(2022, 1, 1)
for i in range(NUM_DAYS):
    # Calculate the number of page views based on the previous day's value
    if i == 0:
        page_views = random.randint(*page_views_range)
    else:
        previous_page_views = data[i - 1][1]
        page_views = int(previous_page_views * random.uniform(0.8, 1.2))
        page_views = min(max(page_views, page_views_range[0]), page_views_range[1])

    # Calculate the click-through rate and number of clicks
    click_through_rate = random.uniform(*click_through_rate_range)
    clicks = int(page_views * click_through_rate)

    # Calculate the conversions and conversion rate
    conversion_rate = random.uniform(*conversion_rate_range)
    conversions = int(clicks * conversion_rate)
    conversion_rate = conversions / clicks if clicks > 0 else 0

    # Generate the demographic targeting
    age = random.randint(*age_range)
    gender = random.choice(gender_options)
    location = random.choice(location_options)

    # Add the row to the data list
    data.append(
        [current_date.strftime('%Y-%m-%d'), page_views, click_through_rate, conversions, conversion_rate, age, gender,
         location])

    # Increment the date for the next row
    current_date += datetime.timedelta(days=1)

# Save the data to a CSV file
with open('facebook_other_kpi_sample_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
