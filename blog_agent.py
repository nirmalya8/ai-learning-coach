from utils.blog_scraper import fetch_blogs

def get_blog_resources(state):
    topic = state["topic"]
    state["blogs"] = fetch_blogs(topic)[:3]
    return state
