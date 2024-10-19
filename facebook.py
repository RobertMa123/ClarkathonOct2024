import requests
import pandas as pd

def get_groups(keyword):
    # URL to search for public groups containing the keyword
    url = f'https://www.googleapis.com/customsearch/v1?key=AIzaSyDmzZ5B86WPjcUpBghQ-F2Gg95T0dHmAiE&cx=70c8a26a4782b4147&q={keyword}+facebook+group'

    response = requests.get(url).json()["items"]
    
    limit = min(5, len(response))

    top_groups = pd.DataFrame({
        "name" : [response[i]["title"] for i in range(5)],
        "description" : [response[i]["pagemap"]["metatags"][0]["og:description"] for i in range(5)],
        "link" : [response[i]["link"] for i in range(5)]
    })
    
    return top_groups

