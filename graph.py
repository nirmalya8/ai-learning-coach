from langgraph.graph import StateGraph, END
from agents.reddit_agent import get_reddit_resources
from agents.youtube_agent import get_youtube_resources
from agents.blog_agent import get_blog_resources
from agents.schedule_agent import build_schedule

def build_graph():
    workflow = StateGraph(dict)

    workflow.add_node("reddit", get_reddit_resources)
    workflow.add_node("youtube", get_youtube_resources)
    workflow.add_node("blogs", get_blog_resources)
    workflow.add_node("schedule", build_schedule)

    workflow.set_entry_point("reddit")

    workflow.add_edge("reddit", "youtube")
    workflow.add_edge("youtube", "blogs")
    workflow.add_edge("blogs", "schedule")
    workflow.add_edge("schedule", END)

    return workflow.compile()
