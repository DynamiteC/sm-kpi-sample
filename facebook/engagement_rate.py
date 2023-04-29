import csv
import random
import datetime
import math
import numpy as np
from scipy.stats import poisson, beta, gamma

# Define the number of days to generate data for
NUM_DAYS = 730

# Define the header row for the CSV file
header = ['date', 'page_views', 'posts', 'likes', 'comments', 'shares', 'engagement_rate']

# Define the Facebook page to generate data for
page_name = 'my_facebook_page'

# Use historical data to generate the initial number of page views
historical_data = [1000, 1200, 1500, 2000, 1800, 2500, 3000, 4000, 5000, 5500, 6000, 7000, 8000, 9000, 10000]
initial_page_views = int(np.random.choice(historical_data, 1))

# Generate the data for each day
data = []
current_date = datetime.date(2022, 1, 1)
for i in range(NUM_DAYS):
    # Generate a random number of posts based on a Poisson distribution with lambda=3
    posts = poisson.rvs(3)

    # Generate the number of likes, comments, and shares per post based on historical data
    likes = int(beta.rvs(2, 5, size=posts).sum())
    comments = int(gamma.rvs(2, loc=0.2, scale=1.5, size=posts).sum())
    shares = int(gamma.rvs(3, loc=0.5, scale=2, size=posts).sum())

    # Calculate the total number of page views for the day based on the previous day's value
    if i == 0:
        page_views = initial_page_views
    else:
        previous_page_views = data[i - 1][1]
        page_views = int(previous_page_views * random.uniform(0.95, 1.05))

    # Calculate the engagement rate using a more realistic formula
    engagement_rate = (0.3 * shares + 0.2 * comments + 0.1 * likes) / page_views

    # Add the row to the data list
    data.append([current_date.strftime('%Y-%m-%d'), page_views, posts, likes, comments, shares, engagement_rate])

    # Increment the date for the next row
    current_date += datetime.timedelta(days=1)

# Save the data to a CSV file
with open('facebook_engagement_rate_sample_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
