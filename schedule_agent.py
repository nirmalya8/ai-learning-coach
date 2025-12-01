import os
import math
from groq import Groq


def _distribute(items, num_days=7):
    """Split a list of resources across days evenly."""
    if not items:
        return [[] for _ in range(num_days)]
    chunk = max(1, math.ceil(len(items) / num_days))
    return [items[i:i + chunk] for i in range(0, len(items), chunk)]


def build_schedule(state):
    """
    Mutates the state by adding state["schedule"].
    
    Required:
        state["topic"] (str)
        state["num_days"] (int)

    Optional (but should exist if scraping succeeded):
        state["videos"]         list[{title, url}]
        state["blogs"]          list[{title, url}]
        state["reddit_posts"]   list[{title, url}]

    Returns:
        state (dict)
    """

    topic = state["topic"]
    num_days = 7#state["num_days"] 

    videos = state.get("videos", [])
    blogs = state.get("blogs", [])
    reddit = state.get("reddit_posts", [])

    # Even resource distribution across study days
    spread_v = _distribute(videos, num_days)
    spread_b = _distribute(blogs, num_days)
    spread_r = _distribute(reddit, num_days)

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("Missing GROQ_API_KEY in environment variables")

    client = Groq(api_key=api_key)
    model = "llama-3.1-8b-instant"

    prompt = f"""
You are an expert curriculum designer.

Generate a {num_days}-day learning schedule for the topic: "{topic}".

Rules:
- Logical difficulty progression (beginner ➜ intermediate ➜ advanced)
- Concepts for each day should be actionable and measurable
- Include expected outcomes for each day

You MUST return **VALID JSON ONLY** and use this structure:

[
  {{
    "day": X,
    "study_topic": "",
    "concepts": [],
    "expected_outcome": "",
    "resources": [
      {{ "type": "video" | "blog" | "reddit", "title": "", "url": "" }}
    ]
  }}
]

Use only the following resources (already preassigned by day):
Videos: {spread_v}
Blogs: {spread_b}
Reddit: {spread_r}
"""

    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    schedule_json = response.choices[0].message.content.strip()
    state["schedule"] = schedule_json
    return state
