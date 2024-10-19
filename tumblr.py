import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_communities(keyword):
    # URL to search for public groups containing the keyword
    url = f'https://www.googleapis.com/customsearch/v1?key=AIzaSyDmzZ5B86WPjcUpBghQ-F2Gg95T0dHmAiE&cx=63510fb2f693c4a11&q={keyword}+tumblr+community'

    response = requests.get(url).json()["items"]
    limit = min(5, len(response))

    top_groups = pd.DataFrame({
        "name" : [response[i]["title"] for i in range(limit)],
        "description" : [response[i]["pagemap"]["metatags"][0]["og:description"] for i in range(limit)],
        "link" : [response[i]["link"] for i in range(limit)]
    })
    
    return top_groups

def scrape_tumblr(url):
    # Send a request to the Tumblr page
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: Unable to access the page. Status code {response.status_code}")
        return None
    
    # Parse the page content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all blog post content
    posts = soup.find_all('article')  # 'article' is often used to wrap posts; may vary by theme
    
    posts_str = ""
    
    for index, post in enumerate(posts, start=1):
        
        if index > 20:
            break
        
        # Extract the title of the post, if available
        title_tag = post.find('h2')
        title = title_tag.get_text(strip=True) if title_tag else 'No title'
        
        # Extract all relevant content from the post (text, images, etc.)
        content_elements = post.find_all(['p', 'div', 'h2', 'h3', 'ul', 'ol', 'li', 'img'])
        
        content = []
        seen_text = set()  # To keep track of unique text
        
        for element in content_elements:
            # Get the text from the element
            text = element.get_text(strip=True)
            check = {text: 0}
            for i in seen_text:
                if text in i:
                    check[text]=check[text]+1
            
            
            # If text has already been captured, skip this element and its children
            if text and check[text]==0:
                # Handle images by getting their URL
                if element.name == 'img':
                    img_url = element.get('src')
                    if img_url and img_url not in seen_text:
                        content.append(f"[Image: {img_url}]")
                        seen_text.add(img_url)
                else:
                    # Capture only the parent text (avoid repeating child text)
                    content.append(text)
                    seen_text.add(text)
        
        # Join all content parts together
        full_content = '\n'.join(content)
        posts_str += f"Post {index}:\n"
        posts_str += f"Title: {title}\n"
        posts_str += f"Content:\n{full_content}\n"
    
    return posts_str