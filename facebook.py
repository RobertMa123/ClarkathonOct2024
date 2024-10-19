import requests
import pandas as pd

def get_groups(keyword):
    # URL to search for public groups containing the keyword
    url = f'https://www.googleapis.com/customsearch/v1?key=AIzaSyDmzZ5B86WPjcUpBghQ-F2Gg95T0dHmAiE&cx=70c8a26a4782b4147&q={keyword}+facebook+group'

    response = requests.get(url).json()["items"]

    n = min(5,len(response))

    descriptions = []
    for i in range(n):
        if "og:description" in response[i]["pagemap"]["metatags"][0]:
            descriptions.append(response[i]["pagemap"]["metatags"][0]["og:description"])
        else:
            descriptions.append("No description provided")
    
    top_groups = pd.DataFrame({
        "name" : [response[i]["title"] for i in range(n)],
        "description" : descriptions,
        "link" : [response[i]["link"] for i in range(n)]
    })
    
    return top_groups

