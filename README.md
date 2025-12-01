# 📚 AI Learning Coach

An AI-powered learning assistant that creates a **personalized day-by-day study schedule** for any topic by scraping YouTube, blogs, and Reddit, and generating structured plans using a Groq LLM.

---

## **Problem Statement**

Learning online can be overwhelming:

- Too many resources: videos, blogs, Reddit posts.  
- No clear learning path from beginner → advanced.  
- Difficulty integrating multiple sources.  

**Goal:** Provide a **personalized, multi-day study schedule** with curated resources, key concepts, and measurable outcomes.

---

## **The Build**

- **Resource Scraping:** `BeautifulSoup` + `Requests` to fetch top YouTube videos, blogs, and Reddit posts.  
- **AI Schedule Generation:** `Groq LLM` (`llama-3.1-8b-instant`) generates JSON learning plans.  
- **Agent Framework:** `LangGraph` orchestrates agents sequentially (video, blog, Reddit, schedule).  
- **Frontend:** `Streamlit` for interactive UI.  
- **Dependencies:** Managed via `requirements.txt`.

---

## **Installation**

```bash
# Clone the repo
git clone https://github.com/nirmalya8/ai-learning-coach.git
cd ai-learning-coach

# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Set your Groq API key, Google CSE ID and key, and youtube API key in the .env file

Run
streamlit app.py
