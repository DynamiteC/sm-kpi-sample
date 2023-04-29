import csv
import random
import datetime
from scipy.stats import beta, gamma, poisson, norm

# Define the number of rows of data to generate
NUM_ROWS = 730

# Define the header row for the CSV file
header = ['date', 'page_views', 'click_through_rate', 'conversions', 'conversion_rate', 'age', 'gender', 'location',
          'campaign_type']

# Define the Facebook page to generate data for
page_name = 'my_facebook_page'

# Define the range of page views for the Facebook page
page_views_range = (1000, 1000000)

# Define the average click through rate per page view
ctr_per_page_view_range = (0.01, 0.05)

# Define the average conversion rate per click through
conversion_rate_range = (0.05, 0.20)

# Define the average age of the audience
age_range = (18, 65)

# Define the gender distribution of the audience
gender_distribution = {'male': 0.4, 'female': 0.6}

# Define the location distribution of the audience
location_distribution = {'United States': 0.5, 'Canada': 0.3, 'Mexico': 0.2}

# Define the types of campaign for the page growth
campaign_types = ['organic', 'paid']

# Generate the data for each row
data = []
current_date = datetime.date(2022, 1, 1)
previous_page_views = random.randint(*page_views_range)
for i in range(NUM_ROWS):
    # Generate the number of page views based on the previous day's value
    if i == 0:
        page_views = previous_page_views
    else:
        page_views = int(previous_page_views * random.uniform(0.95, 1.05))
        page_views = min(max(page_views, page_views_range[0]), page_views_range[1])

    # Generate the number of posts per day based on historical data
    num_posts = poisson.rvs(3)

    # Generate the number of clicks based on the number of page views and click through rate
    num_clicks = int(page_views * random.uniform(*ctr_per_page_view_range))

    # Generate the number of conversions based on the number of clicks and conversion rate
    num_conversions = int(num_clicks * random.uniform(*conversion_rate_range))

    # Calculate the conversion rate
    conversion_rate = num_conversions / num_clicks

    # Generate the age of the audience based on historical data
    age = int(norm.rvs(*age_range))

    # Generate the gender of the audience based on historical data
    gender = random.choices(list(gender_distribution.keys()), weights=list(gender_distribution.values()))[0]

    # Generate the location of the audience based on historical data
    location = random.choices(list(location_distribution.keys()), weights=list(location_distribution.values()))[0]

    # Generate the campaign type based on historical data
    campaign_type = random.choice(campaign_types)

    # Add the row to the data list
    data.append(
        [current_date.strftime('%Y-%m-%d'), page_views, num_clicks, num_conversions, conversion_rate, age, gender,
         location, campaign_type])

    # Increment the date for the next row
    current_date += datetime.timedelta(days=1)
    previous_page_views = page_views

# Save the data to a CSV file
with open('facebook_other_kpi_sample_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
