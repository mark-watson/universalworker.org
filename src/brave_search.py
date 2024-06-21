import requests
import json
import os
from pprint import pprint
import re
import html

api_key = os.environ.get("BRAVE_SEARCH_API_KEY")

def replace_html_tags_with_text(html_string):
    # Define the regex pattern to match HTML tags and capture their content
    html_pattern = re.compile(r'<(.*?)>(.*?)</\1>', re.DOTALL)
    
    # Function to replace each match with its content
    def replace_tag(match):
        tag_content = match.group(2)
        return tag_content

    # Replace HTML tags with their content
    clean_text = re.sub(html_pattern, replace_tag, html_string)
    
    # Unescape any HTML entities
    clean_text = html.unescape(clean_text)
    
    return clean_text


def brave_search(query, num_results = 3):
    # Define the endpoint and parameters for the API call
    url = "https://api.search.brave.com/res/v1/web/search"
    headers = {
        "X-Subscription-Token": f"{api_key}",
        "Content-Type": "application/json"
    }
    params = {
        "q": query,
        "count": num_results
    }

    # Make the API call
    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    ret = []
    if response.status_code == 200:
        # Parse the JSON response
        search_results = response.json()
        # Print the web results
        print("Web Results:\n")
        for result in search_results.get("web", {}).get("results", []):
            description = replace_html_tags_with_text(result.get("description"))
            url = result.get("url") 
            title = result.get("title")
            ret.append({"title": title, "url": url, "description": description})
    else:
        print(f"Error: {response.status_code}")
        print(response.text)
    return ret

