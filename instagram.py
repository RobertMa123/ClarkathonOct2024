import requests

def get_groups(keyword):
    url = f'https://www.googleapis.com/customsearch/v1?key=APIKEY&cx=a6e44c78f3a844486&q={keyword}'

    response = requests.get(url).json()

    topGroups = {}

    for i in range(3):
        topGroups[response["items"][i]["title"]] = response["items"][i]["link"]

    return topGroups
