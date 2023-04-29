import csv
import random
import datetime
import math

# Define the number of rows of data to generate
NUM_ROWS = 730

# Define the header row for the CSV file
header = ['date', 'followers', 'likes', 'comments', 'engagement_rate', 'content_type', 'post_frequency']

# Define the Instagram account to generate data for
username = 'my_instagram_username'

# Define the range of followers for the Instagram account
initial_followers = 2000
max_followers = 900000
min_followers = 1000

# Define the average number of likes per follower
likes_per_follower_range = (0.02, 0.07)

# Define the average number of comments per like
comments_per_like_range = (0.05, 0.15)

# Define the content types for the posts
content_types = ['photo', 'video', 'carousel', 'story']

# Define the post frequency
post_frequency_range = (0.5, 1.5)

# Generate the data for each row
data = []
current_date = datetime.date(2022, 1, 1)
followers = initial_followers
for i in range(NUM_ROWS):
    # Calculate the number of followers based on the previous day's value
    previous_followers = followers
    followers_variation = random.randint(-500, 1000)  # Add some variability to the follower count
    followers += followers_variation
    followers = min(max(followers, min_followers), max_followers)

    # Calculate the average number of likes and comments per post
    likes_per_follower = random.uniform(*likes_per_follower_range)
    comments_per_like = random.uniform(*comments_per_like_range)

    # Calculate the number of likes and comments for each post
    avg_likes = followers * likes_per_follower
    avg_comments = avg_likes * comments_per_like
    likes = int(random.normalvariate(avg_likes, 0.2 * avg_likes))
    comments = int(random.normalvariate(avg_comments, 0.2 * avg_comments))

    # Calculate the engagement rate
    engagement_rate = (likes + comments) / followers

    # Choose a random content type for the post
    content_type = random.choice(content_types)

    # Calculate the post frequency
    post_frequency = random.uniform(*post_frequency_range)

    # Add the row to the data list
    data.append(
        [current_date.strftime('%Y-%m-%d'), followers, likes, comments, engagement_rate, content_type, post_frequency])

    # Increment the date for the next row
    current_date += datetime.timedelta(days=1)

# Save the data to a CSV file
with open('instagram_engagement_rate_sample_data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(data)
