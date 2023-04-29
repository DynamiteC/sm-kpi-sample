import random
import csv
import datetime

# Set up the starting values
subscriber_count = 1000
total_views = 2000
likes_count = 500
dislikes_count = 20

# Set up the headers for the CSV file
headers = ["Date", "Subscriber Count", "Total Views", "Likes Count", "Dislikes Count", "Engagement Rate"]

# Set up the start and end dates
start_date = "2022-01-01"
end_date = "2023-12-31"

# Create a list of dates between the start and end dates
date_list = []
current_date = start_date
while current_date <= end_date:
    date_list.append(current_date)
    current_date = (datetime.datetime.strptime(current_date, "%Y-%m-%d") + datetime.timedelta(days=1)).strftime("%Y-%m-%d")

# Set up the CSV file
with open("youtube_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)

    # Generate the data for each day
    for date in date_list:
        # Generate random engagement rate between 1% and 10%
        engagement_rate = random.uniform(0.01, 0.1)

        # Calculate the number of likes and dislikes based on the engagement rate
        likes = int(total_views * engagement_rate * random.uniform(0.8, 1.2))
        dislikes = int(likes * random.uniform(0.01, 0.1))

        # Calculate the new total views based on the engagement rate
        total_views = int(total_views * (1 + engagement_rate * random.uniform(0.8, 1.2)))

        # Calculate the new subscriber count based on the engagement rate
        subscriber_count = int(subscriber_count * (1 + engagement_rate * random.uniform(0.8, 1.2)))

        # Update the likes and dislikes count
        likes_count += likes
        dislikes_count += dislikes

        # Write the data to the CSV file
        writer.writerow([date, subscriber_count, total_views, likes_count, dislikes_count, engagement_rate])
