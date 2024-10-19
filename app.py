from flask import Flask, request, jsonify, send_from_directory
from reddit import get_communities, get_posts_text
from facebook import get_groups
from gemini import summary_from_post_text, summary_from_desc, summary_tumblr, find_events
from tumblr import get_communities as get_tumblr_communities, scrape_tumblr  # Import Tumblr communities
import os

app = Flask(__name__, static_folder='static')  # Set the folder for serving static files (HTML, CSS, JS)

def run_reddit(keyword, num_communities):
    summaries = []
    communitiesDF = get_communities(keyword, num_communities)
    
    n = min(num_communities, len(communitiesDF))
    
    for i in range(n):
        community_name = communitiesDF['name'][i]
        posts_text = get_posts_text(community_name)
        num_members = str(communitiesDF['subscribers'][i])
        try:
            summary = summary_from_post_text(community_name, posts_text)
        except:
            summary = "No Description"
        link = communitiesDF['link'][i]  

        events = check_events(community_name, posts_text)  # Get events from posts
        summaries.append({
            "source": "Reddit",
            "name": "r/" + community_name,
            "summary": summary,
            "events": events,  # Add events to the response
            "num_members": num_members,
            "link": link  
        })
    
    summaries.sort(key=lambda x: x['num_members'], reverse=True)
    return summaries

def run_facebook(keyword, num_communities):
    summaries = []
    groupsDF = get_groups(keyword)
    n = min(num_communities, len(groupsDF))
    
    for i in range(n):
        group_name = groupsDF['name'][i]
        desc = groupsDF['description'][i]
        try:
            summary = summary_from_desc(group_name, desc)
        except:
            summary = "No description"
        link = groupsDF['link'][i]  

        events = check_events(group_name, desc)  # Get events from group description
        summaries.append({
            "source": "Facebook",
            "name": group_name,
            "summary": summary,
            "events": events,  # Add events to the response
            "link": link  
        })
    
    return summaries

def run_tumblr(keyword, num_communities):
    summaries = []
    communitiesDF = get_tumblr_communities(keyword)  # Using Tumblr's get_communities function
    n = min(num_communities, len(communitiesDF))
    
    for i in range(n):
        community_name = communitiesDF['name'][i]
        desc = communitiesDF['description'][i]
        try:
            summary = summary_tumblr(community_name, desc)
        except:
            summary = "No Description"
        link = communitiesDF['link'][i]

        scraped = scrape_tumblr(link)
        events = check_events(community_name, scraped)  # Get events from scraped Tumblr data
        summaries.append({
            "source": "Tumblr",
            "name": community_name,
            "summary": summary,
            "events": events,  # Add events to the response
            "link": link  
        })
    
    return summaries

def check_events(keyword, text):
    result = find_events(keyword, text)
    print(result)
    
    # Ensure result is a list, even if it's a single event string
    if isinstance(result, list):
        return result
    elif isinstance(result, str) and result.startswith("Event Found!"):
        return [result]  # Return as a single-item list
    else:
        return []  # Return empty list if no events found or incorrect format

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')  # Serve the HTML file from the static folder

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        keyword = data['keyword']
        num_communities = int(data['numCommunities'])
        platforms = data['platforms']

        combined_results = []
        if 'reddit' in platforms:
            combined_results += run_reddit(keyword, num_communities)
        if 'facebook' in platforms:
            combined_results += run_facebook(keyword, num_communities)
        if 'tumblr' in platforms:
            combined_results += run_tumblr(keyword, num_communities)

        return jsonify({"success": True, "communities": combined_results})
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"success": False, "error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
