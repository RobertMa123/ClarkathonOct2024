from flask import Flask, request, jsonify, send_from_directory
from reddit import get_communities, get_posts_text
from facebook import get_groups
from gemini import summary_from_post_text, summary_from_desc, summary_tumblr
from tumblr import get_communities as get_tumblr_communities  # Import Tumblr communities
import os

app = Flask(__name__, static_folder='static')  # Set the folder for serving static files (HTML, CSS, JS)

def run_reddit(keyword, num_communities):
    summaries = []
    communitiesDF = get_communities(keyword)
    
    num_communities = min(num_communities, len(communitiesDF))
    
    for i in range(num_communities):
        community_name = communitiesDF['name'][i]
        posts_text = get_posts_text(community_name)
        num_members = str(communitiesDF['subscribers'][i])
        try:
            summary = summary_from_post_text(community_name, posts_text)
        except:
            summary = "No Description"
        link = communitiesDF['link'][i]  
        summaries.append({
            "source": "Reddit",
            "community": "r/" + community_name,
            "summary": summary,
            "num_members": num_members,
            "link": link  
        })
    
    summaries.sort(key=lambda x: x['num_members'], reverse=True)
    return summaries

def run_facebook(keyword, num_communities):
    summaries = []
    groupsDF = get_groups(keyword)
    num_communities = min(num_communities, len(groupsDF))
    
    for i in range(num_communities):
        group_name = groupsDF['name'][i]
        desc = groupsDF['description'][i]
        try:
            summary = summary_from_desc(group_name, desc)
        except:
            summary = "No description"
        link = groupsDF['link'][i]  
        summaries.append({
            "source": "Facebook",
            "community": group_name,
            "summary": summary,
            "link": link  
        })
    
    return summaries

def run_tumblr(keyword, num_communities):
    summaries = []
    communitiesDF = get_tumblr_communities(keyword)  # Using Tumblr's get_communities function
    num_communities = min(num_communities, len(communitiesDF))
    
    for i in range(num_communities):
        community_name = communitiesDF['name'][i]
        desc = communitiesDF['description'][i]
        try:
            summary = summary_tumblr(community_name, desc)
        except:
            summary = "No Description"
        link = communitiesDF['link'][i]
        summaries.append({
            "source": "Tumblr",
            "community": community_name,
            "summary": summary,
            "link": link  
        })
    
    return summaries

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')  # Serve the HTML file from the static folder

@app.route('/search', methods=['POST'])
def search():
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
    
    return jsonify({"result": combined_results})

if __name__ == '__main__':
    app.run(debug=True)
