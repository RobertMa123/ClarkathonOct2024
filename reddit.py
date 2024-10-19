import requests as rq
import pandas as pd

def get_communities(keyword):
    url = f'https://www.reddit.com/subreddits/search.json?q={keyword}'
    headers = {'User-Agent': 'Mozilla/5.0'}
    result = rq.get(url, headers=headers).json()
    subreddits = result['data']['children']
    df = pd.DataFrame({
    "name" : [sub["data"]["display_name"] for sub in subreddits],
    "subscribers" : [sub["data"]["subscribers"] for sub in subreddits],
    "title" : [sub["data"]["title"] for sub in subreddits]
    })
    return df

def get_posts_text(community_name):
    sub_url = f'https://www.reddit.com/r/{community_name}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    subreddit_posts = rq.get(sub_url, headers=headers).json()["data"]["children"]
    combined_text = ""
    for i in range(len(subreddit_posts)):
        combined_text += f"Post {i}\nTitle: {subreddit_posts[i]["data"]["title"]}\n"
        combined_text += subreddit_posts[i]["data"]["selftext"]
    return combined_text