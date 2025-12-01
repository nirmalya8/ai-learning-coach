from utils.reddit_scraper import fetch_reddit_top

def get_reddit_resources(state):
    topic = state["topic"]
    resources = fetch_reddit_top(topic)
    state["reddit_resources"] = resources[:3]
    return state
