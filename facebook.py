import requests

def get_groups(keyword):
    # URL to search for public groups containing the keyword
    url = f'https://www.googleapis.com/customsearch/v1?key=AIzaSyDmzZ5B86WPjcUpBghQ-F2Gg95T0dHmAiE&cx=70c8a26a4782b4147&q={keyword}+facebook+group'

    response = requests.get(url).json()

    top_groups = {}
    
    for i in range(3):
        top_groups[response["items"][i]["title"]] = response["items"][i]["link"]
    
    return top_groups

