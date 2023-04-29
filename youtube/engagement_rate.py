import random
import csv

# Define the average engagement rate
avg_engagement_rate = 0.05

# Define the number of videos
num_videos = 100

# Define the start date
start_date = '2022-01-01'

# Define the header for the CSV file
header = ['Video ID', 'Publish Date', 'Views', 'Likes', 'Dislikes', 'Comments', 'Engagement Rate']

# Create an empty list to store the data
data = []

# Generate sample data for each video
for i in range(num_videos):
    # Generate a random number of views between 100 and 100,000
    views = random.randint(100, 100000)

    # Generate a random number of likes between 0 and the number of views
    likes = random.randint(0, views)

    # Generate a random number of dislikes between 0 and the number of views minus the number of likes
    dislikes = random.randint(0, views - likes)

    # Generate a random number of comments between 0 and 10% of the number of views
    comments = random.randint(0, int(0.1 * views))

    # Calculate the engagement rate
    engagement_rate = (likes + dislikes + comments) / views

    # Apply the average engagement rate to the actual engagement rate to introduce some variability
    engagement_rate *= random.uniform(0.5, 1.5) * avg_engagement_rate

    # Add the data to the list
    data.append([i + 1, start_date, views, likes, dislikes, comments, engagement_rate])

# Write the data to a CSV file
with open('youtube_engagement_rate.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(data)
