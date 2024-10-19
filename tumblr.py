import requests
import pandas as pd

def get_communities(keyword):
    # URL to search for public groups containing the keyword
    url = f'https://www.googleapis.com/customsearch/v1?key=AIzaSyDmzZ5B86WPjcUpBghQ-F2Gg95T0dHmAiE&cx=63510fb2f693c4a11&q={keyword}+tumblr+community'

    response = requests.get(url).json()["items"]

    top_groups = pd.DataFrame({
        "name" : [response[i]["title"] for i in range(5)],
        "description" : [response[i]["pagemap"]["metatags"][0]["og:description"] for i in range(5)],
        "link" : [response[i]["link"] for i in range(5)]
    })
    
    return top_groups