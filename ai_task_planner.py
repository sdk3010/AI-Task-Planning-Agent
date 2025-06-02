# ai_task_planner.py

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Load API Key only once when the module is imported
load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")
if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set. Please check your .env file.")

# Initialize LLM
llm = ChatGroq(
    temperature=0.7,
    model_name="llama3-8b-8192",
    api_key=groq_api_key
)

# Prompt Template
task_planning_template = """You are an advanced AI Task Planner. Your job is to:
1. Break down complex user requests into actionable tasks
2. Prioritize tasks logically
3. Assign appropriate tools/resources
4. Handle task dependencies

Current tasks:
{current_tasks}

User query: {input}

Response Format:
### Plan Overview
[Brief summary]

### Task Breakdown
1. [Task 1] (Priority: High/Medium/Low)
   - Dependency: [None/Task ID]
   - Resource: [Tool Name]
2. [Task 2]...
"""

planning_prompt = PromptTemplate(
    input_variables=["input", "current_tasks"],
    template=task_planning_template
)

plan_chain = LLMChain(
    llm=llm,
    prompt=planning_prompt
)

# This function will be imported and used in main.py
def generate_plan(user_input, current_tasks):
    return plan_chain.run({
        "input": user_input,
        "current_tasks": current_tasks
    })
