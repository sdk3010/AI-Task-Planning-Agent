AI Task Planning Agent
This project leverages Streamlit and LangChain to create an AI-driven task planning agent that helps break down complex projects or goals into actionable tasks. The app allows users to input their project or goal, and it will generate a list of tasks, prioritize them, and suggest useful resources based on the input.

Table of Contents
    Project Overview
    
    Installation
    
    Usage
    
    Example
      
    Technologies
    
    Contributors
    
    License

Project Overview
The AI Task Planning Agent uses Streamlit for the frontend interface and LangChain for generating task plans based on user input. It enables users to:

    Input a project or goal description.
    
    Automatically break it down into smaller, actionable tasks.
    
    View tasks with their status (Pending/Completed).
    
    Generate prioritized task lists and suggest additional resources.

The app works in real-time and stores tasks in an in-memory database, allowing for easy task tracking.

Installation
To get started, follow these steps:

Prerequisites
Make sure you have the following installed:

    Python 3.8 or higher
    
    pip (Python package installer)

Setup
1. Clone the repository:

    git clone https://github.com/yourusername/ai-task-planner.git
    cd ai-task-planner

2. Install required dependencies:

    pip install -r requirements.txt

3. Create a .env file to store your LangChain API key if needed:

    touch .env
   
4. Add the API key to .env:

    LANGCHAIN_API_KEY=your_api_key_here
   
5. Run the Streamlit app:

  streamlit run main.py
  
The application will launch in your browser.

Usage
    1. Open the Streamlit app.
    
    2. Type or paste your complex project or goal into the provided input box.
    
    3. Click the "Generate Plan" button.
    
    4. The AI will generate a task breakdown and provide suggestions for organizing the project.

Example
Here’s an example of how the app works:

1. Project Input:

    "Develop a machine learning model for predicting housing prices."

2. Generated Plan:
The AI breaks down the task into smaller, actionable items like:

    Collect and clean data
    
    Select a suitable machine learning model
    
    Train the model
    
    Evaluate the model's performance
    
    Deploy the model

3. Task List:

    Tasks will be shown with their ID and status (Pending/Completed).

Example output in the app:

    Task 1: Collect and clean data (Pending)
    Task 2: Select machine learning model (Pending)
    Task 3: Train the model (Pending)

    
Screenshot of the Application:

![image](https://github.com/user-attachments/assets/512fd57d-3501-4fbf-8851-dd2c31d9ca66)


Technologies
    Streamlit - For creating interactive web applications.
    
    LangChain - For language model-based task generation and planning.
    
    Python-dotenv - For environment variable management.
    
    OpenAI (Optional) - If you wish to integrate OpenAI's API for task generation.
