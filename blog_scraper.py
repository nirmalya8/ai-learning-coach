from googleapiclient.discovery import build
# from googleapiclient.discovery import build

def fetch_blogs(query):
    """
    Fetch top 10 blogs about a topic across the internet using Google Custom Search API.
    Includes Medium, Dev.to, and WordPress blogs by filtering sites.
    """
    query = f"How to study {query}"
    api_key = ""  # Replace with your Google API key
    cse_id = ""    # Replace with your Custom Search Engine ID

    # Restrict search to known blog platforms
    sites = "site:medium.com OR site:dev.to OR site:wordpress.com"
    search_query = f"{query} {sites}"

    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_query, cx=cse_id, num=10).execute()

    # Use list comprehension format as requested
    results = [{"title": item["title"], "url": item["link"]} for item in res.get("items", [])]

    return results
