from utils.youtube_scraper import search_youtube

def get_youtube_resources(state):
    topic = state["topic"]
    state["youtube_resources"] = search_youtube(topic)[:3]
    return state
