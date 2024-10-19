import google.generativeai as gem

def summary_from_post_text(community,text):
    gem.configure(api_key="AIzaSyA8XQWC7KyDbZozq7iLzJh-n9Ptusn3NP0")
    model = gem.GenerativeModel("gemini-1.5-flash",system_instruction=f"You are going to be sent posts from a community called {community}"+
                                " summarize the vibe and conversation in less than 3 sentences. Do not use the word vibrant."+
                                ". If this may contain dangerous or explicit material, say no description provided")
    model_response = model.generate_content(text)
    return model_response.text

def summary_from_desc(group, text):
    gem.configure(api_key="AIzaSyA8XQWC7KyDbZozq7iLzJh-n9Ptusn3NP0")
    model = gem.GenerativeModel("gemini-1.5-flash",system_instruction=f"You are going to be sent a description of a facebook group called {group}"+
                                " summarize and rewrite the description in less than 3 sentences"+
                                ". If this may contain dangerous or explicit material, say no description provided")
    model_response = model.generate_content(text)
    return model_response.text

def summary_tumblr(group, text):
    gem.configure(api_key="AIzaSyA8XQWC7KyDbZozq7iLzJh-n9Ptusn3NP0")
    model = gem.GenerativeModel("gemini-1.5-flash",system_instruction=f"You are going to be sent a description of a tumblr group called {group}"+
                                " summarize and rewrite the description in less than 3 sentences"+
                                ". If this may contain dangerous or explicit material, say no description provided")
    model_response = model.generate_content(text)
    return model_response.text

def find_events(group, text):
    gem.configure(api_key="AIzaSyA8XQWC7KyDbZozq7iLzJh-n9Ptusn3NP0")
    model = gem.GenerativeModel(f"gemini-1.5-flash",system_instruction=f"You will be sent text from posts in a community called {group}."+
                                "If you find an event, respond in the format: Event Found!\nEvent Title/Description at Event Location on Event Date"+
                                "If you do not respond with: No Events Found"+
                                "If you find multiple events focus on the most significant one")
    model_response = model.generate_content(text)
    return model_response.text
