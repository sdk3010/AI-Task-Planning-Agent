# main.py

import streamlit as st
from ai_task_planner import generate_plan

# --- Simple In-Memory Task DB ---
if "task_db" not in st.session_state:
    st.session_state["task_db"] = []

def create_task(task: str) -> str:
    task_id = len(st.session_state["task_db"]) + 1
    st.session_state["task_db"].append({"id": task_id, "description": task, "status": "Pending"})
    return f"Task {task_id} created: {task}"

def list_tasks() -> str:
    db = st.session_state["task_db"]
    if not db:
        return "No tasks yet."
    return "\n".join([f"{t['id']}. {t['description']} ({t['status']})" for t in db])

st.title("🤖 AI Task Planning Agent")
st.write("Enter a complex project or goal. The AI will break it down into actionable tasks, prioritize, and suggest resources.")

user_input = st.text_area("Enter your project or goal:")

if st.button("Generate Plan") and user_input.strip():
    with st.spinner("Thinking..."):
        current_tasks = list_tasks()
        try:
            plan = generate_plan(user_input, current_tasks)
        except Exception as e:
            st.error(f"Failed to generate plan: {e}")
            plan = None
    if plan:
        st.subheader("Generated Plan")
        st.markdown(plan)
    st.subheader("Current Task List")
    if st.session_state["task_db"]:
        for t in st.session_state["task_db"]:
            st.write(f"{t['id']}. {t['description']} ({t['status']})")
    else:
        st.info("No tasks created yet.")
