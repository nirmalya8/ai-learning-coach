import streamlit as st
from graph import build_graph
import json

st.set_page_config(page_title="AI Learning Coach", page_icon="🎓", layout="wide")

st.title("🎓 AI Learning Coach")
st.write("Get a curated study path with the best content from YouTube, Reddit & Blogs.")

topic = st.text_input("📌 What do you want to learn?")
days = st.number_input("📅 How many days do you have?", min_value=1, value=7)
hours = st.number_input("⏳ Hours per day you can study?", min_value=1, max_value=12, value=2)

if st.button("Generate Learning Plan 🚀"):
    with st.spinner("Fetching resources and building schedule..."):
        graph = build_graph()
        result = graph.invoke({"topic": topic, "days": days, "hours": hours})

        st.subheader("🔥 Top Resources")
        for label, items in [
            ("YouTube", result["youtube_resources"]),
            ("Blogs", result["blogs"]),
            ("Reddit", result["reddit_resources"]),
        ]:
            st.markdown(f"### 📌 {label}")
            for i in items:
                st.write(f"- [{i['title']}]({i['url']})")

        st.subheader("📆 Study Schedule")
        x = result["schedule"]
        st.markdown(f"{x}")
        # for d in result["schedule"]:
        #     try:
        #         st.markdown(f"#### Day {d['day']}")
        #     except (KeyError, TypeError):
        #         # Skip this entry if 'day' key is missing or d is not a dict
        #         continue

        #     # Iterate over items if they exist
        #     for item in d.get("items", []):
        #         st.write(f"- [{item.get('title', 'No Title')}]({item.get('url', '#')})")

        # x = result["schedule"]
        # # data_list = json.loads(x)
        # # print(data_list[0])
     