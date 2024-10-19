from flask import Flask, request, jsonify
from reddit import get_communities, get_posts_text
from facebook import get_groups
from gemini import summary_from_post_text, summary_from_desc
import random

app = Flask(__name__)

def run_reddit(keyword, num_communities):
    summaries = []
    communitiesDF = get_communities(keyword)
    
    # Ensure we do not exceed the number of available communities
    num_communities = min(num_communities, len(communitiesDF))
    
    for i in range(num_communities):
        community_name = communitiesDF['name'][i]
        posts_text = get_posts_text(community_name)
        num_members = str(communitiesDF['subscribers'][i])
        summary = summary_from_post_text(community_name, posts_text)
        link = communitiesDF['link'][i]  # Link to the community
        summaries.append({
            "source": "Reddit",
            "community": "r/" + community_name,
            "summary": summary,
            "num_members": num_members,
            "link": link  # Add link here
        })
    
    summaries.sort(key=lambda x: x['num_members'], reverse=True)
    return summaries

def run_fb(keyword, num_communities):
    summaries = []
    groupsDF = get_groups(keyword)
    num_communities = min(num_communities, len(groupsDF))
    
    for i in range(num_communities):
        group_name = groupsDF['name'][i]
        desc = groupsDF['description'][i]
        summary = summary_from_desc(group_name, desc)
        link = groupsDF['link'][i]  # Link to the group
        summaries.append({
            "source": "Facebook",
            "community": group_name,
            "summary": summary,
            "link": link  # Add link here
        })
    
    return summaries

@app.route('/')
def index():
    return app.send_static_file('index.html')  # Serve the HTML file

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
        combined_results += run_fb(keyword, num_communities)
    
    return jsonify({"result": combined_results})

if __name__ == '__main__':
    app.run(debug=True)
