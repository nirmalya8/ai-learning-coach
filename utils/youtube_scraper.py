from googleapiclient.discovery import build

def search_youtube(query):
    query = f"How to learn {query}"
    api_key = ""
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.search().list(
        part="snippet",
        q=query,
        type="video",
        maxResults=10
    )
    response = request.execute()
    results = []
    for item in response['items']:
        results.append({
            'title': item['snippet']['title'],
            'url': f"https://www.youtube.com/watch?v={item['id']['videoId']}"
        })
    return results
