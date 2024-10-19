import google.generativeai as gem

def summary_from_post_text(community,text):
    import google.generativeai as gem
    gem.configure(api_key="AIzaSyA8XQWC7KyDbZozq7iLzJh-n9Ptusn3NP0")
    model = gem.GenerativeModel("gemini-1.5-flash",system_instruction=f"You are going to be sent posts from a community called {community}"+
                                " summarize the vibe and conversation in less than 3 sentences. Do not use the word vibrant.")
    model_response = model.generate_content(text)
    return model_response.text

def summary_from_desc(group, text):
    import google.generativeai as gem
    gem.configure(api_key="AIzaSyA8XQWC7KyDbZozq7iLzJh-n9Ptusn3NP0")
    model = gem.GenerativeModel("gemini-1.5-flash",system_instruction=f"You are going to be sent a description of a facebook group called {group}"+
                                " summarize and rewrite the description in less than 3 sentences")
    model_response = model.generate_content(text)
    return model_response.text