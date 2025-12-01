import requests

def fetch_reddit_top(topic):
    # Build query for posts phrased like: "How to learn <topic>"
    query = f"Best resources to learn {topic}"
    url = (
        "https://www.reddit.com/search.json"
        f"?q={query.replace(' ', '+')}"
        "&sort=top&t=all&limit=20"
    )

    headers = {"User-Agent": "LearningAgent/1.0"}

    try:
        res = requests.get(url, headers=headers, timeout=10).json()
        posts = res.get("data", {}).get("children", [])
        
        results = []
        for p in posts:
            title = p["data"]["title"]
            link = "https://www.reddit.com" + p["data"]["permalink"]
            score = p["data"]["score"]
            results.append({"title": title, "url": link, "score": score})

        # Sort by Reddit score (upvotes) highest first
        results = sorted(results, key=lambda x: x["score"], reverse=True)

        # Return top 10
        return results[:10]

    except Exception:
        return []
