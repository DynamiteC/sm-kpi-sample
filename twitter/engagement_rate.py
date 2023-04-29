import random
import csv
import datetime

# Define constants
START_DATE = '2022-01-01'
END_DATE = '2023-12-31'
AVERAGE_FOLLOWERS = 5000
AVERAGE_IMPRESSIONS = 10000
AVERAGE_LIKES = 100
AVERAGE_RETWEETS = 10
AVERAGE_REPLIES = 5


# Define functions for generating random data
def generate_engagement_rate():
    return random.uniform(0.01, 0.5)


def generate_followers():
    return int(random.normalvariate(AVERAGE_FOLLOWERS, AVERAGE_FOLLOWERS * 0.1))


def generate_impressions():
    return int(random.lognormvariate(0, 1) * AVERAGE_IMPRESSIONS)


def generate_likes():
    return int(random.lognormvariate(0, 1) * AVERAGE_LIKES)


def generate_retweets():
    return int(random.lognormvariate(0, 1) * AVERAGE_RETWEETS)


def generate_replies():
    return int(random.lognormvariate(0, 1) * AVERAGE_REPLIES)


# Generate data for each day
data = []
current_date = START_DATE
while current_date <= END_DATE:
    engagement_rate = generate_engagement_rate()
    followers = generate_followers()
    impressions = generate_impressions()
    likes = generate_likes()
    retweets = generate_retweets()
    replies = generate_replies()

    engagement = (likes + retweets + replies) * engagement_rate
    row = [current_date, followers, impressions, likes, retweets, replies, engagement]
    data.append(row)

    # Increment date
    current_date = (datetime.datetime.strptime(current_date, '%Y-%m-%d') + datetime.timedelta(days=1)).strftime(
        '%Y-%m-%d')

# Export data to CSV file
with open('twitter_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Followers', 'Impressions', 'Likes', 'Retweets', 'Replies', 'Engagement'])
    writer.writerows(data)
